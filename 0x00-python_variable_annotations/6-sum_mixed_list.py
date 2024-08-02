#!/usr/bin/env python3

""" Mixed list """
from typing import Union, List

def sum_mixed_list(mxd_lst: List[Union[int,float]]) -> float:
    """ Returns the sum of a list of floats and integers """
    return sum(mxd_lst)