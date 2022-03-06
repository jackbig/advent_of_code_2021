import src.input_bingo as IB
import src.matrix as MTX

def test_read_numbers() -> list:
    args = "1,2,3,4,5,6,7"
    values = IB.read_numbers(args)
    assert(len(values) == 7)
    assert(values[0] == 1)
    assert(values[6] == 7)

def test_read_card():
    lines = [
        "22 13 17 11  0",
        " 8  2 23  4 24",
        "21  9 14 16  7",
        " 6 10  3 18  5",   
        " 1 12 20 15 19",        
        "",
        " 3 15  0  2 22",
        " 9 18 13 17  5",
        "19  8  7 25 23",
        "20 11 10 24  4",
        "14 21 16 12  6"
        ]
    check0 = MTX.Matrix(4,5)
    check0.add_row([22,13,17,11,0])
    check0.add_row([8,2,23,4,24])
    check0.add_row([21,9,14,16,7])
    check0.add_row([6,10,3,18,5])
    check0.add_row([1,12,20,15,19])
    check1 = MTX.Matrix(4,5)
    check1.add_row([3,15,0,2,22])
    check1.add_row([9,18,13,17,5])
    check1.add_row([19,8,7,25,23])
    check1.add_row([20,11,10,24,4])
    check1.add_row([14,21,16,12,6])
    matrices = IB.read_cards(lines)
    assert(len(matrices) == 2)
    assert(matrices[0] == check0)
    assert(matrices[1] == check1)
    




