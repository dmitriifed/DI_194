# TIP_TOP_TIC_TAC_TOE
# 20x20 board, 2 players, 5-in-a-row to trigger "LAST CHANCE!" then final move.
# Runs in terminal (VS Code). No imports needed.

BOARD_SIZE = 20
WIN_LEN = 5
EMPTY = "."

def clear_screen():
    # Simple "clear" that works everywhere
    print("\n" * 60)

def print_rules():
    print("TIP_TOP_TIC_TAC_TOE")
    print("-" * 60)
    print("Rules:")
    print(f"• Board: {BOARD_SIZE}x{BOARD_SIZE}")
    print(f"• Goal: build {WIN_LEN} in a row (horizontal / vertical / diagonal).")
    print("• Players enter coordinates as x;y (1..20). Example: 7;13")
    print('• If a player makes 5-in-a-row: message shows "LAST CHANCE!"')
    print("  Then the other player gets ONE final move.")
    print('  If they also make 5-in-a-row: round is "DRAW" (both +1 point).')
    print("  Otherwise the first player wins the round (+1 point).")
    print("• Game ends when chosen rounds (1..7) are done.")
    print("-" * 60)

def get_rounds():
    while True:
        s = input("How many rounds do you want to play? (1 to 7): ").strip()
        if s.isdigit():
            n = int(s)
            if 1 <= n <= 7:
                return n
        print("Please enter a number from 1 to 7.")

def get_player_info(player_num, taken_symbols):
    while True:
        name = input(f"Player {player_num} nickname: ").strip()
        if name:
            break
        print("Nickname can't be empty.")

    while True:
        sym = input(f"{name}, choose ONE letter (A-Z) as your symbol: ").strip()
        if len(sym) == 1 and sym.isalpha():
            sym = sym.upper()
            if sym not in taken_symbols:
                taken_symbols.add(sym)
                break
            print("That symbol is already taken. Choose another.")
        else:
            print("Symbol must be exactly ONE English letter (A-Z).")

    return {"name": name, "symbol": sym, "points": 0}

