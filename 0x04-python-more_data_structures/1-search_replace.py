#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """
    Replaces all occurrences of 'search' with 'replace' in a new list.

    Args:
        my_list: The initial list.
        search: The element to replace in the list.
        replace: The new element.

    Returns:
        list: A new list with replaced elements.
    """
    new_list = []

    for i in my_list:
        if i == search:
            new_list.append(replace)
        else:
            new_list.append(i)
    
    return new_list
