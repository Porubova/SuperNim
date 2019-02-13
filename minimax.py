U_cache = {}

def cache(U, state):
    U_cache[state] = U
    return U

def U(game, state, d = 10000):
    if game.terminal(state):
        return game.U_terminal(state)
    if state in U_cache:
        return U_cache[state]
    if not d:
        return cache(game.U_heur(state), state)
    if game.player(state) == "max":
        return cache(max(U(game, succ, d-1) for succ in game.succ(state)), state)
    if game.player(state) == "min":
        return cache(min(U(game, succ, d-1) for succ in game.succ(state)), state)
