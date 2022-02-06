from src.matrix import Matrix

def find_commons(first : list, second : list) -> list:
    output = []
    for i in range(0, len(first)):
        for j in range(0, len(second)):
            if first[i] == second[j]:
                output.append(first[i])
    return output

def find_last(input : list, sequence : list) -> int:
    last = -1
    for i in sequence:
        index = input.index(i)
        if (index > last):
            last = index
    return input[last]

def bingo(input : list, mtx : Matrix):
    data = []
    for x in input:
        data.append(x)
        for i in range(0, mtx.columns()):
            commons = find_commons(data, mtx.column(i))
            if len(commons) == mtx.rows():
                return find_last(data, commons)
        for i in range(0, mtx.rows()):
            commons = find_commons(data, mtx.row(i))
            if len(commons) == mtx.columns():
                return find_last(data, commons)
    return None

def unmarked(input : list, mtx : Matrix) -> list:
    output = []
    for i in range(0, mtx.rows()):
        not_marked = [x for x in mtx.row(i) if next((j for j in input if j == x), None) == None]
        if len(not_marked) > 0:
            output += not_marked
    return output

def score(input : list, mtx : Matrix) -> int:
    output = 0
    last = bingo(input, mtx)
    if last is not None:
        output = sum(unmarked(input, mtx)) * last
    return output

