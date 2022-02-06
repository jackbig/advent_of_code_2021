import src.matrix as mtx

def test_init():
    m = mtx.Matrix(4,3)
    assert(m.rows() == 4)
    assert(m.columns() == 3)

def test_row():
    m = mtx.Matrix(4,3)
    m.add_row([1,2,3])
    m.add_row([4,5,6])
    m.add_row([7,8,9])
    m.add_row([10,11,12])
    assert(m.column(0) == [1,4,7, 10])
    assert(m.column(1) == [2,5,8,11])
    assert(m.column(2) == [3,6,9,12])

def test_column():
    m = mtx.Matrix(4,3)
    m.add_row([1,2,3])
    m.add_row([4,5,6])
    m.add_row([7,8,9])
    m.add_row([10,11,12])
    assert(m.row(0) == [1,2,3])
    assert(m.row(1) == [4,5,6])
    assert(m.row(2) == [7,8,9])
    assert(m.row(3) == [10,11,12])