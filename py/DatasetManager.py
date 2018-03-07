import json
import requests
from docopt import docopt
import datetime
import pprint

def _get_images_from_dockerfinder(url="http://neri.di.unipi.it:3000/api/images"):
    try:
        res = requests.get(url)
        if res.status_code == requests.codes.ok:
            json_response = res.json()
            # print(str(json_response['count']) + " total images downloaded")
            return json_response
    except requests.exceptions.ConnectionError as e:
        raise e

def dump_dataset(file_path_json, url="http://neri.di.unipi.it:3000/api/images"):
    print("Downloading dataset from  {} ...".format(url))
    list_json_images = _get_images_from_dockerfinder(url)
    file_path_json = file_path_json.format(datetime.date.today().isoformat(),list_json_images['count'])
    with open(file_path_json, 'w') as f:
        json.dump(list_json_images, f, ensure_ascii=False)
        print("{} saved into file: {}".format(str(list_json_images['count']), file_path_json))

def read_dataset(file_path_json, limit=10):
    print("Reading dataset {} ...".format(file_path_json))
    with open(file_path_json, encoding="utf8") as json_data:
       	dataset = json.load(json_data)
        print( "{} total images in the dataset".format(dataset['count']))
        print("Printing {} images...".format(limit))
        for image in dataset['images'][:limit]:
            pprint.pprint(image)


__doc__= """DatasetManager is a python script that helps to manage the DockerImageDataset

Usage:
  DatasetManager.py dump [--file-path=<path>] [--images-url=<url>]
  DatasetManager.py read [--file-path=<path>] [--limit=<l>]
  DatasetManager.py (-h | --help)
  DatasetManager.py --version

Options:
  -h --help          Show this screen.
  --file-path=<path> Path of the JSON file where save/read DockerImageDataset   [default: ../data/{}_{}.json]
  --limit=<l>        Read the first limit number of images             [default: 10]
  --images-url=<url>  Url of the DockerFinder endpoint [default: http://neri.di.unipi.it:3000/api/images].
  --version     Show version.
"""

if __name__=="__main__":
    args = docopt(__doc__, version='DatasetManager 0.0.1')

    if args['read']:
        read_dataset(file_path_json=args['--file-path'], limit=int(args['--limit']))

    if args['dump']:
        dump_dataset(file_path_json=args['--file-path'], url=args['--images-url'])
