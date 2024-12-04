num_safe = 0

f = open("day2-input.txt", "rt")
# f = open("day2-test.txt", "rt")
         
for report in f:
    safe = True
    
    levels = report.split()
    for i in range(len(levels)):
        levels[i] = int(levels[i])

    if levels[0] == levels[1]:
        safe = False
        
    elif levels[1] > levels[0]:
        for i in range(len(levels) - 1):
            if levels[i+1] < levels[i] or abs(levels[i+1]-levels[i]) < 1 or abs(levels[i+1]-levels[i]) > 3:
                safe = False
                break
    else:
        for i in range(len(levels) - 1):
            if levels[i+1] > levels[i] or abs(levels[i+1]-levels[i]) < 1 or abs(levels[i+1]-levels[i]) > 3:
                safe = False
                break

    if safe == True:
        num_safe += 1
    
    print(report)
    print(levels)
    print(safe)
      

print(num_safe)   
