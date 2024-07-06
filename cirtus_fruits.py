# fruits = ['mango','guava','pawpaw','orange','lemon']
# citrus_fruit = []

# for fruit in fruits:
#     if fruit == 'orange':
#         citrus_fruit.append(fruit)
#         print('citrus_fruit',citrus_fruit)
#     elif fruit == 'lemon':
#         citrus_fruit.append(fruit)
#         print('citrus_fruit',citrus_fruit)
#     else:
#         print(fruit)

# student_scores = [10,20,30,40,50,60,70]
# scores_above_40 = []

# for scores in student_scores:
#     if scores >=40:
#         scores_above_40.append(scores)
#         print(scores_above_40)
       

my_numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
even_num = []
odd_num= []

for n in my_numbers:
    if n %2 ==0:
        even_num.append(n)
      
    elif n %2 !=0:
        odd_num.append(n)
print('odd_num',odd_num)
print('even_num',even_num)