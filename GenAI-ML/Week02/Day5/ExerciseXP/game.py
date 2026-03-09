import random

class Game:
    def __init__(self):
        
        self.mapping={"1": "rock", 
                   "2": "paper", 
                   "3": "scissors"}
        self.item=["rock", "paper", "scissors"]


    def get_user_item(self):
    # ... code to get and validate user input ...
    #  ... code to return user's choice ...
    
        while True:
            choice = input("Choose: 1=rock, 2=paper, 3=scissors: ").strip().lower()
            if choice in self.mapping:
                return self.mapping[choice]
            print("_ERROR_ Please enter 1, 2, or 3.")
        
        

    def get_computer_item(self):
        return random.choice(self.item)
    #     # ... code to generate computer's choice ...
    #     # ... code to return computer's choice ...

    def get_game_result(self, user_item, computer_item):
    #     # ... code to determine and return game result ...
          wins_against = {"rock": "scissors", "paper": "rock", "scissors": "paper"}
          if user_item == computer_item:
              return "draw"
          elif wins_against[user_item] == computer_item:
              return "win"
          else:
              return "loss"
                

    def play(self):
        user_item = self.get_user_item()
        computer_item = self.get_computer_item()
        result = self.get_game_result(user_item, computer_item)
        
    
        print(f"user chose:  {user_item}")
        print(f"computer chose:   {computer_item}")
        print(f"result:   {result}")

        return result
        # ... code to get user and computer choices ...
        # ... code to determine game result ...
        # ... code to print game outcome ...
        # ... code to return game result ...
if __name__ == "__main__":
    Game().play()