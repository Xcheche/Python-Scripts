"""range.pyvowels = ['a', 'e', 'i', 'o', 'u']
for i in range(len(vowels)):
    print(vowels[i])
    """
    
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_num = []
odd_num = []
print('numbers',numbers)

for i in numbers:
    if i % 2 == 0:
        even_num.append(i)
        print('*** Even numbers ***')
        print(even_num)
    else:
        odd_num.append(i)
        print('*** Odd numbers ***')
        print(odd_num)