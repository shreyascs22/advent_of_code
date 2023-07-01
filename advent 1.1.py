import time
start=time.time()
f=open("advent1.txt","r")
f_data=f.read()
f_lines=f_data.splitlines()
cal_sum = 0 
arr_sum=[]
for i in f_lines:
   if (i==''):
      arr_sum.append(cal_sum)
      cal_sum=0
   else:
      cal_sum += int(i)
arr_sum.sort()
sum_three=arr_sum[-1]+arr_sum[-2]+arr_sum[-3]
print(sum_three)
stop=time.time()
print(stop-start)

f.close()
