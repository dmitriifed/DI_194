"""
GenAI-ML / Week02 / Day2 / DailyChallenge

Instructions:
- Write your solution below.
- Add tests in a __main__ block.
"""
import math

class Pagination:
    def __init__ (self, items=None, page_size=10):
        if items == None:
           items = []
        if page_size <= 0:
            raise ValueError("page_size must be >= 1")
        
        self.items = items
        self.page_size = page_size
        self.current_idx = 0
    
        self.total_pages = math.ceil(len(self.items) / self.page_size)

    def get_visible_items(self, current_index, page_size):
        self.cuttent_index = current_index
        self.page_size = page_size

        

p = Pagination([1,2,3,4,5], page_size=2)
print(p.total_pages)  
print(p.current_idx)


# def main():
#     pass

# if __name__ == "__main__":
#     main()
