#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    """
    Returns a set of all elements 
    present in only one set.

    Args:
    set_1(set): The first input set.
        set_2 (set): The second input set.

    Returns:
        set: A new set containing common elements.
        """
    
    return set_1.symmetric_difference(set_2)
