from input import Input
from testInput import TestInput
ws = Input.s
# ws = TestInput.s


def countCrossMas(ws: str) -> int:
    counter = 0
    ws = ws.splitlines()
    print(ws)
    rows = len(ws)
    cols = len(ws[1])
    for row in range(rows):
        for col in range(cols):
            if ws[row][col] == "A" and row >= 1 and col >= 1 and rows-row>=2 and cols-col>=2:
                up_left = ws[row-1][col-1]
                up_right = ws[row-1][col+1]
                down_right = ws[row+1][col+1]
                down_left = ws[row+1][col-1]
                backslash: bool = up_left=="M" and down_right=="S" or up_left=="S" and down_right=="M"
                forwslash: bool = up_right=="M" and down_left=="S" or up_right=="S" and down_left=="M"
                if backslash and forwslash:
                    counter+=1
                

    return counter


print(countCrossMas(ws))
# ws=ws.splitlines()
# print(ws[0][2])