import sys
from geometry import Vector2D, scale, sum, print_vector, magnitude
import utilities.input as utils

def find_direction(command : str) -> Vector2D:
    if command == "forward":
        return Vector2D(1.0, 0.0)
    if command == "up":
        return Vector2D(0.0, -1.0)
    if command == "down":
        return Vector2D(0.0, 1.0)
    raise RuntimeError("unknown command: " + command)

def move(line : str):
    command = line.split()
    if len(command) != 2 :
        raise RuntimeError("too many input: " + len(command))
    versor = find_direction(command[0])
    magnitude = int(command[1])
    return scale(versor, magnitude)

def main():
    lines = utils.read_input(sys.argv[1])
    input = (ln for ln in lines)
    position = Vector2D(0.0, 0.0)
    for line in input:
        motion = move(line)
        position = sum(position, motion)
    print_vector(position)
    print("magnitude: " + str(magnitude(position)))

if __name__ == "__main__":
    main()