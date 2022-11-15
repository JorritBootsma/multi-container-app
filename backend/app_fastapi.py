import os
from typing import Union
from fastapi import Depends, FastAPI

import crud
import models
import schemas
from database import Session, engine
from functions import get_greeting, get_farewell, validate_integer_input

testing = "False"
try:
    testing = os.environ["TESTING"]
except KeyError:
    pass

if not eval(testing):
    # Drop all tables if present
    # print(Base.metadata.tables.keys())
    # Base.metadata.drop_all(bind=engine)

    models.Base.metadata.create_all(bind=engine)

app = FastAPI(debug=True)


# Dependency
def get_db():
    Session.configure(autocommit=False, autoflush=False, bind=engine)
    db = Session()
    try:
        yield db
    finally:
        db.close()


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
    return {"response": "v1.0.2"}


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
    return {"response": "Dummy functionality implemented!"}


@app.post("/persist_in_db")
def persist_in_db(name: str, age: Union[str, int], db: Session = Depends(get_db)):
    valid, error_message = validate_integer_input(age, "age")
    if not valid:
        return {"response": error_message}

    user = schemas.UserCreate(name=name, age=int(age))
    res = crud.create_user(db, user=user)
    print(res)
    return {"response": True, "res": res}


@app.get("/get_all_users")
def get_all_users(db: Session = Depends(get_db)):
    res = crud.get_users(db)
    return {"response": True, "res": res}
