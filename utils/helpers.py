"""
helpers.py

Common helper functions used throughout
the News Summarizer Agent project.
"""

from pathlib import Path
from datetime import datetime


def read_text_file(file_path: str) -> str:
    """
    Read a text file and return its contents.

    Args:
        file_path (str): Path to the text file.

    Returns:
        str: File contents.
    """

    path = Path(file_path)

    if not path.exists():
        return ""

    try:
        return path.read_text(encoding="utf-8")
    except Exception:
        return ""


def save_text_file(file_path: str, content: str) -> None:
    """
    Save text to a file.

    Args:
        file_path (str): Destination path.
        content (str): Text to save.
    """

    path = Path(file_path)

    # Create parent directories if needed
    path.parent.mkdir(parents=True, exist_ok=True)

    with open(path, "w", encoding="utf-8") as file:
        file.write(content)


def get_timestamp() -> str:
    """
    Return the current timestamp.

    Returns:
        str: Current date and time.
    """

    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def file_exists(file_path: str) -> bool:
    """
    Check whether a file exists.

    Args:
        file_path (str): Path to the file.

    Returns:
        bool
    """

    return Path(file_path).exists()


def list_news_files(news_folder: str = "data/news_docs") -> list:
    """
    Return all .txt files from the news folder.

    Args:
        news_folder (str): Folder containing news files.

    Returns:
        list: List of Path objects.
    """

    folder = Path(news_folder)

    if not folder.exists():
        return []

    return list(folder.glob("*.txt"))
