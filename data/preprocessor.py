import re


def remove_diacritics(text):
    """
    Removes Arabic diacritics to reduce the complexity of the text.

    Parameters:
        text (str): The Arabic text from which diacritics will be removed.

    Returns:
        str: The text with diacritics removed.
    """
    return re.sub(r'[\u064B-\u065F]', '', text)


def normalize_arabic(text):
    """
    Normalizes Arabic text by standardizing variations of similar characters.

    Parameters:
        text (str): The Arabic text to be normalized.

    Returns:
        str: The normalized Arabic text.
    """
    text_cleaned = re.sub(r'[يى]', 'ي', text)
    text_cleaned = re.sub(r'ة', 'ه', text_cleaned)
    text_cleaned = re.sub(r'[أإآ]', 'ا', text_cleaned)
    text_cleaned = re.sub(r'ک', 'ك', text_cleaned)

    return text_cleaned
