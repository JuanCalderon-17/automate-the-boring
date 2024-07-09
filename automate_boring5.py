# myCat = {'size': 'fat', 'color': 'blue', 'disposition': 'loud'}
# print(myCat['size'])
# print('My cat is ' + myCat['size'] + ', I dont know what to do')

# wannaSee = {'siblings': 'monica', 'age': 7}
# print(wannaSee['weigth'])

theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ', 'mid-L': ' ', 'mid-M':
' ', 'mid-R': ' ', 'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
turn = 'X'

for i in range(9):
    print(theBoard)

To create the `isValidChessBoard()` function, we'll break down the problem step by step:

1. **Understand the constraints and rules of a valid chess board**:
   - Exactly one black king (`bking`) and one white king (`wking`).
   - Each player can have at most 16 pieces.
   - Each player can have at most 8 pawns.
   - All pieces must be on valid spaces from '1a' to '8h'.
   - The piece names must start with 'w' (white) or 'b' (black) followed by the piece type (`pawn`, `knight`, `bishop`, `rook`, `queen`, `king`).

2. **Plan how to implement these rules in the function**:
   - Validate positions.
   - Count pieces and ensure they are within the limits.
   - Ensure each piece name is correct.
   - Ensure exactly one white king and one black king are present.

3. **Implement the function**:
   - Use loops to check each condition.
   - Use dictionaries and sets to keep track of counts and positions.

Here’s a step-by-step guide to implementing the function:

### Step 1: Validate Positions

First, we need to check if all the positions in the dictionary are valid chessboard positions.

### Step 2: Count Pieces

We need to count the number of each type of piece to ensure they do not exceed the allowed numbers.

### Step 3: Check Piece Names

Verify that each piece name starts with 'w' or 'b' and is followed by a valid piece name.

### Step 4: Ensure Exactly One King for Each Color

Finally, check that there is exactly one `wking` and one `bking`.

Now, let's put it all together in the function:

```python
def isValidChessBoard(board):
    # Step 1: Validate Positions
    valid_positions = set(f"{row}{col}" for row in '12345678' for col in 'abcdefgh')
    piece_names = {'pawn', 'knight', 'bishop', 'rook', 'queen', 'king'}
    
    white_pieces = 0
    black_pieces = 0
    white_pawns = 0
    black_pawns = 0
    white_king_count = 0
    black_king_count = 0
    
    for position, piece in board.items():
        if position not in valid_positions:
            return False
        
        # Step 3: Check Piece Names
        if not (piece.startswith('w') or piece.startswith('b')):
            return False
        
        color = piece[0]
        piece_type = piece[1:]
        
        if piece_type not in piece_names:
            return False
        
        # Count pieces
        if color == 'w':
            white_pieces += 1
            if piece_type == 'pawn':
                white_pawns += 1
            if piece_type == 'king':
                white_king_count += 1
        elif color == 'b':
            black_pieces += 1
            if piece_type == 'pawn':
                black_pawns += 1
            if piece_type == 'king':
                black_king_count += 1
    
    # Step 2: Count Pieces
    if white_pieces > 16 or black_pieces > 16:
        return False
    
    if white_pawns > 8 or black_pawns > 8:
        return False
    
    # Step 4: Ensure Exactly One King for Each Color
    if white_king_count != 1 or black_king_count != 1:
        return False
    
    return True

# Test the function
chess_board = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}
print(isValidChessBoard(chess_board))  # Should print: True
```

### Explanation:
1. **Step 1**: We create a set of valid positions from '1a' to '8h'.
2. **Step 2 & Step 3**: Loop through each item in the dictionary to validate the position and piece name, and count the pieces.
3. **Step 4**: Ensure the counts for pieces, pawns, and kings are within the valid range and there is exactly one king for each color.

This structured approach ensures that we check all necessary conditions for a valid chessboard.
# Lists of gym names and their monthly fees
gyms = ["Strong Gym", "Tigers Gym", "Orange Gym", "Tower Gym"]
fees = [18, 22, 29, 20]

# Combine the two lists into pairs using zip and print each pair
for gym, fee in zip(gyms, fees):
    print(f"{gym}: ${fee:.2f}")

Strong Gym: $18.00
Tigers Gym: $22.00
Orange Gym: $29.00
Tower Gym: $20.00