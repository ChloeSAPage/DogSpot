import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Home" in response.data  # Assuming your home page contains the word "Home"

def test_explore(client):
    response = client.get('/explore')
    assert response.status_code == 200
    assert b"Explore" in response.data  # Assuming your explore page contains the word "Explore"

def test_contact(client):
    response = client.get('/contact')
    assert response.status_code == 200
    assert b"Contact" in response.data  # Assuming your contact page contains the word "Contact"

def test_signin(client):
    response = client.get('/signin')
    assert response.status_code == 200
    assert b"Sign in" in response.data  # Assuming your sign-in page contains the words "Sign in"
