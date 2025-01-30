Dataset **FloodNet 2021: Track 2** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/remote/eyJsaW5rIjogImZzOi8vYXNzZXRzLzI5NTBfRmxvb2ROZXQgMjAyMTogVHJhY2sgMi9mbG9vZG5ldC0yMDIxOi10cmFjay0yLURhdGFzZXROaW5qYS50YXIiLCAic2lnIjogIkd4LzlZMy9jWEg4SE40VDBza29GdWV2WkpFVi85UTNZa2FaL2MrSXAzdzQ9In0=)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='FloodNet 2021: Track 2', dst_dir='~/dataset-ninja/')
```
Make sure not to overlook the [python code example](https://developer.supervisely.com/getting-started/python-sdk-tutorials/iterate-over-a-local-project) available on the Supervisely Developer Portal. It will give you a clear idea of how to effortlessly work with the downloaded dataset.

The data in original format can be [downloaded here](https://drive.google.com/drive/folders/1g1r419bWBe4GEF-7si5DqWCjxiC8ErnY).