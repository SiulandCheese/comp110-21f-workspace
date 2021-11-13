"""Some useful functions I want to implement in my analysis."""

__author__ = "730383189" 

from csv import DictReader


def count(interest_points: list[str]) -> dict[str, int]: 
    """Counts the number of occurances in a list."""
    result: dict[str, int] = {}

    for column in interest_points: 
        if column in result: 
            result[column] += 1

        else: 
            result[column] = 1 

    return result 


def head(table: dict[str, list[str]], N: int) -> dict[str, list[str]]:
    """Make a limited column-based table."""
    result: dict[str, list[str]] = {}
    
    for key in table: 
        i = 0 
        values_under_n: list[str] = []

        while i < len(table) and i != N: 
            values_under_n.append(table[key][i]) 
            i += 1 
        
        result[key] = values_under_n
    return result 


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of CSV into a 'table'."""
    result: list[dict[str, str]] = []

    file_handle = open(filename, "r", encoding="utf8")

    cvs_reader = DictReader(file_handle)

    for row in cvs_reader: 
        result.append(row)

    file_handle.close
    
    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]: 
    """Produce a list[str] of all values in a single column."""
    result: list[str] = [] 

    for row in table:
        item: str = row[column] 
        result.append(item)

    return result 


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]: 
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}
    
    first_row: dict[str, str] = row_table[0]
    for column in first_row: 
        result[column] = column_values(row_table, column)

    return result 


def select(table: dict[str, list[str]], desired_columns: list[str]) -> dict[str, list[str]]:
    """Select what columns you want to display."""
    result: dict[str, list[str]] = {}

    for column in desired_columns: 
        result[column] = table[column] 

    return result  


def google_translate(untranslated_table: dict[str, list[str]]) -> dict[str, list[int]]: 
    """Takes strings in a list within a dictionary and makes them integers."""
    translated_table: dict[str, list[int]] = {}
    
    for key in untranslated_table: 
        translated_table[key] = []
        for value in untranslated_table[key]: 
            current_value: int
            if value == "None to less than one month!": 
                current_value = 1
            elif value == "2-6 months":
                current_value = 2
            elif value == "7-12 months": 
                current_value = 3 
            elif value == "1-2 years": 
                current_value = 4 
            elif value == "Over 2 years": 
                current_value = 5
            elif value == "1": 
                current_value = 1
            elif value == "2": 
                current_value = 2
            elif value == "3": 
                current_value = 3
            elif value == "4": 
                current_value = 4
            elif value == "5": 
                current_value = 5
            elif value == "6": 
                current_value = 6
            elif value == "7": 
                current_value = 7
            translated_table[key].append(int(current_value))
                
    return translated_table


def bojack(data_int: dict[str, list[int]]) -> dict[int, float]: 
    """Transforms a dict of strings and lists of integers into a dictionary of integers and floats."""
    result: dict[int, float] = {} 
    placeholder: list[int] = []
    i = 0 
    a = 0 
    b = 0 
    c = 0 
    d = 0 
    e = 0 
    for value in data_int["difficulty"]: 
        placeholder.append(data_int["difficulty"][value])

    result[1] = 0
    result[2] = 0
    result[3] = 0
    result[4] = 0
    result[5] = 0
    for value in data_int["prior_exp"]:
        result[value] += placeholder[i]
        i += 1 
        if value == 1: 
            a += 1 
        elif value == 2: 
            b += 1 
        elif value == 3: 
            c += 1 
        elif value == 4: 
            d += 1 
        elif value == 5: 
            e += 1 
    
    for value in result: 
        if value == 1: 
            result[1] = result[1] / a
        elif value == 2: 
            result[2] = result[2] / b
        elif value == 3: 
            result[3] = result[3] / c
        elif value == 4: 
            result[4] = result[4] / d
        elif value == 5: 
            result[5] = result[5] / e

    return result 