class Matrix:
    def __init__(self, rows : int, columns : int) -> None:
        assert(rows > 0)
        assert(columns > 0)
        self._rows = rows
        self._columns = columns
        self._data = []

    def add_row(self, row : list) -> None:
        assert(len(row) == self._columns)
        copy = list(row)
        self._data.append(copy)

    def rows(self) -> int:
        return self._rows
    
    def columns(self) -> int:
        return self._columns

    def row(self, index : int) -> list:
        assert(index >= 0)
        assert(index < self._rows)
        return self._data[index]
    
    def column(self, index : int) -> list:
        assert(index >= 0)
        assert(index < self._columns)        
        return [self._data[i][index] for i in range(0, self._rows)]

    def __eq__(self, __o: 'Matrix') -> bool:
        if self._rows != __o._rows or self._columns != __o._columns:
            return False
        equality = True
        for i in range(0, self._rows):
            if self.row(i) != __o.row(i):
                equality = False
        for i in range(0, self._columns):
            if self.column(i) != __o.column(i):
                equality = False
        return equality

def printMatrix(mtx : 'Matrix') -> str:
    output = ""
    for i in range(0, mtx.rows()):
        is_first = True
        row = mtx.row(i)
        for item in row:
            if is_first:
                output += str(item)
                is_first = False
            else:
                output += ", " + str(item)
        output += "\n"
    return output
        


