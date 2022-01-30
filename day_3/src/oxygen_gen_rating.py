from collections import namedtuple
import sys

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

def count_one_digit(index : int, input : list) -> int:
    count = 0
    for number in input:
        digit = number[index]
        if digit == 1:
            count += 1
    return count

def divide(index : int, input : list) -> tuple:
    ones = []
    zeros = []
    for number in input:
        if number[index] == 1:
            ones.append(number)
        else:
            zeros.append(number)
    return (zeros, ones)

def count_digits(input : list) -> int:
    if len(input) == 0:
        raise ValueError("invalid input")
    return len(input[0])

def most_frequent_digit(digit_counter : int, input_count : int, min : int, max : int) -> int:
    limit = input_count // 2 + input_count % 2
    if digit_counter < limit:
        return min
    return max

def oxygen(input : list, digits_count : int):
    oxy_group = list(input)
    #carbon_group = list(input)
    for index in range(0, digits_count):
        ones_count = count_one_digit(index, oxy_group)
        limit = len(oxy_group) // 2 + len(oxy_group) % 2
        most_freq_digit = 1
        if ones_count < limit:
            most_freq_digit = 0
        zeros, ones = divide(index, oxy_group)
        #print(index, ones_count, most_freq_digit)
        if most_freq_digit == 1:
            oxy_group = ones
            #print(oxy_group)
        else:
            oxy_group = zeros
            #print(oxy_group)
    print(oxy_group)
    print(convert_to_decimal(oxy_group[0]))

def convert_to_decimal(number : list) -> int:
    value = 0
    exponent = len(number) - 1 
    for digit in number:
        value += pow(2, exponent) * int(digit)
        exponent -= 1
    return value

def carbon(input : list, digits_count : int):
    group = list(input)
    for index in range(0, digits_count):
        if len(group) > 1:
            ones_count = count_one_digit(index, group)
            limit = len(group) // 2 + len(group) % 2
            most_freq_digit = 0
            if ones_count < limit:
                most_freq_digit = 1
            zeros, ones = divide(index, group)
            print("ones: ")
            print(ones)
            print("zeros: ")
            print(zeros)
            if most_freq_digit == 1:
                group = ones
            else:
                group = zeros
            print("group:")
            print(group)
            print("-----")
    print(group)
    print(convert_to_decimal(group[0]))

def main():
    lines = read_input(sys.argv[1])
    input = [convert_to_binary_list(ln) for ln in lines]
    input_count = len(input)
    digits_count = count_digits(input)
    oxygen(input, digits_count)
    #carbon(input, digits_count)

def test_count_digits():
    assert(count_digits([[1, 0, 0]]) == 3)

def test_divide():
    input = [convert_to_binary_list([1, 0, 0])]
    input.append(convert_to_binary_list([1, 0, 1]))
    input.append(convert_to_binary_list([1, 1, 1]))
    input.append(convert_to_binary_list([0, 0, 1]))
    input.append(convert_to_binary_list([0, 0, 0]))
    zeros, ones = divide(0, input)
    assert(len(zeros) == 2)
    assert(len(ones) == 3)
    zeros, ones = divide(1, input)
    assert(len(zeros) == 4)
    assert(len(ones) == 1)
    zeros, ones = divide(2, input)
    assert(len(zeros) == 2)
    assert(len(ones) == 3)

def test_most_frequent():
    assert(most_frequent_digit(4, 7) == 1)
    assert(most_frequent_digit(4, 8) == 1)
    assert(most_frequent_digit(0, 7) == 0)
    assert(most_frequent_digit(3, 7) == 0)

if __name__ == "__main__":
    #test_count_digits()
    #test_divide()
    #test_most_frequent()
    main()