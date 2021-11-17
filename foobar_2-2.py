# I should stop after this one, getting a bit hard for me
# and I know these are not optimal solutions
def solution(src, dest):
    # obvious case src == dest
    if src == dest:
        return 0
    # intuitively enumerate all possible single moves, then 
    # each move from that = double moves etc ...
    # first need to turn into coordinate system
    def coord(sqr):
        x = sqr % 8
        y = int(sqr / 8)
        return (x, y)
    coord_src = coord(src)
    coord_dest = coord(dest)
    # I looked up max moves is 6 (opposite corners) so should never go past 6
    move_count = 0
    def single_moves(coord):
        return [(coord[0] - 2, coord[1] + 1),
                (coord[0] - 2, coord[1] - 1),
                (coord[0] + 2, coord[1] + 1),
                (coord[0] + 2, coord[1] - 1),
                (coord[0] + 1, coord[1] + 2),
                (coord[0] + 1, coord[1] - 2),
                (coord[0] - 1, coord[1] + 2),
                (coord[0] - 1, coord[1] - 2)]
    # return [(coord[0] - 2, coord[1] + 1),
               # (coord[0] - 2, coord[1] - 1),
               # (coord[0] + 2, coord[1] + 1),
               # (coord[0] + 2, coord[1] - 1),
               # (coord[1] + 2, coord[0] + 1),
               # (coord[1] + 2, coord[0] - 1),
               # (coord[1] - 2, coord[0] + 1),
               # (coord[1] - 2, coord[0] - 1)] # oops this fails case 5
    possible_positions = single_moves(coord_src)
    next_moves = []
    while True:
        move_count += 1
        for move in possible_positions:
            if move[0] in range(8) and move[1] in range(8):
                if move == coord_dest:
                    return move_count
                else:
                    next_moves += single_moves(move)
        possible_positions = next_moves
        next_moves = []
