from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles


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


subapi = FastAPI()


@subapi.get("/sub")
def read_sub():
    return {"message": "Hello World from sub API"}


app.mount("/subapi", subapi)
