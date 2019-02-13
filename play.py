from minimax import *

def move(game, state, d = 10000):
    if game.player(state) == "max":
        # initialize the search for best move
        # None indicates no move has been defined yet, and it's value is
        # -infinity
        best_move, best_util = None, -float("inf")

        for succ in game.succ(state):
            util_succ = U(game, succ, d)
            if util_succ > best_util:   # we improved
                best_move, best_util = succ, util_succ

    elif game.player(state) == "min":
        best_move, best_util = None, +float("inf")

        for succ in game.succ(state):
            util_succ = U(game, succ, d)
            if util_succ < best_util:   # we improved
                best_move, best_util = succ, util_succ

    else:                               # not "max" nor "min
        assert False                    # never reach this point
                
    return best_move
