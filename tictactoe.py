"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """

    moves_x = 0
    moves_o = 0

    # Count the moves of X and O
    for row in range(3):
        for column in range(3):
            if board[row][column] == X:
                moves_x = moves_x + 1
            elif board[row][column] == O:
                moves_o = moves_o + 1

    # Check who's turn it is
    if board == initial_state() or moves_x <= moves_o:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    actions = set()

    for row in range(3):
        for column in range(3):
            if board[row][column] == EMPTY:
                actions.add((row, column))
    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    row, column = action

    # Raise ValueError if the action is not valid
    if board[row][column] != EMPTY:
        raise ValueError

    # Make a deepcopy of the board
    board_copy = copy.deepcopy(board)

    # Adapt deepcopy of board according to the action
    board_copy[row][column] = player(board)

    return board_copy


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    horizontally = check_horizontally(board)
    vertically = check_vertically(board)
    diagonally = check_diagonally(board)

    if horizontally != None:
        return horizontally
    elif vertically != None:
        return vertically
    elif diagonally != None:
        return diagonally
    else:
        return None


def check_horizontally(board):

    winner = None

    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2]:
            if board[row][0] == X:
                winner = X
            elif board[row][0] == O:
                winner = O
    return winner


def check_vertically(board):

    winner = None

    for column in range(3):
        if board[0][column] == board[1][column] == board[2][column]:
            if board[0][column] == X:
                winner = X
            elif board[0][column] == O:
                winner = O
    return winner


def check_diagonally(board):

    winner = None

    if board[0][0] == board[1][1] == board[2][2] or board[0][2] == board[1][1] == board[2][0]:
        if board[1][1] == X:
            winner = X
        elif board[1][1] == O:
            winner = O
    return winner


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    remaining_actions = 0
    board_winner = winner(board)

    # Check for EMPTY fields in board
    for row in range(3):
        if EMPTY in board[row]:
            remaining_actions = remaining_actions + 1

    if remaining_actions == 0 or board_winner != None:
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    utility = 0
    player = winner(board)

    if player == X:
        utility = 1
    elif player == O:
        utility = -1

    return utility


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    optimal_action = ()

    # Check if board is a terminal board
    if terminal(board):
        optimal_action = None

    # Get the current player
    current_player = player(board)

    if current_player == X:
        v = -math.inf
        for action in actions(board):
            action_value = max(v, min_value(result(board, action)))
            if action_value > v:
                v = action_value
                optimal_action = action

    elif current_player == O:
        v = math.inf
        for action in actions(board):
            action_value = min(v, max_value(result(board, action)))
            if action_value < v:
                v = action_value
                optimal_action = action

    return optimal_action


def max_value(board):

    v = -math.inf
    if terminal(board):
        return utility(board)

    for action in actions(board):
        action_value = max(v, min_value(result(board, action)))
        if action_value > v:
            v = action_value

    return v


def min_value(board):

    v = math.inf
    if terminal(board):
        return utility(board)

    for action in actions(board):
        action_value = min(v, max_value(result(board, action)))
        if action_value < v:
            v = action_value

    return v
