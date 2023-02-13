from fastapi import FastAPI
from annotation_converter import convert, kognicFormat

app = FastAPI()

@app.get("/convert")
async def convertKognicToOpenLabel(kognicObjectRepresentation : kognicFormat.KognicAnnotation):
    ''' Create HTTP GET-request to convert Kognic to Open Label annotation. '''
    return convert.convert(kognicObjectRepresentation)
