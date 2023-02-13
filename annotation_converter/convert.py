from annotation_converter import kognicFormat, openLabelFormat

def get_bbox_from_epbb(xmax, xmin, ymax, ymin):
    ''' Converts extreme point to 2D canonical bounding box. '''
    return [.5*(xmax - xmin) + xmin, .5*(ymax - ymin) + ymin, xmax - xmin, ymax - ymin]

def convert(kognicObjectRepresentation : kognicFormat.KognicAnnotation):
    ''' Converts model representation of Kognic to Open Label annotation as dictionary. '''
    
    # Prepare empty dicts for later processing.
    # "in"-prefix denotes temporary object for creation of Open Label annotation.
    inObjects = {}
    inFrameObjects = {}
    inFrames = {}
    
    featureDict = {feature.id : feature for feature in kognicObjectRepresentation.shapes.cam.features}

    for key, shapeProperty in kognicObjectRepresentation.shapeProperties.items():
        inObjects[key] = openLabelFormat.Objects(name = key, type = shapeProperty.all.cls)
        
        if key not in featureDict:
            raise Exception("Property key not found as feature.")
            
        feature = featureDict[key]

        maxX = feature.geometry.coordinates.maxX.coordinates[0]
        minX = feature.geometry.coordinates.minX.coordinates[0]
        maxY = feature.geometry.coordinates.maxY.coordinates[1]
        minY = feature.geometry.coordinates.minY.coordinates[1]
        bboxVal = get_bbox_from_epbb(maxX, minX, maxY, minY)
        bboxname = 'bbox-' + key.split('-')[0]

        inBbox = openLabelFormat.BoundingBox(name = bboxname, stream = 'CAM', val = bboxVal)
        inObjectData = openLabelFormat.FrameObjectData(bbox = [inBbox])

        if shapeProperty.all.unclear is not None:
            inBoolean = openLabelFormat.Boolean(name = 'Unclear', val = shapeProperty.all.unclear)
            inObjectData.boolean = [inBoolean]

        if shapeProperty.all.objectType is not None:
            inText = openLabelFormat.Text(name = 'ObjectType', val = shapeProperty.all.objectType)
            inObjectData.text = [inText]

        inFrameObject = openLabelFormat.FrameObject(objectData = inObjectData)
        inFrameObjects[key] = inFrameObject

        if feature.properties.timestamp not in inFrames.keys():
                inFrames[feature.properties.timestamp] = {'objects' : {}}

        inFrames[feature.properties.timestamp]['objects'] = inFrameObjects

    inOpenLabel = openLabelFormat.OpenLabel(objects = inObjects, frames = inFrames)
    inData = openLabelFormat.Data(openLabel = inOpenLabel)

    openLabelObjectRepresentation = openLabelFormat.OpenLabelAnnotation(data = inData)
    return openLabelObjectRepresentation.dict(by_alias = True, exclude_none = True)
