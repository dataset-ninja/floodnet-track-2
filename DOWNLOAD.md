Dataset **FloodNet 2021: Track 2** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/supervisely-supervisely-assets-public/teams_storage/m/7/r7/nhzNbmKhsJQCzuyIinKr0lexXK7jH938TOc1q8M8V54qmp86bPSNkBDu8Z2slKiF0gaJjIfOVdoL0w98foRHo030grn1JBFYx5c0hTPPR6E5ambZF2ZkskwvyBQt.tar)

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