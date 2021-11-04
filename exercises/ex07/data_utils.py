"""Utility functions."""

__author__ = "730383189"

# Define your functions below
from csv import DictReader


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


def select(table: dict[str, list[str]], desired_columns: list[str]) -> dict[str, list[str]]:
    """Select what columns you want to display."""
    result: dict[str, list[str]] = {}

    for column in desired_columns: 
        result[column] = table[column] 

    return result  


def concat(table: dict[str, list[str]], additional_table: dict[str, list[str]]) -> dict[str, list[str]]: 
    """Combines two tables."""
    result: dict[str, list[str]] = {}

    for column in table: 
        result[column] = table[column] 
    
    for column in additional_table: 
        if column in result:
            i = 0 
            while i < len(additional_table[column]):
                result[column].append(additional_table[column][i]) 
                i += 1
        else: 
            result[column] = additional_table[column]

    return result 


def count(interest_points: list[str]) -> dict[str, int]: 
    """Counts the number of occurances in a list."""
    result: dict[str, int] = {}

    for column in interest_points: 
        if column in result: 
            result[column] += 1

        else: 
            result[column] = 1 

    return result 