import sys
import utilities.input as utils

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

def analyze(input : list, digits_count : int, selector):
    group = list(input)
    for index in range(0, digits_count):
        if len(group) <= 1:
            continue
        ones_count = count_one_digit(index, group)
        selected_digit = selector(ones_count, len(group))
        zeros, ones = divide(index, group)
        if selected_digit == 1:
            group = ones
        else:
            group = zeros
    print(group)
    print(convert_to_decimal(group[0]))

# it returns begin or end by checking if value is lower or greater then limit
def switch(value : int, limit : int, begin : int, end : int) -> int:
    output = end
    if value < limit:
        output = begin
    return output

def oxygen_digit_selector(ones_count : int, group_count : int) -> int:
    limit = group_count // 2 + group_count % 2
    return switch(ones_count, limit, 0, 1)

def carbon_digit_selector(ones_count : int, group_count : int) -> int:
    limit = group_count // 2 + group_count % 2
    return switch(ones_count, limit, 1, 0)

def convert_to_decimal(number : list) -> int:
    value = 0
    exponent = len(number) - 1 
    for digit in number:
        value += pow(2, exponent) * int(digit)
        exponent -= 1
    return value

def main():
    lines = utils.read_input(sys.argv[1])
    input = [utils.convert_to_binary_list(ln) for ln in lines]
    input_count = len(input)
    digits_count = count_digits(input)
    print("oxygen")
    analyze(input, digits_count, oxygen_digit_selector)
    print("C02")
    analyze(input, digits_count, carbon_digit_selector)

def test_count_digits():
    assert(count_digits([[1, 0, 0]]) == 3)

def test_divide():
    input = [utils.convert_to_binary_list([1, 0, 0])]
    input.append(utils.convert_to_binary_list([1, 0, 1]))
    input.append(utils.convert_to_binary_list([1, 1, 1]))
    input.append(utils.convert_to_binary_list([0, 0, 1]))
    input.append(utils.convert_to_binary_list([0, 0, 0]))
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