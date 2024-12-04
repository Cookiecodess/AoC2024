from input import Input
from testInput import TestInput
ws = Input.s
# ws = TestInput.s




# 1. Look for "X"
# 2. Look at all eight letters around said "X" for "M", if no "M" abort
# 3. Remember the direction
# 4. In the same direction, look for "A" then "S", if no then abort
# 5. Increment counter, move on and look for next "X", repeat
# 

def countXmas(ws: str) -> int:
    counter = 0
    ws = ws.splitlines()
    print(ws)
    rows = len(ws)
    cols = len(ws[1])
    for row in range(rows):
        for col in range(cols):
            if ws[row][col] == "X":
                right = False
                down = False
                left = False
                up = False
                if cols - col >= 4:
                    right = True
                if rows - row >= 4:
                    down = True
                if col >= 3:
                    left = True
                if row >= 3:
                    up = True

                if right and ws[row][col+1:col+4] == "MAS":
                    counter += 1
                if down and ws[row+1][col] == "M" and ws[row+2][col] == "A" and ws[row+3][col] == "S":
                    counter += 1
                if left and ws[row][col-3:col] == "SAM":
                    counter += 1
                if up and ws[row-1][col] == "M" and ws[row-2][col] == "A" and ws[row-3][col] == "S":
                    counter += 1
                
                if right and down and ws[row+1][col+1] == "M" and ws[row+2][col+2] == "A" and ws[row+3][col+3] == "S":
                    counter += 1
                if left and down and ws[row+1][col-1] == "M" and ws[row+2][col-2] == "A" and ws[row+3][col-3] == "S":
                    counter += 1
                if left and up and ws[row-1][col-1] == "M" and ws[row-2][col-2] == "A" and ws[row-3][col-3] == "S":
                    counter += 1
                if right and up and ws[row-1][col+1] == "M" and ws[row-2][col+2] == "A" and ws[row-3][col+3] == "S":
                    counter += 1

    return counter


print(countXmas(ws))
# ws=ws.splitlines()
# print(ws[0][2])