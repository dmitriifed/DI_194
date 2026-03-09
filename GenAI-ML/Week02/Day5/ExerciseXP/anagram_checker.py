# ANAGRAM

class AnagramChecker:
    def __init__(self, word_list_path= "wordlist.txt"):
        
        self.word_set = set()
        self.word_list = []
   
        with open(word_list_path, "r", encoding="utf-8") as f:
          for line in f:
             clean = line.strip().lower()
             if clean: 
                self.word_set.add(clean)
                

    def is_valid_word(self, word): 
        clean = word.strip().lower()
        return clean in self.word_set

    
        
    def is_anagram(self, word1, word2):
       
       w1 = word1.strip().lower()
       w2 = word2.strip().lower()
       if w1 == w2:
          return False
       if len(w1) != len(w2):
          return False
       else: 
          return sorted(w1) == sorted(w2)


    def get_anagrams(self, word):
       anagrams = []
       target = word.strip().lower()
      

       for candidate in self.word_set:
            if self.is_anagram(target, candidate):
               anagrams.append(candidate)
       return sorted(anagrams)



# DEBUG 
    
if __name__ == "__main__":
    checker = AnagramChecker("wordlist.txt")
    print(len(checker.word_set))
    print(checker.is_valid_word("meat"))