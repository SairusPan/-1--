#阶段1
def pretty_print(board):
    """ Accepts a list of lists `board` as input
    and returns the game board.   
    """
    # sp2 is a format specifier
    sp2 = len('  '.join(board[0]))
    # Printing 0 with three initial spaces first
    print(f"   {(0)}", end="  ")
    # Printing column number
    for columns in range(1, len(board[0])):
        print(f"{str(columns):<3.3s}", end="")
    # A new empty line for formatting purposes
    print('')
    # Printing dashed lines
    print(f"   {len(board[0])*3*'-'}")
    # Printing row numbers and the board
    for rows in range(len(board)):
        print(f"{str(rows):>2.2s}|{str('  '.join(board[0])):<{sp2+2}.{sp2}s}")
    print('')

#阶段2
DIR_UP = "u"
DIR_DOWN = "d" 
DIR_LEFT = "l"
DIR_RIGHT = "r"
BLANK_PIECE = "Z"
def validate_input(board, position, direction):
    """ Accepts a list of lists `board` and a tuple of integers `position`
    and a string `direction` as inputs. Returns True if the inputs are valid
    or False if the inputs are invalid.
    """
    dic = {}
    # Counting frequencies of colours with dictionary
    for rows in board:
        for pieces in rows:
            if pieces in dic.keys():
                dic[pieces] += 1
            else:
                dic[pieces] = 1
    # Iterating over keys in the dictionary
    for keys in dic.keys():
        # Iterating over the board
        for i in range(0, len(board) - 1):
            # Listing conditions
            if (len(board[i]) == len(board[i + 1]) and 'A' <= keys <= 'Y' 
                and dic[keys] % 4 == 0 and len(board[i])>=2
                and len(board[i + 1])>=2 and str(board).isupper() 
                and 0<=position[0]<=len(board[0]) 
                and 0<=position[1]<=len(board[1])
                and len(position) == 2
                and (direction in ("u, d, l, r"))):
                
                return True
            else:
                return False
