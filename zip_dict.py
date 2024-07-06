# matric_no = ['001','002','003','004','005','006','007','008','009','010']
# student_name = ['Edu','Helen','Chike','Chike','Chike','Chike','Chike','Chike','Chike','Chike']
# student_admission_info = dict(zip(matric_no,student_name))

# print(student_admission_info)
# step2


# matric_no = ['001','002','003','004','005','006','007','008','009','010']
# student_name = ['Edu','Helen','Chike','Chike','Chike','Chike','Chike','Chike','Chike','Chike']
# student_admission_info ={}

# for key,value in zip(matric_no,student_name):
#     student_admission_info[key] = value
# print(student_admission_info)

#step3
matric_no = ['001','002','003','004','005','006','007','008','009','010']
student_name = ['Edu','Helen','Chike','Chike','Chike','Chike','Chike','Chike','Chike','Chike']
student_admission_info ={}

for m,s in zip(matric_no,student_name):
    student_admission_info[m]=s

print(student_admission_info)