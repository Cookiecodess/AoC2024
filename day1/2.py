### Day 1: Historian Hysteria ###
#   Part 2   #

f = open("day1-input.txt", "rt")
# f = open("day1-test.txt", "rt")

a_dict = {}
b_dict = {}
a_list = []
b_list = []
for line in f:
    numbers = line.split()
    a = int(numbers[0])
    b = int(numbers[1])
    # Create two lists a and b containing the numbers
    a_list += [a]
    b_list += [b]
    # Create two dicts a and b, where keys: numbers, values: number of occurrences of that number
    if a not in a_dict:
        a_dict[a] = 1
    else:
        a_dict[a] += 1
    if b not in b_dict:
        b_dict[b] = 1
    else:
        b_dict[b] += 1


simscore = 0
for i in range(len(a_list)):
    simscore += a_list[i] * b_dict.get(a_list[i], 0)

print(simscore)