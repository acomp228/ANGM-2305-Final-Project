# Carrot Quest

## Repository 
<https://github.com/acomp228/ANGM-2305-Final-Project>

## Description
This is a grid based puzzle game. The player must move the player character across a maze-like board grid,
collecting items and avoiding enemies to progress to the next level.

## Features
- Player Movement
    - Player will start in a designated part of the game "board". Each press of an arrow key will move the player 
    one grid in that direction, by updating the x, y of it's position by a set amount equal to the center of the next grid.

- Enemy Movement
    - Similar to the player movement, the enemies of this game will move from grid space to grid space by updating the
    x,y of their positions by the correct amount. The enemy will only move (on set paths) when the player moves, creating a puzzle
    that the player has to figure out in order to reach all the collectibles in the maze while avoiding the enemies.

- Collectible Items
    - There will be collectible items located on specified grids on the board, represented by some kind of visual marker. When the player
    moves onto these same spots, the art will disappear from the screen, likely by creating some kind of conditional for their visiblity based on
    if a player lands on their space. They will also increment a "collectible" variable in the code and when that reaches a certain number, the  
    "win" condition that ends the level will be triggered.

- Winning & Losing
    - When the player collects all the collectibles in the level, a "win" condition will be triggered. This will likely be done by setting a conditional
    that will only activate when the 'collectible' variable is incremented to a certain number (however many collectibles are in the level). The player 
    will 'lose' a level when the player character and an enemy land on the same grid space. This will trigger the "lose" state conditional, which will reset
    the level, likely by ending whatever game functions the game was currently running (aside from the event loop) and resetting variables to their original
    values.

## Challenges

- I will need to research how to import art assets into pygame. At this point I know how to draw very simple squares and lines, but I would need to learn how to execute
more complex visuals like a rabbit, a fox, and a carrot as well as some kind of static background, like a field or a forest. 

- I will need to learn how to create a simple maze using pygame. At this point, I believe I know how to make the visual walls and barriers well enough, but I will have to research how to prevent player movement through walls, for both the player and enemies. 

- I will also have to learn to create "win" and "lose" conditions within pygame. I understand the concepts in game design from my Scripting class, but specifically implementing the ability to lose & reset the level, as well as winning and continuing to a new level within python will be something I have to learn for this project.

## Outcomes
Ideal Outcome:
- Ideally, the game will consisit of two playable levels, with different board layouts. There will be art assets to represent the player character (a rabbit), the enemies
(a fox), the collectibles (carrots), as well as some kind of static background image behind the grid. The players and enemies will move through the set maze & when the player has collected all the collectibles for a certain level, a "You Win" screen will pop up before taking the player to the next level.

Minimum Viable Outcome:
- Minimum viable outcome is only one playable level, with much more simplistic art assets, likely simple colored cubes and a black background. There will still be a maze for the player to work through, and movement for the player and enemy should work in the same way. There does not need to be a "You Win" message when the player picks up the last collectible, the game can just end and the player can quit out of the game, as there is not a 2nd level for the player to move on to.


## Milestones
- Week 1:
1: Create Level 1 Board
2: Create Player Movement Logic
3: Create Enemy Movement Logic

- Week 2:
1: Create Collectible Logic
2: Create Win & Lose Logic
3: Create Level 2 Board

- Week 3 (Final):
1: Replace Temp Assets with Final Art
2: Record Final Presentation
