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

def main():
    start_counter = 8
    restart_counter = 6
    epoch_count = int(sys.argv[2])
    fishes = read_input(sys.argv[1]) 
    for epoch in range(0, epoch_count):
        new_fishes = []
        for i in range(0, len(fishes)):
            #print(fs)
            if fishes[i] == 0:
                fishes[i] = restart_counter
                new_fishes.append(start_counter)
            else:
                fishes[i] -= 1
        fishes += new_fishes
    #print_fishes(epoch_count, fishes)
    print("Fishes: " + str(len(fishes)))

if __name__ == "__main__":
    main()
