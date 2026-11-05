import pytest

BASE_URL = "http://127.0.0.1:8000/delivery.html"

@pytest.fixture
def delivery_url():
    return BASE_URL
