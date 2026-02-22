"""
GenAI-ML / Week01 / Day3 / DailyChallenge

Instructions:
- Write your solution below.
- Add tests in a __main__ block.
"""

###

word = input("Enter a word: ")

char_indexes = {}

for i in range(len(word)):
    ch = word[i]
    if ch in char_indexes:
        char_indexes[ch].append(i)
    else:
        char_indexes[ch] = [i]

print(char_indexes)

###

items_purchase = {"Water": "$1", "Bread": "$3", "TV": "$1,000", "Fertilizer": "$20"}
wallet = "$300"

wallet_amount = int(wallet.replace("$", "").replace(",", ""))

basket = []

for item in items_purchase:  
    price_str = items_purchase[item]
    price = int(price_str.replace("$", "").replace(",", ""))

    if price <= wallet_amount:
        basket.append(item)
        wallet_amount -= price

if len(basket) == 0:
    print("Nothing")
else:
    basket.sort() 
    print(basket)

###

