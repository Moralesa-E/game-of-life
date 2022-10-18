from gameoflife import GameOfLife

def run():
    game = GameOfLife(size=500,squaresPerSide=50)
    game.init_game()

if __name__ =='__main__':
    run()