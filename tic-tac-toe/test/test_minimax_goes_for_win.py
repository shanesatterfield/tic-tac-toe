import pytest
from ai import *
from grid import Grid

def test_case_1_horizontal():
    ai = Minimax()
    grid = [[1,1,0],[0,0,0],[0,0,0]]
    print(ai.make_move(grid, True))
    assert ai.make_move(grid, True)  == (0,2)

    grid = [[2,2,0],[0,0,0],[0,0,0]]
    assert ai.make_move(grid, False) == (0,2)


    grid = [[1,0,1],[0,0,0],[0,0,0]]
    assert ai.make_move(grid, True)  == (0,1)

    grid = [[2,0,2],[0,0,0],[0,0,0]]
    assert ai.make_move(grid, False) == (0,1)


    grid = [[0,1,1],[0,0,0],[0,0,0]]
    assert ai.make_move(grid, True)  == (0,0)

    grid = [[0,2,2],[0,0,0],[0,0,0]]
    assert ai.make_move(grid, False) == (0,0)


def test_case_2_horizontal():
    ai = Minimax()
    grid = [[0,0,0],[1,1,0],[0,0,0]]
    assert ai.make_move(grid, True)  == (1,2)

    grid = [[0,0,0],[2,2,0],[0,0,0]]
    assert ai.make_move(grid, False) == (1,2)


    grid = [[0,0,0],[1,0,1],[0,0,0]]
    assert ai.make_move(grid, True)  == (1,1)

    grid = [[0,0,0],[2,0,2],[0,0,0]]
    assert ai.make_move(grid, False) == (1,1)


    grid = [[0,0,0],[0,1,1],[0,0,0]]
    assert ai.make_move(grid, True)  == (1,0)

    grid = [[0,0,0],[0,2,2],[0,0,0]]
    assert ai.make_move(grid, False) == (1,0)

def test_case_3_horizontal():
    ai = Minimax()
    grid = [[0,0,0],[0,0,0],[1,1,0]]
    assert ai.make_move(grid, True)  == (2,2)

    grid = [[0,0,0],[0,0,0],[2,2,0]]
    assert ai.make_move(grid, False) == (2,2)


    grid = [[0,0,0],[0,0,0],[1,0,1]]
    assert ai.make_move(grid, True)  == (2,1)

    grid = [[0,0,0],[0,0,0],[2,0,2]]
    assert ai.make_move(grid, False) == (2,1)


    grid = [[0,0,0],[0,0,0],[0,1,1]]
    assert ai.make_move(grid, True)  == (2,0)

    grid = [[0,0,0],[0,0,0],[0,2,2]]
    assert ai.make_move(grid, False) == (2,0)


def test_case_1_vertical():
    ai = Minimax()
    grid = [[1,0,0],[1,0,0],[0,0,0]]
    assert ai.make_move(grid, True)  == (2,0)

    grid = [[2,0,0],[2,0,0],[0,0,0]]
    assert ai.make_move(grid, False) == (2,0)


    grid = [[1,0,0],[0,0,0],[1,0,0]]
    assert ai.make_move(grid, True)  == (1,0)

    grid = [[2,0,0],[0,0,0],[2,0,0]]
    assert ai.make_move(grid, False) == (1,0)


    grid = [[0,0,0],[1,0,0],[1,0,0]]
    assert ai.make_move(grid, True)  == (0,0)

    grid = [[0,0,0],[2,0,0],[2,0,0]]
    assert ai.make_move(grid, False) == (0,0)


def test_case_2_vertical():
    ai = Minimax()
    grid = [[0,1,0],[0,1,0],[0,0,0]]
    assert ai.make_move(grid, True)  == (2,1)

    grid = [[0,2,0],[0,2,0],[0,0,0]]
    assert ai.make_move(grid, False) == (2,1)


    grid = [[0,1,0],[0,0,0],[0,1,0]]
    assert ai.make_move(grid, True)  == (1,1)

    grid = [[0,2,0],[0,0,0],[0,2,0]]
    assert ai.make_move(grid, False) == (1,1)


    grid = [[0,0,0],[0,1,0],[0,1,0]]
    assert ai.make_move(grid, True)  == (0,1)

    grid = [[0,0,0],[0,2,0],[0,2,0]]
    assert ai.make_move(grid, False) == (0,1)


def test_case_3_vertical():
    ai = Minimax()
    grid = [[0,0,1],[0,0,1],[0,0,0]]
    assert ai.make_move(grid, True)  == (2,2)

    grid = [[0,0,2],[0,0,2],[0,0,0]]
    assert ai.make_move(grid, False) == (2,2)


    grid = [[0,0,1],[0,0,0],[0,0,1]]
    assert ai.make_move(grid, True)  == (1,2)

    grid = [[0,0,2],[0,0,0],[0,0,2]]
    assert ai.make_move(grid, False) == (1,2)


    grid = [[0,0,0],[0,0,1],[0,0,1]]
    assert ai.make_move(grid, True)  == (0,2)

    grid = [[0,0,0],[0,0,2],[0,0,2]]
    assert ai.make_move(grid, False) == (0,2)


def test_case_1_diagonal():
    ai = Minimax()
    grid = [[1,0,0],[0,1,0],[0,0,0]]
    assert ai.make_move(grid, True)  == (2,2)

    grid = [[2,0,0],[0,2,0],[0,0,0]]
    assert ai.make_move(grid, False) == (2,2)


    grid = [[1,0,0],[0,0,0],[0,0,1]]
    assert ai.make_move(grid, True)  == (1,1)

    grid = [[2,0,0],[0,0,0],[0,0,2]]
    assert ai.make_move(grid, False) == (1,1)


    grid = [[0,0,0],[0,1,0],[0,0,1]]
    assert ai.make_move(grid, True)  == (0,0)

    grid = [[0,0,0],[0,2,0],[0,0,2]]
    assert ai.make_move(grid, False) == (0,0)


def test_case_2_diagonal():
    ai = Minimax()
    grid = [[0,0,1],[0,1,0],[0,0,0]]
    assert ai.make_move(grid, True)  == (2,0)

    grid = [[0,0,2],[0,2,0],[0,0,0]]
    assert ai.make_move(grid, False) == (2,0)


    grid = [[0,0,1],[0,0,0],[1,0,0]]
    assert ai.make_move(grid, True)  == (1,1)

    grid = [[0,0,2],[0,0,0],[2,0,0]]
    assert ai.make_move(grid, False) == (1,1)


    grid = [[0,0,0],[0,1,0],[1,0,0]]
    assert ai.make_move(grid, True)  == (0,2)

    grid = [[0,0,0],[0,2,0],[2,0,0]]
    assert ai.make_move(grid, False) == (0,2)
