# Game of life

<!-- ABOUT THE CODE-->

The Game of Life is a cellular automaton devised by the British mathematician John Horton Conway in 1970. It is a zero-player game, meaning that its evolution is determined by its initial state, requiring no further input. One interacts with the Game of Life by creating an initial configuration and observing how it evolves.

## Instructions 

Run "pip install requirements.txt" in command terminal, preferably in a virtual environment.

Run main.py file.

The game will start in pause mode, press any key to exit pause.

With the left mouse button selesct the squares.

With the right mouse button deselect the squares.

The game ends when the window closes.


## Configuration

You can change properties like:
<ul>
  <li>Window size </li>
  <li>Squares per side </li>
  <li>Background color </li>
  <li>Square background color </li>
  <li>Grid color </li>
</ul>

When you call the class
GameOfLife(size= int , squaresPerSide= int , bgColor= [R, G, B] , squareBgColor= [R, G, B], gridColor= [R, G, B])
