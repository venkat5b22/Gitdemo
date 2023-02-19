my_list = [3,1,9,5,2,0,4,6]
new_list = []

while my_list:
    min = my_list[0]  
    for x in my_list: 
        if x < min:
            min = x
    new_list.append(min)
    my_list.remove(min)    

print(new_list)



l = [64, 25, 12, 22, 11, 1,2,44,3,122, 23, 34]
for i in range(len(l)):
    #print(l[i])
    for j in range(i+1,len(l)):
        if l[i] < l[j]:
            l[i],l[j] =l[j],l[i]
#print(l)            


##########################################