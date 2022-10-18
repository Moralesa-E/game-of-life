import pygame
import numpy as np
import time

class GameOfLife:

    def __init__(self, size:int, squaresPerSide:int, bgColor:list = [25, 25, 25], squareBgColor:list =[255,255,255], gridColor:list = [128,128,128]) -> None:
        self.width = size
        self.height = size
        self.bgColor = bgColor
        self.squareBg = squareBgColor
        self.gridColor = gridColor
        self.numberColums = squaresPerSide
        self.numberRows = squaresPerSide
        self._heightSquare = self.height / self.numberRows
        self._widthSquare = self.width / self.numberColums
        self._runnig = True
        self._pause = True

    def init_game(self):
        pygame.init()
        self._screen = pygame.display.set_mode((self.height, self.width))
        self._screen.fill(self.bgColor)
        self._gameState = np.zeros((self.numberColums, self.numberRows))

        self.runGame()

    def runGame(self):

        while self._runnig:

            time.sleep(0.1)
            newGameState = np.copy(self._gameState)
            self._screen.fill(self.bgColor)

            ev = pygame.event.get()

            for event in ev:
                if event.type == pygame.QUIT:
                    self._runnig = False
                elif event.type == pygame.KEYDOWN:
                    self._pause = not self._pause

            #Events from mouse
            mouseClick = pygame.mouse.get_pressed()
            if mouseClick[0]:
                posX, posY = pygame.mouse.get_pos()
                celX, celY = int(np.floor(posX / self._widthSquare)), int(np.floor(posY / self._heightSquare))
                newGameState[celX, celY] = 1
            elif mouseClick[2]:
                posX, posY = pygame.mouse.get_pos()
                celX, celY = int(np.floor(posX / self._widthSquare)), int(np.floor(posY / self._heightSquare))
                newGameState[celX, celY] = 0

            #Algorithm
            for y in range(0, self.numberColums):
                for x in range(0, self.numberRows):
                    if not self._pause:

                        n_neigh =   self._gameState[(x-1) % self.numberColums, (y-1) % self.numberRows] + \
                                    self._gameState[(x)   % self.numberColums, (y-1) % self.numberRows] + \
                                    self._gameState[(x+1) % self.numberColums, (y-1) % self.numberRows] + \
                                    self._gameState[(x-1) % self.numberColums, (y)   % self.numberRows] + \
                                    self._gameState[(x+1) % self.numberColums, (y)   % self.numberRows] + \
                                    self._gameState[(x-1) % self.numberColums, (y+1) % self.numberRows] + \
                                    self._gameState[(x)   % self.numberColums, (y+1) % self.numberRows] + \
                                    self._gameState[(x+1) % self.numberColums, (y+1) % self.numberRows]
                        
                        if self._gameState[x,y] == 0 and n_neigh == 3:
                            newGameState[x,y] = 1

                        elif self._gameState[x,y] == 1 and (n_neigh < 2 or n_neigh > 3):
                            newGameState[x,y] = 0
                            
                    #Print Squares
                    poly =[ (    x*self._widthSquare,     y*self._heightSquare),
                            ((x+1)*self._widthSquare,     y*self._heightSquare),
                            ((x+1)*self._widthSquare, (y+1)*self._heightSquare),
                            (    x*self._widthSquare, (y+1)*self._heightSquare)]

                    if newGameState[x,y]==0:
                        pygame.draw.polygon(self._screen,self.gridColor,poly,1)
                    else:
                        pygame.draw.polygon(self._screen,self.squareBg,poly,0)

            self._gameState = np.copy(newGameState)
            pygame.display.flip()

        self.quitGame()

    def quitGame(self):
        pygame.quit()