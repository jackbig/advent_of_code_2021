import bingo
import input_bingo as BI
import matrix as MTX
import sys
import utilities.input as inpututils

def main():
    numbers_file = sys.argv[1]
    cards_file = sys.argv[2]
    lines = inpututils.read_input(numbers_file)
    assert(len(lines) == 1)
    numbers = BI.read_numbers(lines[0])
    lines = inpututils.read_input(cards_file)
    matrices = BI.read_cards(lines)
    #for mtx in matrices:
    #    print(MTX.printMatrix(mtx))
    scores = []
    for i in range(0, len(numbers)):
        if i > 0:
            test = numbers[i]
        to_remove = []
        for mtx in matrices:
            value = bingo.bingo(numbers[:i], mtx)
            if value is not None:
                score = bingo.score(numbers[:i], mtx)
                print("BINGO!!!")
                print("SCORE: " + str(score))
                scores.append(score)
                to_remove.append(mtx)
        for item in to_remove:
            matrices.remove(item)
        to_remove.clear()            
    print("LAST BINGO: " + str(scores[len(scores) - 1]))

if __name__ == "__main__":
    main()