import sys

from geometry import Vector2D, scale, sum, print_vector, magnitude

def read_input(path : str) -> list:
    with open(path, "r") as input_file:
        return input_file.readlines()

#def find_direction(command : str):
#    if command == "forward":
#        return [1.0, 0.0]
#    if command == "up":
#        return [0.0, -1.0]
#    if command == "down":
#        return [0.0, 1.0]
#    raise RuntimeError("unknown command: " + command)

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
    #versor[0] = versor[0] * magnitude
    #versor[1] = versor[1] * magnitude
    #return versor
    return scale(versor, magnitude)

#def sum(a, b):
#    assert(len(a) == 2)
#    assert(len(b) == 2)
#    c = [0.0, 0.0]
#    c[0] = a[0] + b[0]
#    c[1] = a[1] + b[1]
#    return c

def main():
    lines = read_input(sys.argv[1])
    input = (ln for ln in lines)
    position = Vector2D(0.0, 0.0)
    for line in input:
        motion = move(line)
        position = sum(position, motion)        
    #print(position)
    print_vector(position)
    print("magnitude: " + str(magnitude(position)))

if __name__ == "__main__":
    main()