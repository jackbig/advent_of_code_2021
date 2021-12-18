import sys

def read_input(path : str) -> list:
    with open(path, "r") as input_file:
        return input_file.readlines()

def main():
    lines = read_input(sys.argv[1])
    input = (int(ln) for ln in lines)
    count = 0
    previous = None
    for value in input:
        if previous is not None and previous < value:
            count +=1
        previous = value
    print(count)

if __name__ == "__main__":
    main()