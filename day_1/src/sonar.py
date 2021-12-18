import sys

def read_input(path : str) -> list:
    input = []
    with open(path, "r") as input_file:
        lines = input_file.readlines()
        for ln in lines:
            input.append(int(ln))
    return input

def count_rise(input : list, output_path : str) -> int:
    with open(output_path, "w") as output:
        previous = None
        count = 0
        for value in input:
            if previous is not None:
                if previous < value:
                    msg = str(previous) + " < " + str(value) + "\n"
                    output.write(msg)
                    count += 1
            previous = value
        output.write("total: " + str(count))
    return count

def main():
    input = read_input(sys.argv[1])
    count = count_rise(input, sys.argv[2])
    print(count)

if __name__ == "__main__":
    main()