from typing import Union
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get("/hello/{name}")
def greet(name: str):
    return {"response": f"Hello {name}"}


@app.get("/goodbye/{name}")
def farewell(name: str):
    return {"response": f"Goodbye {name}!"}


@app.get("/test_with_latest")
def test():
    return {"response": "The latest image is pulled!"}


@app.get("/version_number")
def version_number():
    return {"response": "v0.2.0-multi-container-app"}


@app.get("/streamlit_greeting")
def streamlit_greeting(name: str, age: Union[str, int]):
    greeting = ""
    age = int(age)

    if age < 5:
        greeting = "TA-DA"
    elif 5 <= age < 12:
        greeting = "Hoi"
    elif 12 <= age < 18:
        greeting = "Yo"
    elif 18 <= age < 30:
        greeting = "Hallo"
    elif age > 30:
        greeting = "Goedendag"
    return {"response": f"{greeting} {name}"}


@app.get("/streamlit_goodbye")
def streamlit_farewell(name: str, age: Union[str, int]):
    farewell = ""
    age = int(age)

    if age < 5:
        farewell = "TA-DA"
    elif 5 <= age < 18:
        farewell = "Doei"
    elif 18 <= age < 30:
        farewell = "De ballen"
    elif age > 30:
        farewell = "Tot ziens"
    return {"response": f"{farewell} {name}"}


@app.get("/dummy_functionality")
def dummy_func():
    return {"response": f"Dummy functionality implemented!"}
