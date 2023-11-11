import json
import os
import shutil
from urllib.parse import unquote, urlparse

import supervisely as sly
from supervisely.io.fs import get_file_name_with_ext, get_file_size
from tqdm import tqdm

import src.settings as s
from dataset_tools.convert import unpack_if_archive


def count_files(path, extension):
    count = 0
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(extension):
                count += 1
    return count


def convert_and_upload_supervisely_project(
    api: sly.Api, workspace_id: int, project_name: str
) -> sly.ProjectInfo:
    images_path = "/mnt/d/datasetninja-raw/floodnet-track-2/Images"
    questions_path = "/mnt/d/datasetninja-raw/floodnet-track-2/Questions"

    batch_size = 30

    def create_ann(image_path, qjson):
        tags = []

        image_np = sly.imaging.image.read(image_path)[:, :, 0]
        img_height = image_np.shape[0]
        img_wight = image_np.shape[1]

        filtered_data = {
            k: v for k, v in qjson.items() if v["Image_ID"] == get_file_name_with_ext(image_path)
        }

        for k, v in filtered_data.items():
            new_element = {"Question_ID": k}
            _v_ = {k_: v_ for k_, v_ in v.items() if k_ != "Image_ID"}
            val = str({**new_element, **_v_})
            tags.append(sly.Tag(tag_question, value=val))

        return sly.Annotation(img_size=(img_height, img_wight), img_tags=tags)

    tag_question = sly.TagMeta("question", sly.TagValueType.ANY_STRING)
    tag_metas = [tag_question]

    project = api.project.create(workspace_id, project_name, change_name_if_conflict=True)
    meta = sly.ProjectMeta(tag_metas=tag_metas)
    api.project.update_meta(project.id, meta.to_json())

    ds_name_to_json = {
        "Test_Image": "Test_Question.json",
        "Train_Image": "Training Question.json",
        "Valid_Image": "Valid Question.json",
    }

    for ds_name in os.listdir(images_path):
        curr_images_path = os.path.join(images_path, ds_name)

        dataset = api.dataset.create(project.id, ds_name.lower(), change_name_if_conflict=True)

        images_names = os.listdir(curr_images_path)

        progress = sly.Progress("Create dataset {}".format(ds_name.lower()), len(images_names))

        qjson_path = os.path.join(questions_path, ds_name_to_json[ds_name])
        with open(qjson_path) as json_file:
            qjson = json.load(json_file)

        for img_names_batch in sly.batched(images_names, batch_size=batch_size):
            images_pathes_batch = [
                os.path.join(curr_images_path, image_name) for image_name in img_names_batch
            ]

            img_infos = api.image.upload_paths(dataset.id, img_names_batch, images_pathes_batch)
            img_ids = [im_info.id for im_info in img_infos]

            anns_batch = [create_ann(image_path, qjson) for image_path in images_pathes_batch]
            api.annotation.upload_anns(img_ids, anns_batch)

            progress.iters_done_report(len(img_names_batch))

    return project
