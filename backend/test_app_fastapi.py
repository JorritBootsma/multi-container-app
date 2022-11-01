from fastapi.testclient import TestClient

from app_fastapi import app

client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200


def test_streamlit_greeting():
    response = client.get("/streamlit_greeting", params={"name": "X", "age": 10})
    assert response.status_code == 200
    assert response.json()["response"] == "Hoi X"


def test_greeting_int_as_string_age():
    response = client.get("/streamlit_greeting", params={"name": "X", "age": '10'})
    assert response.json()["response"] == "Hoi X"


def test_greeting_string_age():
    response = client.get("/streamlit_greeting", params={"name": "X", "age": 'a'})
    assert response.json()["response"] == \
           "Couldn't convert the `age` input to an integer. " \
           "Please insert a valid number"


if __name__ == "__main__":
    test_read_root()
    test_streamlit_greeting()