The **FloodNet 2021: A High Resolution Aerial Imagery Dataset for Post Flood Scene Understanding** provides high-resolution UAS imageries with detailed semantic annotation regarding the damages. To advance the damage assessment process for post-disaster scenarios, the authors of the dataset presented a unique challenge considering classification, semantic segmentation, and visual question answering highlighting the UAS imagery-based FloodNet dataset. The Challenge has two tracks: 1) Image Classification and Semantic Segmentation ([available on DatasetNinja](https://datasetninja.com/floodnet)); and 2) Visual Question Answering (current).

Frequent, and increasingly severe, natural disasters threaten human health, infrastructure, and natural systems. The provision of accurate, timely, and understandable information has the potential to revolutionize disaster management. For quick response and recovery on a large scale, after a natural disaster such as a hurricane, access to aerial images is critically important for the response team. The emergence of small unmanned aerial systems (UAS) along with inexpensive sensors presents the opportunity to collect thousands of images after each natural disaster with high flexibility and easy maneuverability for rapid response and recovery. Moreover, UAS can access hard-to-reach areas and perform data collection tasks that can be unsafe for humans if not impossible. Despite all these advancements and efforts to collect such large datasets, analyzing them and extracting meaningful information remains a significant challenge in scientific communities.

The data was collected with a small UAS platform, DJI Mavic Pro quadcopters, after Hurricane Harvey. The whole dataset has 2343 images, divided into training (~60%), validation (~20%), and test (~20%) sets.

For Track 1 (Semi-supervised Classification and Semantic Segmentation), in the training set, there are around 400 labeled images (~25% of the training set) and around 1050 unlabeled images (~75% of the training set). For Track 2 (Supervised VQA), in the training set, there are around 1450 images and there are a total of 4511 image-question pairs.

The presented dataset contains annotations from **Track 2**. For the Visual Question Answering (VQA) task, the images are associated with multiple questions. These questions will be divided into the following categories:

* **Simple Counting**: Questions will be designed to count the number of objects regardless of their attribute. For example: “how many buildings are there in the image?”.
* **Complex Counting**: Questions will be asked to count the number of objects belonging to a specific attribute. For example: “how many flooded buildings are there in the image?”.
* **Condition Recognition**: In this category, all the questions are mainly designed to ask questions regarding the condition of the object and the neighborhood. For example: “What is the condition of the road in the given image?”.
* **Yes/No type of question**: For this type of question, the answer will be either a ‘Yes’ or a ‘No’. For example: “Is there any flooded road?”.


