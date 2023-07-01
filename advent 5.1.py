arr=[['G','D','V','Z','J','S','B'],
     ['Z','S','M','G','V','P'],
     ['C','L','B','S','W','T','Q','F'],
     ['H','J','G','W','M','R','V','Q'],
     ['C','L','S','N','F','M','D'],
     ['R','G','C','D'],
     ['H','G','T','R','J','D','S','Q'],
     ['P','F','V'],
     ['D','R','S','T','J']]

f=open("advent5.txt","r")
f_data=f.read()
f_lines= f_data.splitlines()
arr_waste=[]
#print(f_lines)
for i in f_lines:
    split=i.split(" ")
    number_of_boxes=int(split[1])
    box_from=int(split[3])-1
    box_to=int(split[5])-1

    arr[box_to].extend(arr[box_from][-(number_of_boxes):])
    for j in range(number_of_boxes):
        arr_waste=arr[box_from].pop()
    #alt method - change the array directly itself by sicing arr=arr[box_from-1][:len(arr[box_from-1])-number_of_boxes]
print(arr)
f.close()