#阶段3
DIR_UP = "u"
DIR_DOWN = "d"
DIR_LEFT = "l"
DIR_RIGHT = "r"
BLANK_PIECE = "Z"
def legal_move(board, position, direction):
    """Accepts a list of lists `board` and a tuple of integers `position`
    and a string `direction` as inputs. Returns True if the move is legal or
    False if the move is not legal.
    """
    row = position[0]
    column = position[1]
    # Cases for moving up
    if DIR_UP in direction and row == 0: 
        return False
    if (DIR_UP in direction  # Checking blank pieces
        and (BLANK_PIECE == board[row - 1][column] 
             or board[row][column] == BLANK_PIECE)):
        return False
    if (DIR_UP in direction 
        and 0 < column <len(board[0]) - 1 and row == 1):
        if (board[row - 1][column - 1] == board[row][column] 
            or board[row - 1][column + 1] == board[row][column]):
            return True
        elif (board[row - 1][column] == board[row][column + 1] 
              or board[row - 1][column] == board[row][column - 1]):
            return True
        elif board[row - 1][column] == board[row + 1][column]:
            return True
        else:
            return False
    if (DIR_UP in direction and 0 < column <len(board[0]) - 1 
        and row == len(board[0]) - 1):
        if (board[row - 1][column + 1] == board[row][column] 
            or board[row - 1][column - 1] == board[row][column]):
            return True
        elif board[row + 2][column] == board[row][column]:
            return True
        elif (board[row - 1][column] == board[row][column + 1] 
              or board[row - 1][column] == board[row][column - 1]):
            return True
        else:
            return False
    if (DIR_UP in direction and column == len(board[0]) - 1 
        and 0<row<len(board[0]) - 1):
        if board[row - 1][column - 1] == board[row][column]:
            return True
        elif board[row - 1][column] == board[row][column - 1]:
            return True
        elif board[row + 1][column] == board[row - 1][column]:
            return True
        elif board[row - 2][column] == board[row][column]:
            return True
        else:
            return False
    if (DIR_UP in direction and column == 0 
        and 0 < row < len(board[0]) - 1):
        if board[row - 1][column + 1] == board[row][column]:
            return True
        elif board[row - 1][column] == board[row][column + 1]:
            return True
        elif board[row + 2][column] == board[row][column]:
            return True
        elif board[row + 1][column] == board[row - 1][column]:
            return True
        else:
            return False
    if DIR_UP in direction and column == 0 and row == 1:
        if board[row - 1][column + 1] == board[row][column]:
            return True
        elif board[row - 1][column] == board[row][column + 1]:
            return True
        elif board[row - 1][column] == board[row + 1][column]:
            return True
        else:
            return False
    if DIR_UP in direction and column == len(board[0]) - 1 and row == 1:
        if board[row - 1][column - 1] == board[row][column]:
            return True
        elif board[row - 1][column] == board[row + 1][column]:
            return True
        elif board[row - 1][column] == board[row][column - 1]:
            return True
        else:
            return False
    if DIR_UP in direction and column == 0 and row == len(board[0]) - 1:
        if board[row - 1][column + 1] == board[row][column]:
            return True
        elif board[row - 1][column] == board[row][column + 1]:
            return True
        elif board[row - 2][column] == board[row][column]:
            return True
        else:
            return False
    if (DIR_UP in direction and column == len(board[0]) - 1 
        and row == len(board[0]) - 1):
        if board[row - 1][column - 1] == board[row][column]:
            return True
        elif board[row - 1][column] == board[row][column - 1]:
            return True
        elif board[row - 2][column] == board[row][column]:
            return True
        else:
            return False
    if (DIR_UP in direction and 0 <column<len(board[0]) - 1 
        and 0<row<len(board[0]) - 1):
        if (board[row - 1][column + 1] == board[row][column] 
            or board[row - 1][column - 1] == board[row][column]):
            return True
        elif (board[row - 1][column] == board[row][column + 1] 
              or board[row - 1][column] == board[row][column - 1]):
            return True
        elif (board[row - 2][column] == board[row][column] 
              or board[row + 1][column] == board[row - 1][column]):
            return True
        else:
            return False
    # Cases for moving down
    if (DIR_DOWN in direction 
        and row == len(board[0]) - 1): 
        return False
    if (DIR_DOWN in direction  # Checking for blank pieces
        and (board[row][column] == BLANK_PIECE 
             or board[row + 1][column] == BLANK_PIECE)):
        return False
    if (DIR_DOWN in direction and row == 0 
        and 0<column<len(board[0]) - 1):
        if (board[row + 1][column + 1] == board[row][column]
            or board[row + 1][column - 1] == board[row][column]):
            return True
        elif (board[row + 1][column] == board[row][column + 1] 
              or board[row + 1][column] == board[row][column - 1]):
            return True
        elif board[row + 2][column] == board[row][column]:
            return True
        else:
            return False
    if (DIR_DOWN in direction and row == len(board[0]) - 2 
        and 0<column<len(board[0]) - 1):
        if (board[row + 1][column + 1] == board[row][column] 
            or board[row + 1][column - 1] == board[row][column]):
            return True
        elif (board[row + 1][column] == board[row][column - 1] 
              or board[row + 1][column] == board[row][column + 1]):
            return True
        elif board[row - 1][column] == board[row + 1][column]:
            return True
        else:
            return False
    if (DIR_DOWN in direction and 0<row<len(board[0]) - 2 
        and column == len(board[column]) - 1):
        if board[row + 1][column - 1] == board[row][column]:
            return True
        elif board[row + 1][column] == board[row][column - 1]:
            return True
        elif (board[row + 2][column] == board[row][column] 
              or board[row - 1][column] == board[row + 1][column]):
            return True
        else:
            return False
    if DIR_DOWN in direction and 0<row<len(board[0]) - 2 and column == 0:
        if board[row + 1][column + 1] == board[row][column]:
            return True
        elif board[row + 1][column] == board[row][column + 1]:
            return True
        elif (board[row + 2][column] == board[row][column] 
              or board[row - 1][column] == board[row + 1][column]):
            return True
        else:
            return False
    if (DIR_DOWN in direction and column == len(board[0]) - 1 
        and row == 0):
        if board[row + 1][column - 1] == board[row][column]:
            return True
        elif board[row + 1][column] == board[row][column - 1]:
            return True
        elif board[row + 2][column] == board[row][column]:
            return True
        else:
            return False
    if DIR_DOWN in direction and column == 0 and row == 0:
        if board[row + 1][column + 1] == board[row][column]:
            return True
        elif board[row + 1][column] == board[row][column + 1]:
            return True
        elif board[row + 1][column] == board[row][column]:
            return True
        else:
            return False
    if (DIR_DOWN in direction and column == len(board[0]) - 1 
        and row == len(board[0]) - 2):
        if board[row + 1][column - 1] == board[row][column]:
            return True
        elif board[row + 1][column] == board[row][column - 1]:
            return True
        elif board[row + 1][column] == board[row - 1][column]:
            return True
        else:
            return False
    if (DIR_DOWN in direction and column == len(board[0]) - 1 
        and row == len(board[0]) - 2):
        if board[row + 1][column - 1] == board[row][column]:
            return True
        elif board[row + 1][column] == board[row][column - 1]:
            return True
        elif board[row + 1][column] == board[row - 1][column]:
            return True 
        else:
            return False
    if DIR_DOWN in direction and column == 0 and row == len(board[0]) - 2:
        if board[row + 1][column + 1] == board[row][column]:
            return True
        elif board[row + 1][column] == board[row][column + 1]:
            return True
        elif board[row - 1][column] == board[row + 1][column]:
            return True
        else:
            return False
    if (DIR_DOWN in direction and 0<column<len(board[0]) - 1 
        and 0<row<len(board[0]) - 2):
        if (board[row + 1][column + 1] == board[row][column] 
            or board[row + 1][column - 1] == board[row][column]):
            return True
        elif (board[row + 1][column] == board[row][column - 1] 
              or board[row + 1][column] == board[row][column + 1]):
            return True
        elif board[row + 2][column] == board[row][column]:
            return True
        elif board[row - 1][column] == board[row + 1][column]:
            return True
        else:
            return False
    # Cases for moving left
    if DIR_LEFT in direction and column == 0:
        return False
    if (DIR_LEFT in direction  # Checking for blank pieces
        and (board[row][column] == BLANK_PIECE 
             or board[row][column - 1] == BLANK_PIECE)):
        return False
    if DIR_LEFT in direction and 1<column<len(board[0]) - 1 and row == 0:
        if board[row][column - 2] == board[row][column]:
            return True
        elif board[row][column - 1] == board[row][column + 1]:
            return True
        elif board[row + 1][column - 1] == board[row][column]:
            return True
        elif board[row + 1][column] == board[row][column - 1]:
            return True
        else:
            return False
    if (DIR_LEFT in direction and 1<column<len(board[0]) - 1 
        and row == len(board[0]) - 1):
        if board[row][column - 2] == board[row][column]:
            return True
        elif board[row][column - 1] == board[row][column + 1]:
            return True
        elif board[row - 1][column - 1] == board[row][column]:
            return True
        elif board[row][column - 1] == board[row - 1][column]:
            return True
        else:
            return False
    if DIR_LEFT in direction and column == 1 and row == 0:
        if board[row][column - 1] == board[row][column + 1]:
            return True
        elif board[row + 1][column - 1] == board[row][column]:
            return True
        elif board[row + 1][column] == board[row][column + 1]:
            return True
        else:
            return False
    if DIR_LEFT in direction and column== 1 and row == len(board[0]) - 1:
        if board[row][column - 1] == board[row][column + 1]:
            return True
        elif board[row - 1][column - 1] == board[row][column]:
            return True
        elif board[row - 1][column] == board[row][column - 1]:
            return True
        else:
            return False
    if DIR_LEFT in direction and column == len(board[0]) - 1 and row == 0:
        if board[row][column - 2] == board[row][column]:
            return True
        elif board[row + 1][column - 1] == board[row][column]:
            return True
        elif board[row + 1][column] == board[row][column - 1]:
            return True
        else:
            return False
    if (DIR_LEFT in direction and row == len(board[0]) - 1 
        and column == len(board[0]) - 1):
        if board[row][column - 2] == board[row][column]:
            return True
        elif board[row - 1][column - 1] == board[row][column]:
            return True
        elif board[row - 1][column] == board[row][column - 1]:
            return True
        else:
            return False
    if DIR_LEFT in direction and 0<row<len(board[0]) - 1 and column == 1:
        if board[row][column - 1] == board[row][column + 1]:
            return True
        elif board[row + 1][column - 1] == board[row][column]:
            return True
        elif board[row - 1][column - 1] == board[row][column]:
            return True
        elif board[row + 1][column] == board[row][column - 1]:
            return True
        elif board[row - 1][column] == board[row][column - 1]:
            return True
        else:
            return False
    if (DIR_LEFT in direction and column == len(board[0]) - 1 
        and 0 <= row <len(board[0]) - 1):
        if board[row - 1][column - 1] == board[row][column]:
            return True
        elif board[row + 1][column - 1] == board[row][column]:
            return True
        elif board[row + 1][column - 1] == board[row][column]:
            return True
        elif board[row + 1][column] == board[row][column - 1]:
            return True
        elif board[row - 1][column] == board[row][column - 1]:
            return True
        else:
            return False
    if (DIR_LEFT in direction and 1<column<len(board[0]) - 1 
        and 0<=row<len(board[0]) - 1):
        if board[row][column - 2] == board[row][column]:
            return True
        elif board[row][column - 1] == board[row][column + 1]:
            return True
        elif (board[row - 1][column - 1] == board[row][column] 
              or board[row + 1][column - 1] == board[row][column]):
            return True
        elif (board[row - 1][column] == board[row][column - 1] 
              or board[row + 1][column] == board[row][column - 1]):
            return True
        else:
            return False
    # Cases for moving right
    if (DIR_RIGHT in direction 
        and column == len(board[0]) - 1):
        return False
    if (DIR_RIGHT in direction  # Checking for blank pieces
        and (board[row][column] == BLANK_PIECE 
             or board[row][column + 1] == BLANK_PIECE)):
        return False
    if DIR_RIGHT in direction and row == 0 and column == 0:
        if board[row][column + 2] == board[row][column]:
            return True
        elif board[row + 1][column + 1] == board[row][column]:
            return True
        if board[row + 1][column] == board[row][column + 1]:
            return True
        else:
            return False
    if (DIR_RIGHT in direction 
        and column == len(board[0]) - 2 and row == 0):
        if board[row][column - 1] == board[row][column + 1]:
            return True
        elif board[row + 1][column + 1] == board[row][column]:
            return True
        elif board[row + 1][column] == board[row][column + 1]:
            return True
        else:
            return False
    if DIR_RIGHT in direction and 0<column<len(board[0]) - 2 and row == 0:
        if board[row][column + 2] == board[row][column]:
            return True
        elif board[row + 1][column + 1] == board[row][column]:
            return True
        elif board[row + 1][column] == board[row][column + 1]:
            return True
        elif board[row][column - 1] == board[row][column + 1]:
            return True
        else:
            return False
    if DIR_RIGHT in direction and column == 0 and row == len(board[0]) - 1:
        if board[row][column + 2] == board[row][column]:
            return True
        elif board[row - 1][column + 1] == board[row][column]:
            return True
        elif board[row - 1][column] == board[row][column + 1]:
            return True
        else:
            return False
    if (DIR_RIGHT in direction and column == len(board[0]) - 2 
        and row == len(board[0]) - 1):
        if board[row][column - 1] == board[row][column + 1]:
            return True
        elif board[row - 1][column + 1] == board[row][column]:
            return True
        elif board[row - 1][column] == board[row][column + 1]:
            return True
        else:
            return False
    if (DIR_RIGHT in direction and 0<column<len(board[0]) - 2 
        and row == len(board[0]) - 1):
        if board[row][column + 2] == board[row][column]:
            return True
        elif board[row][column - 1] == board[row][column + 1]:
            return True
        elif board[row - 1][column + 1] == board[row][column]:
            return True
        elif board[row - 1][column] == board[row][column + 1]:
            return True
        else:
            return False
    if DIR_RIGHT in direction and column == 0 and 0<row<len(board[0]) - 1:
        if board[row][column + 2] == board[row][column]:
            return True
        elif board[row - 1][column + 1] == board[row][column]:
            return True
        elif board[row + 1][column + 1] == board[row][column]:
            return True
        elif board[row + 1][column] == board[row][column + 1]:
            return True
        elif board[row - 1][column] == board[row][column + 1]:
            return True
        else:
            return False
    if (DIR_RIGHT in direction and column == len(board[0]) - 2 
        and 0<row<len(board[0]) - 1):
        if board[row][column - 1] == board[row][column]:
            return True
        elif board[row - 1][column + 1] == board[row][column]:
            return True
        elif board[row + 1][column + 1] == board[row][column]:
            return True
        elif board[row - 1][column] == board[row][column + 1]:
            return True
        elif board[row + 1][column] == board[row][column + 1]:
            return True
        else:
            return False
    if (DIR_RIGHT in direction and 0<column<len(board[0]) - 2 
        and 0<row<len(board[0]) - 1):
        if board[row][column + 2] == board[row][column]:
            return True
        elif board[row][column - 1] == board[row][column + 1]:
            return True
        elif board[row - 1][column + 1] == board[row][column]:
            return True
        elif board[row - 1][column + 1] == board[row][column]:
            return True
        elif board[row - 1][column] == board[row][column + 1]:
            return True
        elif board[row + 1][column] == board[row][column + 1]:
            return True
        else:
            return False