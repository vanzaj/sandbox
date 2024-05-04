from fastapi.testclient import TestClient
from api.bank_note import app

client = TestClient(app)

def test_index():
    response = client.get('/')
    assert response.json() == {'message': 'Hello World'}


def test_hello():
    response = client.get('/hello/Alice')
    assert response.json() == {'message': 'Hello Alice'}


def test_model_info():
    response = client.get('/model/info')
    expected = {"model": {"name": "RandomForestClassifier", "accuracy": 0.9951456310679612}}
    assert response.json() == expected


def test_model_predict():
    data = {'variance': 0, 'skewness': 0, 'curtosis': 0, 'entropy': 0}
    response = client.post('/model/predict', json=data)
    assert response.json() == {'prediction': 'Fake Bank note'}


def test_model_predict_invalid_data():
    data = {'skewness': 0, 'curtosis': 0, 'entropy': 0}
    response = client.post('/model/predict', json=data)
    assert response.json() == {'prediction': 'Fake Bank note'}