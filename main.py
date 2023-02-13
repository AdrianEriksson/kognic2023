from fastapi import FastAPI
from annotation_converter import convert, kognicFormat

app = FastAPI()

@app.get("/convert")
async def convertKognicToOpenLabel(kognicData : kognicFormat.KognicAnnotation):
    return convert.convert(kognicData)
