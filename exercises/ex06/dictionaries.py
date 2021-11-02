"""Practice with dictionaries."""

__author__ = "730383189"


def invert(test: dict[str, str]) -> dict[str, str]:
    """Makes keys values and values keys."""
    i = 0 
    j = 1 
    new_dict: dict[str, str] = dict()
    values: list[str] = list(test.values())
    keys: list[str] = list(test.keys())

    while j < len(values): 
        if values[i] == values[j]: 
            raise KeyError("Cannot have two keys of the same type") 
        if j == len(values) - 1: 
            i += 1
            j = i
        j += 1

    i = 0 
    while i < len(test):
        new_dict[values[i]] = keys[i]
        i = i + 1

    return new_dict


def favorite_color(NAMES_COLORS: dict[str, str]) -> str:
    """Finds which value in a dictionary is most common.""" 
    colors: list[str] = list(NAMES_COLORS.values())
    i = 1 
    j = 0
    k = 0 
    m = 0 
    common_color: str = ""
    while j < len(colors): 
        while i < len(colors): 
            if colors[i] == colors[j]: 
                k += 1 
            if k > m: 
                m = k 
                common_color = colors[j]
            i += 1 
        j += 1
        i = j + 1 
        k = 0 
    return common_color


def count(words: list[str]) -> dict[str, int]:
    """Counts the amount of times words in a list are used."""
    words_dict: dict[str, int] = dict()
    i = 0 
    for word in words: 
        if words[i] in words_dict: 
            words_dict[words[i]] += 1
        else: 
            words_dict[words[i]] = 1 
        i += 1
    return words_dict