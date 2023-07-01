f=open("advent6.txt","r")
f_data=f.read()

def equal(num1,num2,num3,num4):
    if ((num1==num2) or (num1==num3) or(num1==num4)):
        return False
    elif ((num2==num3) or (num2==num4)):
        return False
    elif (num3==num4):
        return False
    else:
        return True

for i in range(len(f_data)-4):
    arr=[f_data[i],f_data[i+1],f_data[i+2],f_data[i+3]]
    flag=equal(arr[0],arr[1],arr[2],arr[3])
    if flag:
        print("The marker is at",i+3)
        break
f.close()