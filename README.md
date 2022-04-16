# Lab 4, tasks 5 and 6

---Task 5---
there are two modules for this task:
- one is the main module with the main game while loop
- another is the module describing the structure of the game data (implementation of classes, methods etc)
The idea of the game is:
1. moving from room to room
2. picking items if possible (there are specific items that can defeat enemy through his/her weakness)
3. fighting enemies if possible
4. reading the descriptions of the newly entered rooms
5. Win if one defeats the enemy 2 times
6. Fail if one fights the enemy with wrong item
7. Possibility to record the actions through redirecting output to the log file


---Task 6---
Basic principles are analogically to the task 5,
but the logic of the performed actions is altered and complicated
The game is meant to describe the traveller going through Lviv streets
in attempt to go from point A to point B.
There are certain adventures that can happen along the way with the traveller,
both interesting and dangerous.
The items, characters and locations are implemented here as well.
However, more complex hierarchy of these classes is written.
For example, the branch of Character - Enemy - Agressiveenemy - Criminal
gets more and more dangerous for each stage of the child class.
Some ideas in the Item class are altered, such as the circumstances the person
can find them. Activation items are added - they can be activated with a specific item (the chest - the code, the door - the key etc).
This logic is used to end the game: the final activation item (in this main module, the door) congratulates the player and ends the game.
Some additional functionality is added to the data scheme module that increases
the variants of plot development (characters' reactions, special actions with the specific hostile/friendly characters etc).
