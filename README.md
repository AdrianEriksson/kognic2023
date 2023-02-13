# Kognic Coding Assignment

## Overview
This repository includes a REST API supporting conversion of Kognic to Open Label annotations schemas, utilizing *FastAPI* and custom package *annotation_converter*.

## Annotation Converter
Annotation converter package includes functionality for converting Kognic to Open Label annotation. This is done by creating a Pydantic object representation of the  JSON-schemas, allowing conversion between the respective representations.

The package can be installed using pip in the root directory of the repository by entering:
```
pip install .
```

Kognic JSON-schema presented as a model representation using Pydantic.
```json
{
  "title": "KognicAnnotation",
  "type": "object",
  "properties": {
    "certainty": {
      "title": "Certainty",
      "type": "string"
    },
    "shapeProperties": {
      "title": "Shapeproperties",
      "type": "object",
      "additionalProperties": {
        "$ref": "#/definitions/ShapeProperties"
      }
    },
    "shapes": {
      "$ref": "#/definitions/Shapes"
    }
  },
  "required": [
    "certainty",
    "shapeProperties",
    "shapes"
  ],
  "definitions": {
    "ShapeProperty": {
      "title": "ShapeProperty",
      "type": "object",
      "properties": {
        "ObjectType": {
          "title": "Objecttype",
          "type": "string"
        },
        "Unclear": {
          "title": "Unclear",
          "type": "boolean"
        },
        "class": {
          "title": "Class",
          "type": "string"
        }
      },
      "required": [
        "class"
      ]
    },
    "ShapeProperties": {
      "title": "ShapeProperties",
      "type": "object",
      "properties": {
        "@all": {
          "$ref": "#/definitions/ShapeProperty"
        }
      },
      "required": [
        "@all"
      ]
    },
    "Coordinate": {
      "title": "Coordinate",
      "type": "object",
      "properties": {
        "coordinates": {
          "title": "Coordinates",
          "minItems": 2,
          "maxItems": 2,
          "type": "array",
          "items": {
            "type": "number"
          }
        }
      },
      "required": [
        "coordinates"
      ]
    },
    "GeometryCoordinates": {
      "title": "GeometryCoordinates",
      "type": "object",
      "properties": {
        "maxX": {
          "$ref": "#/definitions/Coordinate"
        },
        "maxY": {
          "$ref": "#/definitions/Coordinate"
        },
        "minX": {
          "$ref": "#/definitions/Coordinate"
        },
        "minY": {
          "$ref": "#/definitions/Coordinate"
        }
      },
      "required": [
        "maxX",
        "maxY",
        "minX",
        "minY"
      ]
    },
    "Geometry": {
      "title": "Geometry",
      "type": "object",
      "properties": {
        "coordinates": {
          "$ref": "#/definitions/GeometryCoordinates"
        },
        "type": {
          "title": "Type",
          "type": "string"
        }
      },
      "required": [
        "coordinates",
        "type"
      ]
    },
    "FeatureProperty": {
      "title": "FeatureProperty",
      "type": "object",
      "properties": {
        "@timestamp": {
          "title": "@Timestamp",
          "type": "integer"
        }
      },
      "required": [
        "@timestamp"
      ]
    },
    "Features": {
      "title": "Features",
      "type": "object",
      "properties": {
        "geometry": {
          "$ref": "#/definitions/Geometry"
        },
        "id": {
          "title": "Id",
          "type": "string"
        },
        "properties": {
          "$ref": "#/definitions/FeatureProperty"
        },
        "type": {
          "title": "Type",
          "type": "string"
        }
      },
      "required": [
        "geometry",
        "id",
        "properties",
        "type"
      ]
    },
    "Cam": {
      "title": "Cam",
      "type": "object",
      "properties": {
        "type": {
          "title": "Type",
          "type": "string"
        },
        "features": {
          "title": "Features",
          "type": "array",
          "items": {
            "$ref": "#/definitions/Features"
          }
        }
      },
      "required": [
        "type",
        "features"
      ]
    },
    "Shapes": {
      "title": "Shapes",
      "type": "object",
      "properties": {
        "CAM": {
          "$ref": "#/definitions/Cam"
        }
      },
      "required": [
        "CAM"
      ]
    }
  }
}
```

