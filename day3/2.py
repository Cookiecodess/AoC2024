from testinput import TestInput
from input import Input

s = Input.s
# s = TestInput.s2
# s="mul(2,3)do()don't()mul(3,4)"
start = 0
end = 0

while "don't()" in s:
    start = s.index("don't()")
    temp_s = s[start:]
    if "do()" in temp_s:
        end = temp_s.index("do()") + start
        s = s[:start] + s[end+4:]
    else:
        s = s[:start]
        break


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