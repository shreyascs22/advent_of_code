f=open("advent6.txt","r")
f_data=f.read()
for i in range(len(f_data)-14):
    arr=[]
    arr.extend(f_data[i:i+14])
    print(set(arr))
    if (len(set(arr))==len(arr)):
        print(i+15)
        break
f.close()