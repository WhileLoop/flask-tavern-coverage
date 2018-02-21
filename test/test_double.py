import requests

def test_double():
    response = requests.get('http://127.0.0.1:8080/double', params = dict(number = 2))
    assert response.json()['double'] == 4
