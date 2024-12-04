from testinput import TestInput
from input import Input

s = Input.s
# s = TestInput.s

# print(s)
# print(s.index("mul("))

# find index of "mul("
# add 4 to index, read a number, else abort
# read a comma, else abort
# read a number, else abort
# read ")", else abort
# delete substring from beginnign up to ")" from s
# repeat
ans = 0
no_more = False
while True:
    while True:
        try:
            i = s.index("mul(")
        except:
            no_more = True
            break
        i = i+4
        x_str = ""
        y_str = ""
        while s[i].isdigit():
            x_str += s[i]
            i += 1
        if s[i] != ",":
            break
        i += 1
        while s[i].isdigit():
            y_str += s[i]
            i += 1
        if s[i] != ")":
            break
        x = int(x_str)
        y = int(y_str)
        ans += x*y
        s = s[i+1:]
    if no_more:
        break
    s = s[i+1:]


print(ans)

