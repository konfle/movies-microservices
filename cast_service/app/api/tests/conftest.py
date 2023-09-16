import pytest

from fastapi.testclient import TestClient

from app.main import app
from app.api import db_manager as dbm


@pytest.fixture(scope="module")
def test_app():
    """
    Pytest fixture providing a TestClient for the FastAPI app.

    This fixture sets up a TestClient for the FastAPI app to simulate HTTP requests
    during testing. It configures the client to use the specified base URL for API
    endpoints under '/api/v1/casts/'.

    Usage:
    ```
    def test_example(test_app):
        response = test_app.get("/some_endpoint")
        assert response.status_code == 200
    ```

    Returns:
        TestClient: A TestClient instance for making HTTP requests to the app.
    """
    with TestClient(app, base_url=f"http://localhost:8080/api/v1/casts/") as client:
        yield client


@pytest.fixture
def mock_add_cast(monkeypatch):
    """
    Fixture to mock the 'db_manager.add_cast' function.

    This fixture replaces the actual 'db_manager.add_cast' function with a mock
    implementation to isolate the tests from the database.

    Args:
        monkeypatch: Pytest fixture for patching modules and objects during testing.
    """
    async def mock_add_cast(payload):
        return 1
    monkeypatch.setattr(dbm, "add_cast", mock_add_cast)
