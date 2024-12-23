from testInput import TestInput
from input import Input

# rules = TestInput.rules.strip()
# updates = TestInput.updates.strip()
rules = Input.rules.strip()
updates = Input.updates.strip()

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

sum = 0
for update in updates:
    if inCorrectOrder(update, rules):
        midIndex = len(update) // 2
        sum += update[midIndex]

print(sum)