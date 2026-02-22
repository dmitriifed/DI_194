"""
GenAI-ML / Week01 / Day5 / ExerciseXP

TIP_TOP_TIC_TAC_TOE 

Spec:
- Board: 20x20
- Two players choose:
  - nickname
  - ONE English letter (A-Z) as symbol; must be different
- Moves are entered as: x;y  (both 1..20)
  - Define coords consistently: x = column, y = row
  - Invalid (bad format / out of bounds / taken cell) => ask again
- Extra rule: a player may surrender by typing TAP (case-insensitive)
  - Round ends immediately, opponent +1 point, message: "<name> tapped out!"
- Win condition: 5 in a row (horizontal / vertical / diagonal)
- LAST CHANCE round rule:
  - When a player first forms 5-in-a-row => show "LAST CHANCE!"
  - Opponent gets ONE final move
  - If opponent also forms 5 => "DRAW" and both +1 point
  - Else => first player wins round (+1 point), message: "<name> TAKES IT!"
- Game:
  - At start ask rounds: 1..7
  - After each round start next immediately, showing:
    score, last message, rounds remaining (under the field)
  - After all rounds: announce overall winner by points (or DRAW)
  - Ask play again? (yep/nope)
"""
# Outline:

# 1) Game setup (before any round starts)
# - Print rules (include x;y input and TAP surrender)
# - Ask number of rounds (1..7)
# - Ask each player: nickname + symbol letter (A-Z), symbols must differ
# - Store players as list of dicts: [{"name":..., "symbol":..., "points":0}, ...]
# - last_message = "Game start!"


rules = """TIP_TOP_TIC_TAC_TOE
Board: 20x20
Goal: Make 5 in a row (horizontal, vertical, diagonal)

How to play:
- On your turn, enter coordinates as x;y (example: 7;13)
- x and y must be between 1 and 20
- You can surrender the round by typing TAP

Round rules:
- If a player makes 5 in a row, the message "LAST CHANCE!" appears
- The other player gets ONE final move
- If the other player also makes 5 in a row, the round is a DRAW (both +1 point)
- Otherwise the first player wins the round (+1 point)

Game:
- Choose 1 to 7 rounds
- After each round you will see: score, last message, and rounds remaining
- After all rounds: the player with more points wins, otherwise DRAW
- You will be asked to play again (yep/nope)
"""

def print_rules():
    print(rules)
    pass

def get_rounds():
    # number 1...7
    pass

def game_setup():
    # total_rounds = input("... ")
    # player1_nickname = input("... ")
    # player1_letter = input("... ")
    # player2_nickname = input("... ")
    # player2_letter = input("... ")
    # last_message = ("game start!")
    pass


def get_player_info(player_nickname, player_letter):
    pass

def ask_play_again():
    pass

def main():
    total_rounds, players, last_message= game_setup()
pass

# + rounds, end, etc. 
if __name__ =="__main__":
main()






# 2) Board representation (20x20)
# - board is a 2D list of strings (rows x cols): 20 lists each length 20
# - empty cell is "."
# - print with row/col numbers 1..20
# - convert user coords (1..20) to internal (0..19):
#   x0 = x - 1, y0 = y - 1
# - access as board[y0][x0]




# 3) Input parsing + validation (x;y or TAP)
# - loop until valid action:
#   - read line
#   - if line == "TAP" (case-insensitive): return ("tap", None)
#   - else parse x;y (allow spaces)
#   - validate:
#     (1) correct format => two integers split by ";"
#     (2) bounds 1..20
#     (3) target cell is empty
#   - if invalid: print short error and continue




# 4) Turn system
# - track current player with current_index (0 or 1)
# - after a normal move: current_index = 1 - current_index
# - alternate starting player each round:
#   start_index = (round_no - 1) % 2




# 5) Win detection (5 in a row)
# - after placing symbol at (x0,y0), check only around that cell
# - check 4 line directions:
#   horizontal: (1,0)
#   vertical: (0,1)
#   diag down-right: (1,1)
#   diag up-right: (1,-1)
# - for each line: count same symbols in both directions + 1
# - if any total >= 5 => win detected




# 6) LAST CHANCE logic
# - variables/state:
#   last_chance = False
#   trigger_index = None
# - when someone first forms 5:
#   last_chance = True
#   trigger_index = current_index
#   message = "LAST CHANCE!"
#   force exactly one opponent move next
# - after opponent move:
#   - if opponent forms 5 => DRAW (+1 each)
#   - else => trigger player wins (+1)




# 7) Round loop + scoring + messages
# - start with fresh board each round
# - loop turns until round ends by:
#   - TAP surrender (opponent +1)
#   - LAST CHANCE resolved into win/draw
#   - board full => DRAW (+1 each) (optional but recommended)
# - return round_message to be displayed at start of next round




# 8) Game end + play again
# - after all rounds:
#   - compare players[0]["points"] vs players[1]["points"]
#   - announce VICTORY name + symbol OR DRAW
# - ask play again? (yep/nope)
# """




# def main():
#     pass

# if __name__ == "__main__":