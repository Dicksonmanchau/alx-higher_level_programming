#!/usr/bin/python3

def common_elements(set_1, set_2):
    """
    Returns a set of common 
    elements in two sets

    Args:
        set_1: The first input set
        set_2: The second input set

    Returns:
        set:A new set 
        containing new common elements.
    """

    c_set = set()

    for element in set_1:
        if element in set_2:
            c_set.add(element)

    return c_set
