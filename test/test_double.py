import pytest, requests
from requests_toolbelt import sessions
import pytest

@pytest.fixture
def session():
	return sessions.BaseUrlSession(base_url = 'http://127.0.0.1:8080')

def test_double2(session):
    response = session.get('/double', params = dict(number = 2))
    assert response.json()['double'] == 4

def test_double3(session):
    response = session.get('/double', params = dict(number = 3))
    assert response.json()['double'] == 6
