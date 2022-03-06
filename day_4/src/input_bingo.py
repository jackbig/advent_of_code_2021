import src.matrix as MTX

def read_numbers(input : str) -> list:
    return [int(x) for x in input.split(",")]

def read_cards(input : list) -> list:
    output = []
    mtx = None
    for ln in input:
        values = ln.split(" ")
        values = [int(x) for x in values if len(x) > 0]
        if len(values) > 0:
            if mtx is None:
                mtx = MTX.Matrix(4,5)
            mtx.add_row(values)
        else:
            output.append(mtx)
            mtx = None
    if mtx is not None:
        output.append(mtx)
    return output