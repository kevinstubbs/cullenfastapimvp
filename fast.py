from fastapi import FastAPI, UploadFile, File
from fastapi.staticfiles import StaticFiles
from models import MetaData
from document_generation import create_report
import os

app = FastAPI()

app.mount("/reports", StaticFiles(directory="reports", html=True), name="reports")


@app.get("/")
async def root():
    return {"message": "Hello World!"}


@app.get("/goodbye")
async def goodbye():
    return {"message": "Goodbye!"}


@app.get("/names/{name}")
async def hello_name(name):
    return {"message": f"hello {name}"}


@app.post("/uploadfile/{report_name}")
async def create_upload_file(project_folder: str, file: UploadFile):
    if not os.path.isdir(project_folder):
        os.mkdir(project_folder)
    with open(''.join([project_folder, '/', file.filename]), 'wb') as new_file:
        contents = await file.read()
        new_file.write(contents)
    return {"filename": file.filename}


@app.post("/input_metadata/")
async def upload_metadata(data: list[MetaData]):
    report = create_report(data)
    return report

subapi = FastAPI()


@subapi.get("/sub")
def read_sub():
    return {"message": "Hello World from sub API"}


app.mount("/subapi", subapi)
