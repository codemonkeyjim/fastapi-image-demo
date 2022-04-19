from fastapi import FastAPI, UploadFile
from PIL import Image


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/image/")
async def create_file(image: UploadFile):
    pil_image = Image.open(image.file)
    return {
        "filename": image.filename,
        "content_type": image.content_type,
        "format": pil_image.format,
        "width": pil_image.size[0],
        "height": pil_image.size[1],
        "mode": pil_image.mode,
    }
