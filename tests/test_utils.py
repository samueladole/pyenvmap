import os
from typing import Optional
import pytest
from pyenvmap.utils import (
    is_optional_type,
    auto_load_dotenv,
    debug_env_snapshot
)


@pytest.fixture
def dotenv_file(tmp_path):
    """Fixture to create a temporary .env file for testing."""
    env_file = tmp_path / ".env"
    env_file.write_text("""
    DEBUG=true
    PORT=8080
    SECRET_KEY="supersecret"
    """)
    return env_file


def test_is_optional_type():
    """Test the utility function to check for Optional types."""
    assert is_optional_type(Optional[int]) is True
    assert is_optional_type(Optional[str]) is True
    assert is_optional_type(int) is False
    assert is_optional_type(str) is False
    assert is_optional_type(Optional[Optional[str]]) is True


def test_auto_load_dotenv(dotenv_file):
    """Test auto loading of .env file into os.environ."""
    # Before loading
    assert "DEBUG" not in os.environ
    assert "PORT" not in os.environ

    auto_load_dotenv(dotenv_file)

    # After loading
    assert os.getenv("DEBUG") == "true"
    assert os.getenv("PORT") == "8080"
    assert os.getenv("SECRET_KEY") == "supersecret"


def test_debug_env_snapshot():
    """Test the function that returns a snapshot of environment variables."""
    # Set some environment variables for testing
    set_env(DEBUG="true", PORT="8080")

    snapshot = debug_env_snapshot(["DEBUG", "PORT", "NON_EXISTENT_VAR"])

    assert snapshot["DEBUG"] == "true"
    assert snapshot["PORT"] == "8080"
    assert snapshot["NON_EXISTENT_VAR"] == "<not set>"

    # Clear the environment variables
    clear_env("DEBUG", "PORT")


# Helper functions for setting and clearing environment variables

def set_env(**kwargs):
    """Helper to temporarily set environment variables."""
    for key, value in kwargs.items():
        os.environ[key] = str(value)


def clear_env(*keys):
    """Helper to remove environment variables."""
    for key in keys:
        os.environ.pop(key, None)
