import pytest
from your_module import combinations

def test_combinations():
    assert combinations([1, 2, 3], 2) == [[1, 2], [1, 3], [2, 3]]

def test_combinations_empty():
    assert combinations([], 2) == []

def test_combinations_k_larger_than_n():
    assert combinations([1, 2, 3], 4) == []

def test_combinations_k_equal_to_n():
    assert combinations([1, 2, 3], 3) == [[1, 2, 3]]

def test_combinations_k_equal_to_1():
    assert combinations([1, 2, 3], 1) == [[1], [2], [3]]

def test_combinations_k_equal_to_0():
    assert combinations([1, 2, 3], 0) == [[]]
