from typing import Type, Union, get_origin, get_args
from pathlib import Path
import os
from pyenvmap.parser import load_dotenv

def is_optional_type(t: Type) -> bool:
    """Check if a type is Optional[X], i.e., Union[X, NoneType]."""
    return get_origin(t) is Union and type(None) in get_args(t)


def auto_load_dotenv(dotenv_path: Union[str, Path] = ".env") -> None:
    """Automatically load a .env file if it exists.

    Intended as a convenience hook for projects using pyenvmap.
    """
    path = Path(dotenv_path)
    if path.exists():
        load_dotenv(path)


def debug_env_snapshot(keys: list[str]) -> dict[str, str]:
    """Return a snapshot of current environment values for debugging.

    Useful in tests or logging.
    """
    return {key: os.getenv(key, "<not set>") for key in keys}
