#!/usr/bin/env python3
""" Complex types - list of floats """
from typing import Callable, Iterator, Union, Optional, List

def sum_list(input_list : list[float]) -> float:
    """ Returns sum of list of floats """
    return sum(input_list)