# DockerImageDataset



## Python script
The folder *py* contains the python script for managing the dataset of Docker images.
```
cd py
```
Install the python library dependencies:
```
pip install requirements.txt
```

The `DatasetManager.py` is the script that helps in managing the dataset
```
DatasetManager is a python script that helps to manage the DockerImageDataset

Usage:
  DatasetManager.py dump [--file-path=<path>] [--images-url=<url>]
  DatasetManager.py read [--file-path=<path>] [--limit=<l>]
  DatasetManager.py officials
  DatasetManager.py (-h | --help)
  DatasetManager.py --version

Options:
  -h --help          Show this screen.
  --file-path=<path> Path of the JSON file where save/read DockerImageDataset   [default: ../data/{}_{}.json]
  --limit=<l>        Read the first limit number of images             [default:10]
  --images-url=<url>  Url of the DockerFinder endpoint [default: http://neri.di.unipi.it:3000/api/images].
  --version     Show version.
```

##### Dump the dataset
Run the following command to dump the dataset from the DockerFinder endpoint.
```
python DatasetManager.py dump
```

#### Read the dataset
Read the file `../data/2018-03-07_15779.json`and print only the first image.
```
python DatasetManager.py read --file=../data/2018-03-07_15779.json --limit=1    
```