Open Label JSON-schema presented as a model representation using Pydantic.
```json
{
  "title": "OpenLabelAnnotation",
  "type": "object",
  "properties": {
    "data": {
      "$ref": "#/definitions/Data"
    }
  },
  "required": [
    "data"
  ],
  "definitions": {
    "Objects": {
      "title": "Objects",
      "type": "object",
      "properties": {
        "name": {
          "title": "Name",
          "type": "string"
        },
        "type": {
          "title": "Type",
          "type": "string"
        }
      },
      "required": [
        "name",
        "type"
      ]
    },
    "BoundingBox": {
      "title": "BoundingBox",
      "type": "object",
      "properties": {
        "name": {
          "title": "Name",
          "type": "string"
        },
        "stream": {
          "title": "Stream",
          "type": "string"
        },
        "val": {
          "title": "Val",
          "minItems": 4,
          "maxItems": 4,
          "type": "array",
          "items": {
            "type": "number"
          }
        }
      },
      "required": [
        "name",
        "stream",
        "val"
      ]
    },
    "Boolean": {
      "title": "Boolean",
      "type": "object",
      "properties": {
        "name": {
          "title": "Name",
          "type": "string"
        },
        "val": {
          "title": "Val",
          "type": "boolean"
        }
      },
      "required": [
        "name",
        "val"
      ]
    },
    "Text": {
      "title": "Text",
      "type": "object",
      "properties": {
        "name": {
          "title": "Name",
          "type": "string"
        },
        "val": {
          "title": "Val",
          "type": "string"
        }
      },
      "required": [
        "name",
        "val"
      ]
    },
    "FrameObjectData": {
      "title": "FrameObjectData",
      "type": "object",
      "properties": {
        "bbox": {
          "title": "Bbox",
          "type": "array",
          "items": {
            "$ref": "#/definitions/BoundingBox"
          }
        },
        "boolean": {
          "title": "Boolean",
          "type": "array",
          "items": {
            "$ref": "#/definitions/Boolean"
          }
        },
        "text": {
          "title": "Text",
          "type": "array",
          "items": {
            "$ref": "#/definitions/Text"
          }
        }
      },
      "required": [
        "bbox"
      ]
    },
    "FrameObject": {
      "title": "FrameObject",
      "type": "object",
      "properties": {
        "object_data": {
          "$ref": "#/definitions/FrameObjectData"
        }
      },
      "required": [
        "object_data"
      ]
    },
    "Frames": {
      "title": "Frames",
      "type": "object",
      "properties": {
        "objects": {
          "title": "Objects",
          "type": "object",
          "additionalProperties": {
            "$ref": "#/definitions/FrameObject"
          }
        }
      },
      "required": [
        "objects"
      ]
    },
    "OpenLabel": {
      "title": "OpenLabel",
      "type": "object",
      "properties": {
        "objects": {
          "title": "Objects",
          "type": "object",
          "additionalProperties": {
            "$ref": "#/definitions/Objects"
          }
        },
        "frames": {
          "title": "Frames",
          "type": "object",
          "additionalProperties": {
            "$ref": "#/definitions/Frames"
          }
        }
      },
      "required": [
        "objects",
        "frames"
      ]
    },
    "Data": {
      "title": "Data",
      "type": "object",
      "properties": {
        "openlabel": {
          "$ref": "#/definitions/OpenLabel"
        }
      },
      "required": [
        "openlabel"
      ]
    }
  }
}
```

## API
The API is implemented using *FastAPI* with *Uvicorn*.

### Starting the API
The API can be started using the following command in the root directory of the repository by entering:

```
uvicorn main:app
```

Note: Use "--reload" as additional parameter to enable automatic reload for simple debugging purposes. 

### Using the API
The API support GET HTTP-request with Kognic JSON annotation as payload, returning the corresponding Open Label translaton. See example CURL syntax below:

```
curl --request GET 
     --url http://127.0.0.1:8000/convert
     --header 'Content-Type: application/json'
     --data @path/to/input.json
```