from game import Game
from minigames.mastermind import mastermind

if __name__ == '__main__':
    jeux = Mastermind()
    jeux.generer()
    print(jeux.get_solution())
