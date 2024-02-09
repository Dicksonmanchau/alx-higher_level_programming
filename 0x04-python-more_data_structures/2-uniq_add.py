#!/usr/bin/python3

def uniq_add(my_list=[]):
    """
    Adds all unique integers in the list (only once for each integer).

    Args:
        my_list (list): The input list.

    Returns:
        int: The sum of unique integers.
    """
    new_list = []
    sum = 0

    for num in my_list:
        if num not in new_list:
            sum += num
            new_list.append(num)

    return sum