def new_board():
    return [[EMPTY for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

def format_header_numbers():
    # Column header: 1..20
    header = "    "  # left padding for row numbers
    for x in range(1, BOARD_SIZE + 1):
        header += f"{x:>2} "
    return header.rstrip()

def print_board(board, players, status_message, rounds_left, round_no):
    clear_screen()
    print("TIP_TOP_TIC_TAC_TOE")
    print(f"Round: {round_no}    Rounds remaining after this: {rounds_left}")
    print()

    print(format_header_numbers())
    for y in range(BOARD_SIZE):
        row_num = f"{y+1:>2} "
        line = row_num + " "
        for x in range(BOARD_SIZE):
            line += f"{board[y][x]:>2} "
        print(line.rstrip())

    print("\n" + "-" * 60)
    p1, p2 = players
    print(f"{p1['name']} [{p1['symbol']}]  Points: {p1['points']}")
    print(f"{p2['name']} [{p2['symbol']}]  Points: {p2['points']}")
    print(f"Message: {status_message}")
    print("-" * 60)

def parse_move(s):
    # Accept "x;y" with optional spaces
    s = s.strip().replace(" ", "")
    if ";" not in s:
        return None
    parts = s.split(";")
    if len(parts) != 2:
        return None
    if not parts[0].isdigit() or not parts[1].isdigit():
        return None
    x = int(parts[0])
    y = int(parts[1])
    return x, y  # 1-based

def in_bounds(x, y):
    return 1 <= x <= BOARD_SIZE and 1 <= y <= BOARD_SIZE

def count_in_direction(board, symbol, x0, y0, dx, dy):
    # x0,y0 are 0-based
    count = 0
    x = x0 + dx
    y = y0 + dy
    while 0 <= x < BOARD_SIZE and 0 <= y < BOARD_SIZE and board[y][x] == symbol:
        count += 1
        x += dx
        y += dy
    return count

def has_five_in_row(board, symbol, x0, y0):
    # Check the 4 main directions through the last placed cell
    directions = [(1, 0), (0, 1), (1, 1), (1, -1)]
    for dx, dy in directions:
        left = count_in_direction(board, symbol, x0, y0, -dx, -dy)
        right = count_in_direction(board, symbol, x0, y0, dx, dy)
        total = 1 + left + right
        if total >= WIN_LEN:
            return True
    return False

def ask_move(player):
    while True:
        raw = input(f"{player['name']} [{player['symbol']}], enter x;y (1..20): ")
        parsed = parse_move(raw)
        if parsed is None:
            print("Invalid format. Use x;y (example: 7;13).")
            continue
        x, y = parsed
        if not in_bounds(x, y):
            print("Out of bounds. Coordinates must be 1..20.")
            continue
        return x, y

def play_one_round(players, round_no, rounds_left_after_this, start_index, last_round_message):
    board = new_board()
    moves_made = 0
    status_message = last_round_message if last_round_message else "Game start!"

    current_index = start_index
    last_chance = False
    last_chance_winner_index = None

    while True:
        print_board(board, players, status_message, rounds_left_after_this, round_no)
        current = players[current_index]
        other_index = 1 - current_index

        if last_chance and current_index != last_chance_winner_index:
            print('FINAL MOVE (because of "LAST CHANCE!")')

        x, y = ask_move(current)
        x0, y0 = x - 1, y - 1

        if board[y0][x0] != EMPTY:
            status_message = "That cell is already taken. Try again."
            continue

        board[y0][x0] = current["symbol"]
        moves_made += 1

        made_five = has_five_in_row(board, current["symbol"], x0, y0)

        # If someone just made 5-in-a-row:
        if made_five:
            if not last_chance:
                # Trigger LAST CHANCE, give opponent one final move
                last_chance = True
                last_chance_winner_index = current_index
                status_message = "LAST CHANCE!"
                current_index = other_index
                continue
            else:
                # This can only happen if opponent makes 5 on the final move
                status_message = "DRAW"
                players[0]["points"] += 1
                players[1]["points"] += 1
                print_board(board, players, status_message, rounds_left_after_this, round_no)
                return status_message

        # If we're in last chance and opponent has now played their final move, end round:
        if last_chance and current_index != last_chance_winner_index:
            winner = players[last_chance_winner_index]
            winner["points"] += 1
            status_message = f"{winner['name']} TAKES IT!"
            print_board(board, players, status_message, rounds_left_after_this, round_no)
            return status_message

        # Board full without any 5-in-a-row => draw (both +1 point)
        if moves_made >= BOARD_SIZE * BOARD_SIZE:
            status_message = "DRAW"
            players[0]["points"] += 1
            players[1]["points"] += 1
            print_board(board, players, status_message, rounds_left_after_this, round_no)
            return status_message

        # Normal turn switch
        current_index = other_index

def ask_play_again():
    while True:
        s = input("Play again? (yep/nope): ").strip().lower()
        if s in ("y", "yes", "yep"):
            return True
        if s in ("n", "no", "nope"):
            return False
        print("Please type yep or nope.")

def game():
    while True:
        clear_screen()
        print_rules()

        total_rounds = get_rounds()
        taken = set()
        p1 = get_player_info(1, taken)
        p2 = get_player_info(2, taken)
        players = [p1, p2]

        last_message = ""
        for r in range(1, total_rounds + 1):
            rounds_left_after_this = total_rounds - r
            start_index = (r - 1) % 2  # alternate who starts each round
            last_message = play_one_round(players, r, rounds_left_after_this, start_index, last_message)

        # Final result
        clear_screen()
        print("TIP_TOP_TIC_TAC_TOE — GAME OVER")
        print("-" * 60)
        print(f"{players[0]['name']} [{players[0]['symbol']}]  Points: {players[0]['points']}")
        print(f"{players[1]['name']} [{players[1]['symbol']}]  Points: {players[1]['points']}")
        print("-" * 60)

        if players[0]["points"] > players[1]["points"]:
            winner = players[0]
            print(f"VICTORY: {winner['name']} with [{winner['symbol']}]")
        elif players[1]["points"] > players[0]["points"]:
            winner = players[1]
            print(f"VICTORY: {winner['name']} with [{winner['symbol']}]")
        else:
            print("DRAW")

        print("-" * 60)
        if not ask_play_again():
            break

if __name__ == "__main__":
    game()