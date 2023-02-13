from pydantic import BaseModel, Field, conlist
from typing import Dict, Optional, List

''' Pydantic model representation of Open Label JSON schema. '''

class Objects(BaseModel):
    name : str
    type : str 

class BoundingBox(BaseModel):
    name : str
    stream : str
    val : conlist(float, min_items=4, max_items=4)

class Boolean(BaseModel):
    name : str
    val : bool

class Text(BaseModel):
    name : str
    val : str

class FrameObjectData(BaseModel):
    bbox : List[BoundingBox]
    boolean : Optional[List[Boolean]]
    text : Optional[List[Text]]

class FrameObject(BaseModel):
    objectData : FrameObjectData = Field(..., alias = 'object_data')

    class Config:
        allow_population_by_field_name = True

class Frames(BaseModel):
    objects : Dict[str, FrameObject]

class OpenLabel(BaseModel):
    objects : Dict[str, Objects]
    frames : Dict[str, Frames]

class Data(BaseModel):
    openLabel : OpenLabel = Field(..., alias = 'openlabel')

    class Config:
        allow_population_by_field_name = True

class OpenLabelAnnotation(BaseModel):
    data : Data