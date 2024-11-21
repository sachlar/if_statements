# if statements
# examine state and decide what to do

cars = ['bmw', 'jaguar', 'ford', 'audi', 'mercedes']

for car in cars:
    if car == "bmw":
        print(car.upper())
    else:
        print(car.title())

# checking if something is in or not in a list
# use 'in' or 'not in'

banned_drivers =['jon', 'bruce', 'karol', 'pete']
driver = 'adam'
if driver in banned_drivers:
    print(f"you are not allowed to drive {driver}.")
else:
    print(f"you are allowed to drive {driver}.")

# check booleans

game_active = True
can_edit = False

# if elif and else
age = 12
if age <= 12:
    print("your ticket is free")
elif age < 18: # you can use lots of elif's to check lots of conditions
    print("your ticket is £25")
else:
    print("your ticket is £40")

# users
users_names = ['bob', 'jon', 'may', 'ann', 'admin']
for n in users_names:
    if n == 'admin':
        print(f"welcome to the game {n} what do you want to do.")
    else:
        print(f"welcome to the game {n} lets play.")

users_names_2 = []
if users_names_2:
    for n in users_names_2:
        print(f"hello {n}")
else:
    print("we need to add some user names")

current_users = ['bob', 'jon', 'may', 'ann', 'admin']
new_users = ['tom', 'dick', 'harry', 'jon', 'ann']
new_users_lower = [name.lower() for name in new_users]
for new_user in new_users_lower:
    if new_user in current_users:
        print(f"username {new_user} is taken, you need to choose another username.")
    else:
        print(f"{new_user} is available to use as your username.")

# ordinal numbers

numbers = list(range(1,10)) 
for number in numbers:
    if number == 1:
        print(f"{number}st")
    elif number == 2:
        print(f"{number}nd")
    elif number == 3:
        print(f"{number}rd")
    else:
        print(f"{number}th")

