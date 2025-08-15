Dataset **FloodNet 2021: Track 2** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/remote/eyJsaW5rIjogInMzOi8vc3VwZXJ2aXNlbHktZGF0YXNldHMvMjk1MF9GbG9vZE5ldCAyMDIxOiBUcmFjayAyL2Zsb29kbmV0LTIwMjE6LXRyYWNrLTItRGF0YXNldE5pbmphLnRhciIsICJzaWciOiAialdpekkvWE5tV1FOM3V1RUh0bWd2eUJCcjYybXB4TUR3NXdJRzlWRWNZZz0ifQ==?response-content-disposition=attachment%3B%20filename%3D%22floodnet-2021%3A-track-2-DatasetNinja.tar%22)

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