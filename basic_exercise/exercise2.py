multiplier = 20


my_list = [1, 2, 3, 4]
multiplied_list = [x * multiplier for x in my_list]
names_list = ["Elie", "Tim", "Matt"]
other_list = [1,2,3,4,5,6]
string_first = "first"
string_third = "third"
common_string = []
list_1_to_100 = list(range(1, 101))
divided_list = [x for x in list_1_to_100 if x % 12 == 0]
amazing_string = "amazing"
vowels = "aeiouy"
no_vowels_in_amzing_string = [ch for ch in amazing_string if ch not in vowels]
thriple_list = [list_1_to_100[i:i + 3] for i in range(0, len(list_1_to_100), 3)][:3]
ten_by_ten_list = [[x for x in range(i, i + 10)] for i in range(0, 101, 10)][:10]
grid = [[x % 10 for x in range(i, i + 10)] for i in range(0, 100, 10)] 

# 3-layer
tuner = int(3)
tunable_list = [x for x in range(tuner)]
tunable_grid = [[tunable_list for x in range(tuner)] for y in range(tuner)] #didnt work 

# simple grid
n = 5
simple_grid = [list(range(n)) for _ in range(n)]


# increasing grid
n = 5
increasing_grid = [list(range(i+1)) for i in range(n+1)]

# everencreasig grid
x = 5
everincreasing_grid = [list(range(i+1)) for i in range(x*x+1)]


print(my_list) # 1
print(multiplied_list) # 2
print([name[0] for name in names_list]) # 3
print([x for x in other_list if x % 3 == 0]) # 4
print(([x for x in other_list if x % 2 == 1]) + ([x for x in other_list if x % 2 == 0])) # 5
print([name[::-1].lower() for name in names_list]) # 6
print([ch for ch in (string_first + string_third)]) # 7
for ch in string_first: 
    if ch in string_third and ch not in common_string:
        common_string.append(ch)
print(common_string) # 8
print(divided_list) # 9
print(no_vowels_in_amzing_string) # 10
print(thriple_list) # 11
print(ten_by_ten_list) # 12
print(grid) # 13
print([grid[i][9] for i in range(len(grid))]) # 14
print(tunable_grid) # 15




print(simple_grid)

print(increasing_grid)

print(everincreasing_grid)