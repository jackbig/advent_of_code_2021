class Vector2D:
    def __init__(self, x : float, y : float) -> None:
        self.x = x
        self.y = y

def magnitude(v : Vector2D) -> float:
    return v.x * v.y

def sum(a : Vector2D, b : Vector2D) -> Vector2D:
    return Vector2D(a.x + b.x, a.y + b.y)

def scale(v : Vector2D, s : float) -> Vector2D:
    return Vector2D(v.x * s, v.y * s)

def print_vector(v : Vector2D) -> str:
    print(str(v.x) + ", " + str(v.y))