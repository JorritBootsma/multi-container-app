from typing import Union
from fastapi import FastAPI

from functions import get_greeting, get_farewell, validate_integer_input

app = FastAPI(debug=True)


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
    return {"response": "v1.0.1"}


@app.get("/streamlit_greeting")
def streamlit_greeting(name: str, age: Union[str, int]):
    valid, error_message = validate_integer_input(age, "age")
    if not valid:
        return {"response": error_message}

    greeting = get_greeting(int(age))
    return {"response": f"{greeting} {name}"}


@app.get("/streamlit_goodbye")
def streamlit_farewell(name: str, age: Union[str, int]):
    valid, error_message = validate_integer_input(age, "age")
    if not valid:
        return {"response": error_message}

    farewell_ = get_farewell(int(age))
    return {"response": f"{farewell_} {name}"}


@app.get("/dummy_functionality")
def dummy_func():
    return {"response": f"Dummy functionality implemented!"}
