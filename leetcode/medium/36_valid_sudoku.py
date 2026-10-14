# LeetCode 36 — Valid Sudoku
# Determine whether a 9 x 9 Sudoku board is valid.
# Only the filled cells need to be validated according to these rules:
# 1. Each row must contain the digits 1–9 without repetition.
# 2. Each column must contain the digits 1–9 without repetition.
# 3. Each of the nine 3 x 3 sub-boxes must contain the digits 1–9 without repetition.
# A partially filled board can be valid even if it is not solvable.
# Example:
# Input:
# [
#  ["5","3",".",".","7",".",".",".","."],
#  ["6",".",".","1","9","5",".",".","."],
#  [".","9","8",".",".",".",".","6","."],
#  ["8",".",".",".","6",".",".",".","3"],
#  ["4",".",".","8",".","3",".",".","1"],
#  ["7",".",".",".","2",".",".",".","6"],
#  [".","6",".",".",".",".","2","8","."],
#  [".",".",".","4","1","9",".",".","5"],
#  [".",".",".",".","8",".",".","7","9"]
# ]

# Output: true

# Constraints:
# board.length == 9
# board[i].length == 9
# board[i][j] is a digit '1'–'9' or '.'

def valid_sudoku(board):
    #we can just use counters for each 'bucket' (row, column, or square) and add shit to said buckets based on where we are in an array. 
    #it would be maximally efficient if we could identify and break if we notice repetitions of a number.
        #tryign to think if theres a better way than conditional checking 'in' and adding if not rejecting whole board if no.
        #wait we dont even need counters let just use sets lol. 
        #this seems efficient on its face because no matter what we gotta look at each location till we find something not allowed.
    #seems like we dont have to check ourselves if it 1-9, but just for repetitions

    # squares = set() #starting top left, going across then moving down
    # rows = set()
    # columns = set() #the way you think i'm organizing it lol
    #hmmm now i'm thinking and we dont w ant sets we want arrays of 9 sets.
    #row and column are easy, how do we give 'addresses' to knowing what square we are in though.... could do manually with < but that seems
    #   dumb. like there has to be a better way than writing conditionals based on row/column indices to figure out what square were in.....
    #  i obviously dont want to just go back through a second time just to do squares in eloquent way, might as well toss them in their buckets
    #  when we first iterate.... hmm.  
    # figuring this out conceptually is easy, the thing thats taking me a minutes is that i want to do it without creating 9 conditionals checking 
    # i, j <= some  shit lol
    # will need diff mathmatical formulas for 
    # we just // 3
    # i shall use row, column coordinate space or whatever that is its not like geometry in school coordinate space because, well it matches 
    # natural data structure 
    #  

    rows = [set() for _ in range(9)]
    columns = [set() for _ in range(9)]
    #we want squares to be a tiny coordinate system so instead of a list of 9 sets we'll make a list of list of 3 sets. 
    squares = [[set() for _ in range(3)] for pasta in range(3)]

    

    # for row in board:
    #     for location in row:

    #wanna use indices so i can have i, j available. 
    for i in range(9):

        square_row = i // 3
        #i want you to know i removed len(board) and len(i) because i'm efficient asf
        for j in range(9):
            current_value = board[i][j]

            if current_value != '.':
                # this makese sense as rows because i is the same number for a whole row so for rows we add all 9 sequentially
                if current_value in rows[i]:
                    return False
                else:
                    rows[i].add(current_value)

                #this makes sense for columns because as you iterate through one of the board lists your actually listing column number
                #will add to same bucket every 9
                if current_value in columns[j]:
                    return False
                else:
                    columns[j].add(current_value)

                square_column = j  // 3
                if current_value in squares[square_row][square_column]:
                    return False
                else:
                    squares[square_row][square_column].add(current_value)

    return True

Input = [
 ["5","3",".",".","7",".",".",".","."],
 ["6",".",".","1","9","5",".",".","."],
 [".","9","8",".",".",".",".","6","."],
 ["8",".",".",".","6",".",".",".","3"],
 ["4",".",".","8",".","3",".",".","1"],
 ["7",".",".",".","2",".",".",".","6"],
 [".","6",".",".",".",".","2","8","."],
 [".",".",".","4","1","9",".",".","5"],
 [".",".",".",".","8",".",".","7","9"]
]      

print(valid_sudoku(Input))

            
            

            
            


        

