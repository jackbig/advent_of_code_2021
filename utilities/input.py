def read_input(path : str) -> list:
    with open(path, "r") as input_file:
        return input_file.readlines()

def convert_to_binary_list(line : str) -> int:
    binary = []
    try:
        for i in range(0, len(line)):
            binary.append(int(line[i]))
    except ValueError:
        pass
    return binary