import pytest
from grid import Grid

def test_case_1():
    grid = [[1,1,1], [0,0,0], [0,0,0]]
    assert Grid.check_win(grid) == 1

    grid = [[2,2,2], [0,0,0], [0,0,0]]
    assert Grid.check_win(grid) == 2

def test_case_2():
    grid = [[0,0,0], [1,1,1], [0,0,0]]
    assert Grid.check_win(grid) == 1

    grid = [[0,0,0], [2,2,2], [0,0,0]]
    assert Grid.check_win(grid) == 2

def test_case_3():
    grid = [[0,0,0], [0,0,0], [1,1,1]]
    assert Grid.check_win(grid) == 1

    grid = [[0,0,0], [0,0,0], [2,2,2]]
    assert Grid.check_win(grid) == 2

def test_case_4():
    grid = [[1,0,0], [1,0,0], [1,0,0]]
    assert Grid.check_win(grid) == 1

    grid = [[2,0,0], [2,0,0], [2,0,0]]
    assert Grid.check_win(grid) == 2

def test_case_5():
    grid = [[0,1,0], [0,1,0], [0,1,0]]
    assert Grid.check_win(grid) == 1

    grid = [[0,2,0], [0,2,0], [0,2,0]]
    assert Grid.check_win(grid) == 2

def test_case_6():
    grid = [[0,0,1], [0,0,1], [0,0,1]]
    assert Grid.check_win(grid) == 1

    grid = [[0,0,2], [0,0,2], [0,0,2]]
    assert Grid.check_win(grid) == 2

def test_case_7():
    grid = [[1,0,0], [0,1,0], [0,0,1]]
    assert Grid.check_win(grid) == 1

    grid = [[2,0,0], [0,2,0], [0,0,2]]
    assert Grid.check_win(grid) == 2

def test_case_8():
    grid = [[0,0,1], [0,1,0], [1,0,0]]
    assert Grid.check_win(grid) == 1

    grid = [[0,0,2], [0,2,0], [2,0,0]]
    assert Grid.check_win(grid) == 2

def test_case_9():
    grid = [[1,2,1], [2,2,1], [1,1,2]]
    assert Grid.check_win(grid) == -1
