import time
start=time.time()
f=open("advent1.txt","r")
f_data=f.read()
f_lines=f_data.splitlines()
cal_sum = 0 
cal_max=0
for i in f_lines:
    if (i!=''):
        a=int(i)
        cal_sum += a
    elif (cal_max<cal_sum):
        cal_max=cal_sum
        cal_sum=0
    else:
        cal_sum=0
        continue
print(cal_max)
stop=time.time()
print(stop-start)

f.close()

