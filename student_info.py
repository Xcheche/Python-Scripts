# Student information


def get_student_info(name,age,sex,nationality):
 
 info = f'{name},{age},{sex},{nationality}'
 return info
name =input('Enter name:\n')
age = int(input('Enter age:\n'))
sex =input('Enter sex:\n')
nationality =('Enter nationality:\n')

info = get_student_info(name, age,sex,nationality)
if age >= 32:
 print('Happy Birthday!')

print(info)

    