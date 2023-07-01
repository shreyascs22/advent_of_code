f=open("advent2.txt","r")
f_data=f.read()
f_lines=f_data.splitlines()
points=0
for i in f_lines:
    if (i[0]=='A'):
        if (i[2]=='X'):
            points += 3 #3
        elif (i[2]=='Y'):
            points += 4 #4
        else:
            points +=8 #8
    elif (i[0]=='B'):
        if (i[2]=='X'):
            points += 1
        elif (i[2]=='Y'):
            points += 5
        else:
            points +=9
    elif (i[0] =='C'):
        if (i[2]=='X'):
            points += 2 #2
        elif (i[2]=='Y'):
            points += 6 #6
        else:
            points +=7 #7
print(points)
f.close()