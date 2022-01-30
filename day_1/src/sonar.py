import sys
import utilities.input as utils

def main():
    lines = utils.read_input(sys.argv[1])
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