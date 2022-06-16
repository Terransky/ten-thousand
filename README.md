# Lab 9 - Ten Thousand Game 

## Project Description
A virtual replication of a dice game called Ten Thousand, perhaps more popularly known by
its trademarked name Farkle. 
* Version 1.00 - Currently employs a classes that contain methods to roll one to six 
dice of random integers between 1-6, score them, and bank them.
* Version 2.00 - Extend Ten Thousand game started in previous class to get the game in playable state.
* Version 3.00 - Gets the roller method and and the hot dice method is working. Zilch and cheater still in progress. 
* Version 4.00 - Zilch and cheater functionality works. 
* Version 5.00 - 4 functional bots designed by each member of the team. bots.py does not work with our code.

## Collaborators: Tony, Aoife, Jae, JJ

### Links and Resources
1. [How to play Ten Thousand](https://en.wikipedia.org/wiki/Dice_10000)
1. [Link to main](ten_thousand/game.py)


Setup
1. .env requirements (where applicable)
1. .venv
1. pip install pytest

Initialize

1. python3 game.py

Test

1. pytest tests/version_2/test_sim_basic.py

Status

1. We have implemented play() method on Game class in game.py
1. We are able to implement all functionalities including zilch and cheater

Test of Note:

1. Passed all of the tests in version_1
2. Passed all of the tests in version_2
3. Passed all of the tests in version_3
4. All bots average 10,000 points or better for 2000 games

