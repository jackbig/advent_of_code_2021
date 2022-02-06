import src.bingo as bingo
from src.matrix import Matrix

def test_find_commons():
    mtx = Matrix(4,3)
    mtx.add_row([1,2,3])
    mtx.add_row([4,5,6])
    mtx.add_row([7,8,9])
    mtx.add_row([10,11,12])
    input = [6,5,2,12]
    commons = bingo.find_commons(input, mtx.row(0))
    assert(commons == [2])
    commons = bingo.find_commons(input, mtx.row(1))
    assert(commons == [6,5])
    commons = bingo.find_commons(input, mtx.row(2))
    assert(commons == [])
    commons = bingo.find_commons(input, mtx.row(3))
    assert(commons == [12])

def test_bingo():
    mtx = Matrix(4,3)
    mtx.add_row([1,2,3])
    mtx.add_row([4,5,6])
    mtx.add_row([7,8,9])
    mtx.add_row([10,11,12])
    assert(bingo.bingo([6,5,2,12], mtx) == None)
    assert(bingo.bingo([3,6,9,46,12], mtx) == 12)
    assert(bingo.bingo([7,28,8,27,9], mtx) == 9)
    assert(bingo.bingo([1,3], mtx) == None)
    assert(bingo.bingo([4,7,10], mtx) == None)

def test_unmarked():
    mtx = Matrix(4,3)
    mtx.add_row([1,2,3])
    mtx.add_row([4,5,6])
    mtx.add_row([7,8,9])
    mtx.add_row([10,11,12])
    assert(bingo.unmarked([6,5,2,12,9], mtx) == [1,3,4,7,8,10,11])
    assert(bingo.unmarked([1,3,4,7,8,10,11], mtx) == [2,5,6,9,12])
    assert(bingo.unmarked([], mtx) == [1,2,3,4,5,6,7,8,9,10,11,12])

def test_score():
    mtx = Matrix(4,3)
    mtx.add_row([1,2,3])
    mtx.add_row([4,5,6])
    mtx.add_row([7,8,9])
    mtx.add_row([10,11,12])
    assert(bingo.score([7,8,9], mtx) == (1+2+3+4+5+6+10+11+12)*9)
    assert(bingo.score([2,5,8,11], mtx) == (1+3+4+6+7+9+10+12)*11)
    assert(bingo.score([7,8,9,2,5,11], mtx) == (1+3+4+6+10+12)*9)
    assert(bingo.score([7,11,2,8,5,9], mtx) == (1+3+4+6+10+12)*5)
    assert(bingo.score([7,411,2,8,55,9], mtx) == (1+3+4+5+6+10+11+12)*9)
    assert(bingo.score([2,505,8,11], mtx) == 0)