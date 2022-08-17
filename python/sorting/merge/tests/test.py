import pytest

from python.sorting.merge.merge_sort import merge_sort


# @pytest.mark.skip('Merge sort')
def test_merge_sort_initial():
    arr = [8, 4, 23, 42, 16, 15]
    actual = merge_sort(arr)
    expected = [4, 8, 15, 16, 23, 42]
    assert actual == expected


# @pytest.mark.skip('Merge sort')
def test_merge_sort_reversed():
    arr = [15, 16, 42, 23, 4, 8]
    actual = merge_sort(arr)
    expected = [4, 8, 15, 16, 23, 42]
    assert actual == expected


# @pytest.mark.skip('Merge sort')
def test_merge_sort_sorta_sorted():
    arr = [4, 8, 15, 16, 42, 23]
    actual = merge_sort(arr)
    expected = [4, 8, 15, 16, 23, 42]
    assert actual == expected


# @pytest.mark.skip('Merge sort')
def test_merge_sort_dupes():
    arr = [4, 8, 4, 16, 42, 23]
    actual = merge_sort(arr)
    expected = [4, 4, 8, 16, 23, 42]
    assert actual == expected

# expected failures

@pytest.mark.xfail
def test_merge_sort_empty_fail():
  arr = []
  actual = merge_sort(arr)
  expected = [2, 4, 8, 16, 23, 42]
  assert actual == expected

@pytest.mark.xfail
def test_merge_sort_fail():
  arr = [8, 4, 23, 42, 16, 15]
  actual = merge_sort(arr)
  expected = [8, 4, 15, 16, 23, 42]
  assert actual == expected