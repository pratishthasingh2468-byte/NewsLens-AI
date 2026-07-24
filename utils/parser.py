"""
parser.py

Utility functions for cleaning and preparing
news articles before processing.
"""

import re


def clean_text(text: str) -> str:
    """
    Clean and normalize the input news article.

    Steps:
    - Remove leading/trailing spaces
    - Replace tabs with spaces
    - Collapse multiple spaces
    - Collapse multiple blank lines

    Args:
        text (str): Raw news article.

    Returns:
        str: Cleaned news article.
    """

    if not text:
        return ""

    # Remove leading/trailing whitespace
    text = text.strip()

    # Replace tabs with spaces
    text = text.replace("\t", " ")

    # Replace multiple spaces with a single space
    text = re.sub(r"[ ]{2,}", " ", text)

    # Replace multiple blank lines with a single blank line
    text = re.sub(r"\n\s*\n+", "\n\n", text)

    return text


def word_count(text: str) -> int:
    """
    Count the number of words.

    Args:
        text (str): Input text.

    Returns:
        int: Total number of words.
    """

    if not text.strip():
        return 0

    return len(text.split())


def character_count(text: str) -> int:
    """
    Count the number of characters.

    Args:
        text (str): Input text.

    Returns:
        int: Total number of characters.
    """

    return len(text)
