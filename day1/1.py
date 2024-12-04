### Day 1: Historian Hysteria ###
#   Part 1   #

f = open("input.txt", "rt")
# f = open("test.txt", "rt")

totaldiff = 0
a = []
b = []

for line in f:
    numbers = line.split()
    a += [int(numbers[0])]
    b += [int(numbers[1])]

a.sort()
b.sort()

for i in range(len(a)):
    totaldiff += abs(a[i]-b[i])
    

print(a)
print(b)
print(totaldiff)