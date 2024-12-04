num_safe = 0

f = open("day2-input.txt", "rt")
# f = open("day2-test.txt", "rt")


def is_safe(l: list, depth: int = 1) -> bool:
    safe = True
    
    if l[0] == l[1]:
        safe = False
        
    elif l[1] > l[0]:
        for i in range(len(l) - 1):
            if l[i+1] < l[i] or abs(l[i+1]-l[i]) < 1 or abs(l[i+1]-l[i]) > 3:
                safe = False
                break
    else:
        for i in range(len(l) - 1):
            if l[i+1] > l[i] or abs(l[i+1]-l[i]) < 1 or abs(l[i+1]-l[i]) > 3:
                safe = False
                break

    if safe == False:
        if depth == 1:
            for i in range(len(l)):
                if i != len(l)-1:
                    temp_l = l[:i] + l[i+1:]
                else:
                    temp_l = l[:i]
                if is_safe(temp_l, 2) == True:
                    return True
        return False

    return True


for report in f: 
    levels = report.split()
    for i in range(len(levels)):
        levels[i] = int(levels[i])

    print(report)
    print(levels)
    
    if is_safe(levels) == True:
        num_safe += 1        
        print("SAFE")
    else:
        print("UNSAFE")

print(num_safe)

# l = [44 ,47, 50, 51, 53, 54, 53]
# print(is_safe(l))


    
    
      



