# Notes — GenAI-ML / Week01 / Day5

## Quick notes
- 

## Snippets / Commands
- 

## TODO
- 
I am going to build a tic tac toe game in basic python that will dispaly in terminal of my vs code.


TIP_TOP_TIC_TAC_TOE 

This TIC TAC TOE will be played on the field 20x20. 
Two players take turns by entering coordinates (x;y) in the terminal. 
The goal is to build 5 characters in a row (vertically, diagonally or horzontally). 
The rounds are plae with same omount of moves and each round ends when 
1 or 2 players have such a long row assembeled.
A game ends when the selected omount of rounds runs out (1 to 7).  
Stats, symbols and Nicknames, messages and rounds remaining will be dispalyed under the field.


Scenario:
 
0. The rules are displyed and 2 players are invited to play 1 to 7 rounds
(they enter this amount to initiate the game).

1. Players enter their nicknames and select 1 letter from the english alphabet for the game.

2. Players take consequitive turns by entering x;y coordinates in the terminal 
and their selected letter appears in the field.

3. If one of the players assembles a row of 5 diagonally, 
horizontally or vertically the message appears "LAST CHANCE!".

4. The other player then makes their final move and if they manage to assemble a row of 5 too
the message appears "DRAW" and players get a point each. 
If only the one palayer has a row of five assembled message dispalyes the Nikname Takes 
and ads 1 point to that player.

5. The next round begins emmidiately with the dispaly of the accumulated score, 
last message, and the rounds remaining counter.

6. The game ends once rounds remaining counter equals zero. 
Message displays the Victory nickname and the letter of the player who won more rounds.
And if the amount of victoiries is equal it displays the message DRAW 
and askes in the input to play again (yep or nope).