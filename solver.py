
# possible game board
board = [
    [6, 0, 0, 3, 0, 4, 0, 0, 0],
    [9, 8, 0, 0, 5, 0, 0, 0, 0],
    [0, 3, 0, 1, 0, 0, 0, 0, 8],
    [0, 0, 7, 2, 0, 3, 4, 0, 0],
    [1, 0, 0, 4, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 7, 0, 0, 9],
    [0, 0, 0, 0, 0, 0, 0, 0, 1],
    [7, 0, 8, 0, 0, 2, 3, 0, 5],
    [0, 5, 0, 0, 0, 0, 2, 0, 0],
]

def valid(b, num, pos):
    #check the row
    for i in range(len(b[0])):
        if b[pos[0]][i] == num and pos[1] != i:
            return False
    #check the column
    for i in range(len(b)):
        if b[i][pos[1]] == num and pos[1] != i:
            return False
    #check the box
    box_x = pos[1] // 3
    box_y = pos[0] // 3
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if b[i][j] == num and (i,j) != pos:
                return False
    return True

def print_board(b):
    for i in range(len(b)):
        if i % 3 == 0 and i != 0:
            print(" - - - - - - - - - - - ")
        
        for j in range(len(b[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(b[i][j])
            else:
                print(str(b[i][j]) + " ", end="")
print_board(board)
def find_empty(b):
    for i in range(len(b)):
        for j in range(len(b[0])):
            if b[i][j] == 0:
                return (i, j)
