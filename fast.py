from fastapi import FastAPI, UploadFile
from fastapi.staticfiles import StaticFiles
from models import MetaData
from document_generation import create_report


app = FastAPI()

app.mount("/static", StaticFiles(directory="static", html=True), name="static")


@app.get("/")
async def root():
    return {"message": "Hello World!"}


@app.get("/goodbye")
async def goodbye():
    return {"message": "Goodbye!"}


@app.get("/names/{name}")
async def hello_name(name):
    return {"message": f"hello {name}"}


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    with open('static/new_file.png', 'wb') as new_file:
        contents = await file.read()
        new_file.write(contents)
    return {"filename": file.filename}


@app.post("/input_metadata/")
async def upload_metadata(data: list[MetaData]):
    create_report(data)
    return data

subapi = FastAPI()


@subapi.get("/sub")
def read_sub():
    return {"message": "Hello World from sub API"}


app.mount("/subapi", subapi)
