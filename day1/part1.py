from sys import stdin

s = stdin.read()

freq = 0
for s in s.split("\n"):
    freq += int(s)
print(freq)