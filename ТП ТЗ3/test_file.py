import pytest
import time
from datetime import datetime
import sys
from programm_file import min_number, max_number, multiplication, total_sum, average
from functools import reduce


list_of_int = [
    [4, 5, 7],
    [76, 82, 56, 102],
    [1, 2, 3, 4, 5, 6]
]


def test_min_number():
    print()
    for s in list_of_int:
        start_time = datetime.now()
        assert min_number(list_of_int) == min(list_of_int)
        print(sys.getsizeof(s), 'bytes  ', datetime.now() - start_time)


def test_max_number():
    print()
    for s in list_of_int:
        start_time = datetime.now()
        assert max_number(list_of_int) == max(list_of_int)
        print(sys.getsizeof(s), 'bytes  ', datetime.now() - start_time)


def test_multiplication():
    print()
    for s in list_of_int:
        start_time = datetime.now()
        assert multiplication(s) == reduce(lambda x, y: x*y, s)
        print(sys.getsizeof(s), 'bytes  ', datetime.now() - start_time)


def test_total_sum():
    print()
    for s in list_of_int:
        start_time = datetime.now()
        assert total_sum(s) == sum(s)
        print(sys.getsizeof(s), 'bytes  ', datetime.now() - start_time)


def test_average():
    print()
    for s in list_of_int:
        start_time = datetime.now()
        assert average(s) == (sum(s)/len(s))
        print(sys.getsizeof(s), 'bytes  ', datetime.now() - start_time)
