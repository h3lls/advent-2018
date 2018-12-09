from sys import stdin

data = [int(x) for x in open("input.txt").readlines()]

freq = 0
freq_hist = set()
while True:
    for d in data:
        freq += d
        if freq in freq_hist:
            print("Found Twice: " + str(freq));
            exit()
        else:
            freq_hist.add(freq)
