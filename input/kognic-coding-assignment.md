# Kognic Coding Assignment

This coding assignment is designed to mimic some of the coding tasks that you will encounter while working together with Kognic. For a reasonably experienced Python developer this assignments should feel fairly straightforward and not take much more than a couple of hours. In order to complete this assignment you need to be proficient in Python, know how python packages are generated and be familiar with basic REST APIs. You are free to use any libraries you want

## Assignment - Annotation Format Conversion Service

### Background
Annotations are produced during the process of labling data. An annotation is a text file (usually json) that describes the content of the data. If you for instance were to produce a bounding-box annotation for an image containing a vehicle the resulting annotation could look something like this:
```
{
    "objects": [
        {
            "type": "vehicle",
            "id": "d9c42ffd-ed63-4f6a-8ac7-227de8a9945f"
            "position": {
                "x_min": 50,
                "x_max": 150,
                "y_min": 50,
                "y_max": 150
            }
        }
    ]
}
```

One challenge when dealing with annotations is that there many different formats available. Due to this there is a need for being able to convert to and from different formats, all while making sure that the contents of the annotations are not unaltered.

### Assignment
For this assignment you are tasked with creating a REST API that performs conversion of annotations from a simplified version of the *Kognic* format to a simplified version of the *OpenLABEL* format. In order to implement this you have two files available, `kognic_1.json` containing the annotation in the Kognic format, as well as `open_label_1.json` containing the same annotation but in OpenLABEL format instead. These files describe an annotation consisting of 3 different classes - `Vehicle`, `Animal` and `LicensePlate` and contain 3 instances of the `Vehicle` class, 1 instance of the `Animal` class and 1 instance of the `LicensePlate` class.

The API should be able convert annotations containing any number instances of these 3 different classes.

The API should be able to receive a GET http-request containing the kognic judgement as a payload and respond with the OpenLABEL converted annotation.

In order to make communication with the API easier you are also expected to provide a python client in the form of a pip-installable python package. You are free to design the client as you wish as long as it can after installation be used in a way similar to this example:

```python
from annotation_converter import convert
import json

path_to_kognic_annotation = 'kognic_1.json'
with open(path_to_kognic_annotation, 'r') as content:
    kognic_annotation = json.load(content)

open_label_annotation = convert(kognic_annotation)
```
### Regarding ASAM OpenLabel
Included is a HTML file with documentation regarding the ASAM OpenLabel format.

### Regarding Extreme Point Bounding Boxes
The *Kognic* format uses extreme point bounding boxes. An extreme point bounding box is defined by 4 points that are placed at the extreme points of the object it should contain. 
These 4 points are:
- minX
- maxX
- minY
- maxY

See attached image from email for reference. 


### How to deliver the assignment
The finished assignment should be shared either as a .zip-file or preferably as a github repository. In addition to all the neccessary code it should contain a README that describes:
1. How to start the REST API locally
2. How to install and use the python-library

