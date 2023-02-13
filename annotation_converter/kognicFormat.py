from pydantic import BaseModel, Field, conlist, root_validator 
from typing import Dict, Optional, List

''' Pydantic model representation of Kognic JSON schema. '''

class ShapeProperty(BaseModel):
    objectType : Optional[str] = Field(None, alias = 'ObjectType')
    unclear : Optional[bool] = Field(None, alias = 'Unclear')
    cls : str = Field(..., alias = 'class')

class ShapeProperties(BaseModel):
    all : ShapeProperty = Field(..., alias = '@all')

class Coordinate(BaseModel):
    coordinates : conlist(float, min_items=2, max_items=2)

class GeometryCoordinates(BaseModel):
    maxX : Coordinate
    maxY : Coordinate
    minX : Coordinate
    minY : Coordinate

class Geometry(BaseModel):
    coordinates : GeometryCoordinates
    type : str

class FeatureProperty(BaseModel):
    timestamp : int = Field(..., alias = '@timestamp')

class Features(BaseModel):
    geometry : Geometry
    id : str
    properties : FeatureProperty
    type : str

class Cam(BaseModel):
    type : str
    features : List[Features]

class Shapes(BaseModel):
    cam : Cam = Field(..., alias = 'CAM')

class KognicAnnotation(BaseModel):
    certainty : str
    shapeProperties : Dict[str, ShapeProperties]
    shapes : Shapes
