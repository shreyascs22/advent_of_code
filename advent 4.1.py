import time
start=time.time()
f=open("advent4.txt","r")
f_data=f.read()
f_lines= f_data.splitlines()
pair_count=0
for i in f_lines:
    sep=i.strip().split(",")
    arr1=[]
    arr2=[]
    arr3=[]
    arr4=[]
    arr1.append(sep[0])
    arr2.append(sep[1])
    arr3=arr1[0].strip().split("-")
    arr4=arr2[0].strip().split("-")
    if ((int(arr4[0])>=int(arr3[0]) and int(arr4[0])<=int(arr3[1])) or (int(arr4[1])>=int(arr3[0]) and int(arr4[1])<=int(arr3[1]))):
        pair_count += 1
    elif ((int(arr3[0])>=int(arr4[0]) and int(arr3[0])<=int(arr4[1])) or (int(arr3[0])>=int(arr4[0]) and int(arr3[0])<=int(arr4[1]))):
        pair_count += 1
    else:
        continue
print(pair_count)
stop=time.time()
print(stop-start)
f.close()