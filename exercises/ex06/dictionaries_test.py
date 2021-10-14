"""Unit tests for dictionary functions."""

from exercises.ex06.dictionaries import invert, favorite_colors, count
import pytest
__author__ = "730383189"


def test_invert_KeyError() -> None:
    """Tests if invert raises KeyError."""
    with pytest.raises(KeyError): 
        my_dictionary = {'kris': 'jordan', 'michael': 'jordan'}
        invert(my_dictionary)


def test_invert_my_birthday() -> None: 
    """Tests if invert works with my birhday."""
    assert invert({"12": "21"}) is None


def test_invert_empty() -> None: 
    """Tests if invert works while empty."""
    assert invert({}) is None


def test_favorite_colors_study_group() -> None: 
    """Tests if favorite colors works with my study group."""
    NAMES_COLORS: dict[str, str] = {"Parker": "Purple", "Vivian": "Periwinkle", "Luis": "Purple"}
    assert favorite_colors(NAMES_COLORS) == 'Purple'


def test_favorite_colors_family() -> None: 
    """Tests if favorite colors works with my family."""
    NAMES_COLORS: dict[str, str] = {"Dad": "Green", "Mom": "Red", "Me": "Purple", "Sister": "Red"}
    assert favorite_colors(NAMES_COLORS) == 'Red'


def test_favorite_colors_empty() -> None:
    """Tests if favorite colors works empty."""
    NAMES_COLORS: dict[str, str] = {}
    assert favorite_colors(NAMES_COLORS) == ''


def test_count_sun_tzu() -> None:
    """Tests if count works on sun tzu."""
    words: list[str] = ["All", "Warfare", "Is", "Based", "On", "Deception"]
    assert count(words) == {"All": 1, "Warfare": 1, "Is": 1, "Based": 1, "On": 1, "Deception": 1}


def test_count_shakesphere() -> None:
    """Tests if count works on shakesphere."""
    words: list[str] = ["To", "Be", "Or", "Not", "To", "Be"]
    assert count(words) == {"To": 2, "Be": 2, "Or": 1, "Not": 1}


def test_count_empty() -> None:
    """Tests if count works empty."""
    words: list[str] = []
    assert count(words) == {}