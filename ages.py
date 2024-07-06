ages = [10,12,13,14,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100]
above_30 = []
below_30 = []

print('Ages',ages)

for n in ages:
    if n >= 30:
        above_30.append(n)
        print('Ages above 30',above_30)

    elif ages != 30:
        below_30.append(n)
        print('Ages below 30',below_30)