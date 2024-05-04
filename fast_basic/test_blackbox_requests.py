import pytest
import requests
import time

@pytest.fixture(scope="function")
def items():
    return {
        "items": {
            "0": {
                "name": "Hammer",
                "price": 9.99,
                "count": 20,
                "id": 0,
                "category": "tools",
            },
            "1": {
                "name": "Pliers",
                "price": 5.99,
                "count": 20,
                "id": 1,
                "category": "tools",
            },
            "2": {
                "name": "Nails",
                "price": 1.99,
                "count": 100,
                "id": 2,
                "category": "consumables",
            },
        }
    }


def localhost(path=""):
    return f"http://127.0.0.1:8000{path}"


def test_index(items):
    rq = requests.get(localhost())
    assert rq.json() == items


def test_query_item_by_id(items):
    rq = requests.get(localhost("/items/0"))
    assert rq.json() == items["items"]["0"]


def test_query_item_by_bad_id():
    rq = requests.get(localhost("/items/1001"))
    assert rq.json() == {"detail": "Item with 1001 does not exist."}


def test_query_item_by_parameter(items):
    rq = requests.get(localhost("/items?name=Nails"))
    expected = {"query": {"name": "Nails", "category": None},
                "selection": [items["items"]["2"]]}
    assert rq.json() == expected


@pytest.mark.skip()
def test_insert_item(items):
    data = {"name": "ScrewDriver", "price": 2.99, "count": 10, "id": 3, "category": "tools"}
    response = requests.post(localhost("/items"), json=data)
    new_items = requests.get(localhost()).json()["items"]
    assert response.json() == {"status": "ok"}
    assert new_items["3"] == data

