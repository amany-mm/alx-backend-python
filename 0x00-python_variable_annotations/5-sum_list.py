#!/usr/bin/env python3
"""Module that contains function to sum floats in a list"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Function that sums floats in a list"""

    result = 0
    for num in input_list:
        result += num
    return result
