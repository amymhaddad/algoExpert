from smallest_diff import smallest


def test_ex_input():
    arr1 = [-1, 5, 10, 20, 28, 3]
    arr2 = [26, 134, 135, 15, 17]
    assert smallest(arr1, arr2) == [28, 26]


def test_uneven_arrays():
    arr1 = [10, 0, 20, 25]
    arr2 = [1005, 1006, 1014, 1032, 1031]
    assert smallest(arr1, arr2) == [25, 1005]


def test_short_arrays():
    arr1 = [0, 20]
    arr2 = [21, -2]
    assert smallest(arr1, arr2) == [20, 21]
