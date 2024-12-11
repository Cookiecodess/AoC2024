from testInput import TestInput
from input import Input

input = TestInput.testInput.splitlines()
input = Input.input.splitlines()
m = [[grid for grid in line] for line in input] 

# 1. find ^'s coordinate [x][y]
# 2. UP: from [x-1][y] till [0][y] , find first #, then get coordinates of the #, let's call that [a][y]
# 3. for every [p][q] from [x][y] to [a-1][y] (x > a-1), add the tuple (p,q) to a set s.
# 4. [x][y] = [a+1][y]
# 5. RIGHT: from [x][y+1] till [x][len(line)] , find first #, then get coordinates of the #, let's call that [x][b]
# 6. for every [p][q] from [x][y+1] to [x][b-1] (y+1 < b), add the tuple (p,q) to s.
# 7. [x][y] = [x][b-1]
# 8. DOWN: from [x+1][y] till [len(input)][y] , find first #, get its coordinates [a][y]
# 9. for every [p][q] from [x+1][y] to [a-1][y] (x+1 < a-1), add the tuple (p,q) to s.
# 10.[x][y] = [a-2][y]
# 11. LEFT: from [x][y-1] till [x][0] (y-1 > 0), find first #, get its coordinates [x][b]
# 12.for every [p][q] from [x][y-1] to [x][b+1] (y-1 > b+1), add tuple (p,q) to s.
# 13.[x][y] = [x][b+1]

guard_x = 0
guard_y = 0
dir = 0 # 0: up, 1: right, 2: down, 3: left
num_rows = len(input)
num_cols = len(input[0])

# find guard's starting position
for row in range(0,num_rows):
    for col in range(0, num_cols):
        if m[row][col]=="^":
            guard_x, guard_y = obs_x, obs_y = row, col
            break

end = False
positions = set() # this will store all unique coordinates of walked positions. 
while not end:
    if dir%4 == 0: # up
        for x in range(guard_x - 1, -1, -1):
            if m[x][guard_y] == "#":
                end_grid = x                
                break
            elif x == 0: # last grid but still no obstacle
                end = True
                end_grid = -1 # walk to the top end
        for x in range(guard_x, end_grid, -1):
            t = (x, guard_y)
            m[x][guard_y] = "X"
            positions.add(t)
        guard_x = end_grid+1

    elif dir%4 == 1: # right
        for y in range(guard_y + 1, num_cols):
            if m[guard_x][y] == "#":
                end_grid = y                
                break
            elif x == num_cols-1: # last grid but still no obstacle
                end = True
                end_grid = num_cols # walk to the right end
        for y in range(guard_y+1, end_grid):
            t = (guard_x, y)
            m[guard_x][y] = "X"
            positions.add(t)
        guard_y = end_grid-1

    elif dir%4 == 2: # down
        for x in range(guard_x+1, num_rows):
            if m[x][guard_y] == "#":
                end_grid = x
                break
            elif x == num_rows-1: # last grid but still no obstacle
                end = True
                end_grid = num_rows # walk to the bottom end
        for x in range(guard_x+1, end_grid):
            t = (x, guard_y)
            m[x][guard_y] = "X"
            positions.add(t)
        guard_x = end_grid-1       
            
    else: # (dir%4==3) left
        for y in range(guard_y, -1, -1):
            if m[guard_x][y] == "#":
                end_grid = y
                break
            elif x == 0: # last grid but still no obstacle
                end = True
                end_grid = -1 # walk to the left end
        for y in range(guard_y, end_grid, -1):
            t = (guard_x, y)
            m[guard_x][y] = "X"
            positions.add(t)
        guard_y = end_grid+1
        
    dir+=1 # change direction for next iteration

# visualize map
c=0
for line in m:
    print(c, "".join(line))
    c+=1

# print solution
print(len(positions))