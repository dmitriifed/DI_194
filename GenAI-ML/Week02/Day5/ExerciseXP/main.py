"""
GenAI-ML / Week02 / Day5 / ExerciseXP

Instructions:
- Write your solution below.
- Add tests in a __main__ block.
"""




from anagram_checker import AnagramChecker

def get_valid_word():
    raw=input("enter a word: ").strip()
    parts = raw.split()
    if len(parts) != 1:
        print("error: single words only")
        return None
    word=parts[0]

    
    if not word.isalpha(): 
        print("error: alphabetic charachters only")
        return None
    return word


def main():
    checker = AnagramChecker("wordlist.txt")

    while True:
        choice = input(" 1 to input a word or 2 for exit").strip()
        
        if choice == "2":
            break
        
        if choice == '1':
            word = get_valid_word()
            if word is None: 
                continue
            if not checker.is_valid_word(word):
                print(f'\nYOUR WORD: "{word.upper()}"')
                print("This is NOT a valid English word.")
                continue
            anagrams = checker.get_anagrams(word)
            print(f'\nYOUR WORD: "{word.upper()}"')
            print("This is a valid English word.")

            if len(anagrams) > 0:
                  print("Anagrams for your word:", ", ".join(anagrams))
            else:
                  print("Anagrams for your word: (none found)")
            
            
        else: 
         print(" 1 to input a word or 2 for exit")
         continue






if __name__ == "__main__":
    main()
