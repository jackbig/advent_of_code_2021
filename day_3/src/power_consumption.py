import sys
import utilities.input as utils

def init_counters(counters : list, number : list) -> list:
    if len(counters) == 0:
        return [0 for i in range(0, len(number))]
    return counters

def update_counters(counters : list, number : list) -> list:
    output = []
    zipped = zip(counters, number)
    for count, digit in zipped:
        output.append(count + digit)
    return output

# Assumption: with a not odd number as total, count must be greater then the half value to be digit 1
def select_digit(count : int, total : int):
    limit = total // 2
    if count > limit:
        return (1, 0) 
    return (0, 1)

def select_one_digit(count : int, total : int) -> int:
    limit = total // 2
    if count > limit:
        return 1 
    return 0

def main():
    lines = utils.read_input(sys.argv[1])
    total = len(lines)
    counters = []
    for ln in lines:        
        number = utils.convert_to_binary_list(ln)
        counters = init_counters(counters, number)
        counters = update_counters(counters, number)
    gamma = 0
    rate = 0
    exponent = len(counters) - 1 
    for count in counters:
        gamma_digit, rate_digit = select_digit(count, total)
        gamma += pow(2, exponent) * gamma_digit        
        rate += pow(2, exponent) * rate_digit
        exponent -= 1
    print(str(gamma))
    print(str(rate))
    print(str(gamma * rate))
    
def test_convert_to_binary():
    input = "00100"
    output = [0,0,1,0,0]
    assert(utils.convert_to_binary_list(input) == output)
    input = "1010"
    output = [1,0,1,0]
    assert(utils.convert_to_binary_list(input) == output)

def test_init_counters():
    input = [1,1,1]
    output = [0,0,0]
    counters = []
    counters = init_counters(counters, input)
    assert(counters == output)    
    input = [1,1]
    counters = init_counters(counters, input)
    assert(counters == output)    

def test_update_counters():
    assert(update_counters([0,0,0], [1,1,1]) == [1,1,1])
    assert(update_counters([1,1,1], [1,0,0]) == [2,1,1])
    assert(update_counters([2,1,1], [0,1,0]) == [2,2,1])
    assert(update_counters([2,2,1], [0,0,1]) == [2,2,2])

def test_select_digit():
    assert(select_digit(0, 3) == (0, 1))
    assert(select_digit(0, 2) == (0, 1))
    assert(select_digit(5, 10) == (0, 1))
    assert(select_digit(5, 9) == (1, 0))

if __name__ == "__main__":
    #test_convert_to_binary()
    #test_init_counters()
    #test_update_counters()
    #test_select_digit()
    main()