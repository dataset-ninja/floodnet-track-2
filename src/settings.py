from typing import Dict, List, Optional, Union

from dataset_tools.templates import (
    AnnotationType,
    Category,
    CVTask,
    Domain,
    Industry,
    License,
    Research,
)

##################################
# * Before uploading to instance #
##################################
PROJECT_NAME: str = "FloodNet 2021: Track 2"
PROJECT_NAME_FULL: str = "FloodNet 2021: A High Resolution Aerial Imagery Dataset for Post Flood Scene Understanding (Track 2)"
HIDE_DATASET = False  # set False when 100% sure about repo quality

##################################
# * After uploading to instance ##
##################################
LICENSE: License = License.CC_BY_SA_4_0(
    source_url="https://competitions.codalab.org/competitions/30320#learn_the_details-terms_and_conditions"
)
APPLICATIONS: List[Union[Industry, Domain, Research]] = [
    Industry.SearchAndRescue(),
    Industry.Environmental(),
]
CATEGORY: Category = Category.Aerial(
    extra=[Category.Safety(), Category.Environmental(), Category.Drones()]
)

CV_TASKS: List[CVTask] = [CVTask.Identification()]
ANNOTATION_TYPES: List[AnnotationType] = []

RELEASE_DATE: Optional[str] = "2020-12-05"  # e.g. "YYYY-MM-DD"
if RELEASE_DATE is None:
    RELEASE_YEAR: int = None

HOMEPAGE_URL: str = "http://www.classic.grss-ieee.org/earthvision2021/challenge.html"
# e.g. "https://some.com/dataset/homepage"

PREVIEW_IMAGE_ID: int = 8507228
# This should be filled AFTER uploading images to instance, just ID of any image.

GITHUB_URL: str = "https://github.com/dataset-ninja/floodnet-track-2"
# URL to GitHub repo on dataset ninja (e.g. "https://github.com/dataset-ninja/some-dataset")

##################################
### * Optional after uploading ###
##################################
DOWNLOAD_ORIGINAL_URL: Optional[
    Union[str, dict]
] = "https://drive.google.com/drive/folders/1g1r419bWBe4GEF-7si5DqWCjxiC8ErnY"
# Optional link for downloading original dataset (e.g. "https://some.com/dataset/download")

CLASS2COLOR: Optional[Dict[str, List[str]]] = None
# If specific colors for classes are needed, fill this dict (e.g. {"class1": [255, 0, 0], "class2": [0, 255, 0]})

PAPER: Optional[Union[str, List[str], Dict[str, str]]] = "https://arxiv.org/abs/2012.02951"
BLOGPOST: Optional[Union[str, List[str], Dict[str, str]]] = None
REPOSITORY: Optional[Union[str, List[str], Dict[str, str]]] = {
    "GitHub": "https://github.com/BinaLab/FloodNet-Challenge-EARTHVISION2021#floodnet-dataset"
}

CITATION_URL: Optional[
    str
] = "https://github.com/BinaLab/FloodNet-Challenge-EARTHVISION2021#paper-link"
AUTHORS: Optional[List[str]] = [
    "Maryam Rahnemoonfar",
    "Tashnim Chowdhury",
    "Argho Sarkar",
    "Debvrat Varshney",
    "Masoud Yari",
    "Robin Murphy",
]
AUTHORS_CONTACTS: Optional[List[str]] = [
    "maryam@umbc.edu",
    "tchowdhury@umbc.edu",
    "asarkar2@umbc.edu",
    "dvarshney@umbc.edu",
    "yari@umbc.edu",
    "murphy@cse.tamu.edu",
]

ORGANIZATION_NAME: Optional[Union[str, List[str]]] = [
    "UMBC, USA",
    "Texas A&M University",
    "Dewberry, USA",
]
ORGANIZATION_URL: Optional[Union[str, List[str]]] = [
    "https://umbc.edu/",
    "https://www.tamu.edu/",
    "https://www.dewberry.com/",
]

SLYTAGSPLIT: Optional[Dict[str, List[str]]] = {
    "__PRETEXT__": "Every image has its ***question*** tag"
}
TAGS: List[str] = None


SECTION_EXPLORE_CUSTOM_DATASETS: Optional[List[str]] = None

##################################
###### ? Checks. Do not edit #####
##################################


def check_names():
    fields_before_upload = [PROJECT_NAME]  # PROJECT_NAME_FULL
    if any([field is None for field in fields_before_upload]):
        raise ValueError("Please fill all fields in settings.py before uploading to instance.")


def get_settings():
    if RELEASE_DATE is not None:
        global RELEASE_YEAR
        RELEASE_YEAR = int(RELEASE_DATE.split("-")[0])

    settings = {
        "project_name": PROJECT_NAME,
        "project_name_full": PROJECT_NAME_FULL or PROJECT_NAME,
        "hide_dataset": HIDE_DATASET,
        "license": LICENSE,
        "applications": APPLICATIONS,
        "category": CATEGORY,
        "cv_tasks": CV_TASKS,
        "annotation_types": ANNOTATION_TYPES,
        "release_year": RELEASE_YEAR,
        "homepage_url": HOMEPAGE_URL,
        "preview_image_id": PREVIEW_IMAGE_ID,
        "github_url": GITHUB_URL,
    }

    if any([field is None for field in settings.values()]):
        raise ValueError("Please fill all fields in settings.py after uploading to instance.")

    settings["release_date"] = RELEASE_DATE
    settings["download_original_url"] = DOWNLOAD_ORIGINAL_URL
    settings["class2color"] = CLASS2COLOR
    settings["paper"] = PAPER
    settings["blog"] = BLOGPOST
    settings["repository"] = REPOSITORY
    settings["citation_url"] = CITATION_URL
    settings["authors"] = AUTHORS
    settings["authors_contacts"] = AUTHORS_CONTACTS
    settings["organization_name"] = ORGANIZATION_NAME
    settings["organization_url"] = ORGANIZATION_URL
    settings["slytagsplit"] = SLYTAGSPLIT
    settings["tags"] = TAGS

    settings["explore_datasets"] = SECTION_EXPLORE_CUSTOM_DATASETS

    return settings
