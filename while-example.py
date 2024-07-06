# counter = 0
# while counter <10:
#     print(counter)
#     counter += 2

age = input('Enter your age: ')
age = int(age)
if age >= 18:
    print('You can vote')
elif age == 17:
    print('You can not vote yet')
    print('You are almost approaching the age of voting')
elif age == 16:
    print('You are too young to vote')
else:
    print(f'You are just  {age} , you are too young to vote')