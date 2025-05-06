def solution(keyinput, board):
    location = [0,0]
    left_right_max = board[0]//2
    up_down_max = board[1]//2


    for move in keyinput:
        if move == 'up' and location[1] < up_down_max:
            location[1] += 1

        elif move == 'down' and location[1] > -up_down_max:
            location[1] -= 1

        elif move == 'left' and location[0] > -left_right_max:
            location[0] -= 1

        elif move == 'right' and location[0] < left_right_max:
            location[0] += 1

    return location