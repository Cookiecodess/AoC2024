from testInput import TestInput
from input import Input

rules = TestInput.rules
updates = TestInput.updates
rules = Input.rules
updates = Input.updates

# for every update
#   for every page
#       find a rule containing that page.
#       if the rule's other page is in the current update: 
#           if rule is met:
#               go to next rule.
#           else:
#               this update ain't correctly-ordered. Go to next update.
#       else: 
#           find next rule containing that page.

# updates = updates.splitlines()
# for i in range(len(updates)):
#     # e.g. "1,2,3,4,5" -> ["1", "2", "3", "4", "5"]
#     updates[i] = updates[i].split(sep=",")
#     update = updates[i]
#     for j in range(len(update)):
#         # e.g. ["1", "2", "3", "4", "5"] -> [1, 2, 3, 4, 5]
#         update[j] = int(update[j])
updates = [[int(num) for num in line.split(",")] for line in updates.splitlines()]

# rules = rules.splitlines()
# for i in range(len(rules)):
#     # e.g. "2|4" -> ["2", "4"]
#     rules[i] = rules[i].split(sep="|")
#     rule = rules[i]
#     for j in range(len(rule)):
#         # e.g. ["2", "4"] -> [2, 4]
#         rule[j] = int(rule[j])
rules = [[int(num) for num in line.split(sep="|")] for line in rules.splitlines()]

def inCorrectOrder(update: list[int], rules: list[list[int]]) -> bool:
    for page in update:
        for rule in rules:
            if rule[0] == page and rule[1] in update:
                if not update.index(page) < update.index(rule[1]):
                    return False
            elif rule[1] == page and rule[0] in update:
                if not update.index(page) > update.index(rule[0]):
                    return False
    return True

# figured out the Divide and Conquer sorting algorithm completely by myself!
# edit: ok no this isn't Divide and Conquer. Apparently it's similar to quicksort but not exactly that either.
# Note: chatGPT says that Topological Sort would be most efficient.
def quicksortlike_sort(unsorted_l: list[int]) -> list[int]:
    l = []
    r = []
    dividingNumber = unsorted_l[0] # picking the first number is arbitrary
    for rule in rules:
        if rule[0] == dividingNumber and rule[1] in unsorted_l:
            r.append(rule[1])
        elif rule[1] == dividingNumber and rule[0] in unsorted_l:
            l.append(rule[0])
    if len(l) > 1: 
        l = quicksortlike_sort(l)
    if len(r) > 1: 
        r = quicksortlike_sort(r)
    return l + [dividingNumber] + r



sum = 0
for update in updates:
    print("\n", update) # for debugging
    if not inCorrectOrder(update, rules):
        sorted = quicksortlike_sort(update)
        print(sorted) # for debugging
        sum += sorted[len(sorted)//2]

print(sum)
