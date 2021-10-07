"""Unit tests for list utility functions."""

from exercises.ex05.utils import only_evens, sub, concat

__author__ = "730383189"


def test_only_evens_empty() -> None:
    """Tests if only_evens works empty."""
    a: list[int] = []
    assert only_evens(a) == [] 


def test_only_evens_1_through_5() -> None:
    """Tests if only_evens works with numbers 1-5."""
    a: list[int] = [1, 2, 3, 4, 5]
    assert only_evens(a) == [2, 4] 


def test_only_evens_my_birthday() -> None:
    """Tests if only_evens works at my birthday."""
    a: list[int] = [12, 21, 2001]
    assert only_evens(a) == [12] 


def test_sub_empty() -> None:
    """Tests if sub works empty."""
    a: list[int] = []
    b: int = 1
    c: int = 2
    assert sub(a, b, c) == [] 


def test_sub_1_through_5() -> None:
    """Tests if sub works with numbers 1-5."""
    a: list[int] = [1, 2, 3, 4, 5]
    b: int = 1
    c: int = 3
    assert sub(a, b, c) == [2, 3] 


def test_sub_my_birthday() -> None:
    """Tests if sub works at my birthday."""
    a: list[int] = [12, 21, 2001]
    b: int = 1
    c: int = 2
    assert sub(a, b, c) == [21] 


def test_concat_empty() -> None:
    """Tests if concat works empty."""
    a: list[int] = []
    b: list[int] = []
    assert concat(a, b) == [] 


def test_concat_1_through_5() -> None:
    """Tests if concat works with numbers 1-5."""
    a: list[int] = [1, 2, 3, 4, 5]
    b: list[int] = [1, 2, 3, 4, 5]
    assert concat(a, b) == [1, 2, 3, 4, 5, 1, 2, 3, 4, 5] 


def test_concat_my_birthday() -> None:
    """Tests if concat works at my birthday."""
    a: list[int] = [12, 21, 2001]
    b: list[int] = [12, 21, 2001]
    assert concat(a, b) == [12, 21, 2001, 12, 21, 2001] 