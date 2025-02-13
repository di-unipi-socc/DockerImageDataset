# DockerImageDataset
The `DockerImageDataset` is a dataset of docker images descriptions obtained by running   [DockerFinder](https://github.com/di-unipi-socc/DockerFinder)

```
DockerFinder  is a microservice-based tool that crawls Docker images
from a remote Docker registry (i.e., Docker Hub) and it automatically
analyses such images to produce multi-attribute descriptions.
```

If you use the `DockerImageDataset` please cite the paper *DockerFinder: Multi-attribute Search of Docker Images*

Download the citation as .bib
```
@inproceedings{BrogiNeriSoldani:dockerfinder,
  author    = {Antonio Brogi and
               Davide Neri and
               Jacopo Soldani},
  title     = {DockerFinder: Multi-attribute Search of Docker Images},
  booktitle = {2017 {IEEE} International Conference on Cloud Engineering, {IC2E}
               2017, Vancouver, BC, Canada, April 4-7, 2017},
  pages     = {273--278},
  publisher = {{IEEE}},
  year      = {2017},
  url       = {https://doi.org/10.1109/IC2E.2017.41},
  doi       = {10.1109/IC2E.2017.41},
  timestamp = {Wed, 17 May 2017 10:11:45 +0200},
  biburl    = {http://dblp.uni-trier.de/rec/bib/conf/ic2e/BrogiNS17},
  bibsource = {dblp computer science bibliography, http://dblp.org}
}
```

## The Dataset
The dataset is provided as *.json* file.
Each entry in the file is a description of a Docker image.

#### JSON description of a single Docker image

An image is described by a JSON, where the most important attributes are listed below:
 - **id**: is the unique identifier of the image inside DockerFinder.
 - **name**: is the name of the image (*repository:tag*)
 - **stars**: number of stars received by the repository containing the image (the stars are not assigned to a single image)
 - **pulls**: number of time the images from the repository is pulled from  the registry (the pulls are assigned to the repository not to the single image)
 - **size**: size (in bytes) of the image,
 - **distro**: name of the OS distribution (e.g., Ubuntu precise (12.04.5 LTS))
 - **last_scan**: datetime of the last scan performed by Docker Finder (e.g.,"2017-11-17T16:03:50.457Z",)
 - **last_updated**: datetime of the last time the image was updated in Docker Hub (e.g., "2017-04-24T22:59:38.213Z",)
 - **softwares**: list of the softwares versions supported by the image (e.g., Python 2.7)
 - "inspect_info": object eith the inspect information of an image:
      - **Id**: SHA256 as unique identifier of the image into Docker HUB (e.g., "sha256:5b117edd0b767986092e9f721ba2364951b0a271f53f1f41aff9dd1861c2d4fe")
      - **Architecture**: the architecture (e.g."amd64",)
      - **Os**: operating system of the image (e.g. "linux",)
      - **Size**: size of the image in bytes.
      - **RootFS**:
          **Layers**: list of the SHA256 of the layers  composing the image.


### Examples
Retrive the JSON description of the image **ubuntu:latest**
```
GET http://neri.di.unipi.it:3000/api/images?name=ubuntu:latest
```
Result:
```

{  
   "count":1,
   "images":[  
      {  
         "_id":"5a984f5a33d74d0011fdaa16",
         "name":"ubuntu:latest",
         "repo_name":"ubuntu",
         "stars":7319,
         "pulls":407474581,
         "description":null,
         "is_automated":false,
         "repo_owner":"",
         "tag":"latest",
         "size":42865987,
         "architecture":null,
         "repository":130,
         "creator":7,
         "last_updater":1156886,
         "last_updated":"2018-01-26T15:53:47.006Z",
         "image_id":null,
         "v2":true,
         "last_scan":"2018-03-01T19:07:06.619Z",
         "distro":"Ubuntu 16.04.3 LTS",
         "status":"updated",
         "inspect_info":{  
            "Id":"sha256:0458a4468cbceea0c304de953305b059803f67693bad463dcbe7cce2c91ba670",
            "RepoTags":[  
               "ubuntu:latest"
            ],
            "RepoDigests":[  
               "ubuntu@sha256:e27e9d7f7f28d67aa9e2d7540bdc2b33254b452ee8e60f388875e5b7d9b2b696"
            ],
            "Parent":"",
            "Comment":"",
            "Created":"2018-01-25T18:23:51.755470218Z",
            "Container":"f28a4906bba09b098de298992e6cc2503f7376a47f2d8b5238a9bb49a41aa336",
            "ContainerConfig":{  
               "Hostname":"f28a4906bba0",
               "Domainname":"",
               "User":"",
               "AttachStdin":false,
               "AttachStdout":false,
               "AttachStderr":false,
               "Tty":false,
               "OpenStdin":false,
               "StdinOnce":false,
               "Env":[  
                  "PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
               ],
               "Cmd":[  
                  "/bin/sh",
                  "-c",
                  "#(nop) ",
                  "CMD [\"/bin/bash\"]"
               ],
               "ArgsEscaped":true,
               "Image":"sha256:c78f61863d4dc2b4f3e2e6999008fbb403d40328eda3370e00349bd0f9e88d40",
               "Volumes":null,
               "WorkingDir":"",
               "Entrypoint":null,
               "OnBuild":null
            },
            "DockerVersion":"17.06.2-ce",
            "Author":"",
            "Config":{  
               "Hostname":"",
               "Domainname":"",
               "User":"",
               "AttachStdin":false,
               "AttachStdout":false,
               "AttachStderr":false,
               "Tty":false,
               "OpenStdin":false,
               "StdinOnce":false,
               "Env":[  
                  "PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
               ],
               "Cmd":[  
                  "/bin/bash"
               ],
               "ArgsEscaped":true,
               "Image":"sha256:c78f61863d4dc2b4f3e2e6999008fbb403d40328eda3370e00349bd0f9e88d40",
               "Volumes":null,
               "WorkingDir":"",
               "Entrypoint":null,
               "OnBuild":null,
               "Labels":null
            },
            "Architecture":"amd64",
            "Os":"linux",
            "Size":111707033,
            "VirtualSize":111707033,
            "GraphDriver":{  
               "Data":null,
               "Name":"aufs"
            },
            "RootFS":{  
               "Type":"layers",
               "Layers":[  
                  "sha256:ff986b10a018b48074e6d3a68b39aad8ccc002cdad912d4148c0f92b3729323e",
                  "sha256:9c7183e0ea88b265d83708dfe5b9189c4e12f9a1d8c3e5bce7f286417653f9b7",
                  "sha256:c98ef191df4b42c3fd5155d23385e75ee59707c6a448dfc6c8e4e9c005a3df11",
                  "sha256:92914665e7f61f8f19b56bf7983a2b3758cb617bef498b37adb80899e8b86e32",
                  "sha256:6f4ce6b888495c7c9bd4a0ac124b039d986a3b18250fa873d11d13b42f6a79f4"
               ]
            }
         },
         "__v":0,
         "softwares":[  
            {  
               "software":"erl",
               "ver":"2"
            },
            {  
               "software":"perl",
               "ver":"5.22.1"
            },
            {  
               "software":"bash",
               "ver":"4.3.48"
            },
            {  
               "software":"tar",
               "ver":"1.28"
            }
         ]
      }
   ]
}
```
