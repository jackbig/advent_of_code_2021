import sys

def read_input(path : str) -> list:
    counters = []
    with open(path, "r", encoding="utf8") as input_file:
        lines = input_file.readlines()
        for ln in lines:
            new_counters = [int(x) for x in ln.split(",")]
            counters += new_counters
    return counters

def print_fishes(epoch : int, fishes : list) -> None:
    msg = "Epoch " + str(epoch) + ": "
    for fish in fishes:
        msg += str(fish) + ", "
    print(msg)

def group(fishes : list, max_count : int) -> list:
    groups = [0 for i in range(0, max_count)]
    for index in fishes:
        assert(index < max_count)
        groups[index] += 1
    return groups

def main():
    max_counter = 8
    restart_counter = 6
    epoch_count = int(sys.argv[2])
    fishes = read_input(sys.argv[1]) 
    groups = group(fishes, max_counter + 1)
    for epoch in range(0, epoch_count):
        new_fishes = groups[0]
        for i in range(1, len(groups)):
            groups[i - 1] = groups[i]
        groups[len(groups) - 1] = new_fishes
        # the ones that reach 0 restart from restart_counter
        groups[restart_counter - 1] += new_fishes 
        #print(groups)
    #print_fishes(epoch_count, fishes)
    print("Fishes: " + str(sum(groups)))

if __name__ == "__main__":
    main()
