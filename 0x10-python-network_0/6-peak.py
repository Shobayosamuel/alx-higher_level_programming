#!/usr/bin/python3
"""find the peak of an unsorted array"""


def find_peak(list_of_integers):
    """
        Return the peak of the array
    """
    if not list_of_integers:
        return None
    lists = list_of_integers
    size = len(lists)
    if size == 1:
        return lists[0]
    elif size == 2:
        return max(lists)
    mid = int(size / 2)
    peak = lists[mid]
    if peak > lists[mid - 1] and peak > lists[mid + 1]:
        return peak
    elif peak < lists[mid - 1]:
        return find_peak(lists[:mid])
    else:
        return find_peak(lists[mid + 1:])
