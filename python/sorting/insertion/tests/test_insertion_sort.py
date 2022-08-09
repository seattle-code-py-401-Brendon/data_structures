import pytest

from python.sorting.insertion.insertion_sort import insertion_sort


# @pytest.mark.skip('Insertion sort')
def test_insertion_sort_initial():
    arr = [8, 4, 23, 42, 16, 15]
    actual = insertion_sort(arr)
    expected = [4, 8, 15, 16, 23, 42]
    assert actual == expected


# @pytest.mark.skip('Insertion sort')
def test_insertion_sort_reversed():
    arr = [15, 16, 42, 23, 4, 8]
    actual = insertion_sort(arr)
    expected = [4, 8, 15, 16, 23, 42]
    assert actual == expected


# @pytest.mark.skip('Insertion sort')
def test_insertion_sort_sorta_sorted():
    arr = [4, 8, 15, 16, 42, 23]
    actual = insertion_sort(arr)
    expected = [4, 8, 15, 16, 23, 42]
    assert actual == expected


# @pytest.mark.skip('Insertion sort')
def test_insertion_sort_dupes():
    arr = [4, 8, 4, 16, 42, 23]
    actual = insertion_sort(arr)
    expected = [4, 4, 8, 16, 23, 42]
    assert actual == expected
