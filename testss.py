class father:
    def value1(self):
        print('these is parent class')
class mother:
    def value2(self):
       print('mother class')
class son(father,mother):
    def value3(self):
        print('son class futhe')
obj=son()
#print(obj.value1())        

l=[3,4,5,1,2,3,7,3,7]
l.sort()
ele=set(l)
#print(list(ele)[-2])

# second largest number in python 
nums=[1,3,5,7,8,4,2,7,12]
#nums.remove(min(nums))
#print(min(nums))
largest=nums[0]
sec_largest=nums[0]
for i in range(len(nums)):
    if nums[i]>largest:
        largest=nums[i]
for j in range(len(nums)):
    if nums[j]>sec_largest and nums[j]!=largest :
        sec_largest=nums[j]
#print(sec_largest)        
nums.sort()
#print(nums[-2])


########################
input='3D5X6G2'
alpha=[]
digit=[]
for i in input:
    if i.isalpha():
        alpha.append(i)
    if i.isdigit():
        digit.append(i)
rel=alpha+digit
#for j in rel:
#    print(j,end='')
################ length of last word in sring #############
def lenword(s):
    sp=s.split()
    return len(sp[-1])
s="   my name is venkataramaiah   "
#print(lenword(s))

def word(s):
    s='   thatismystring   '
    count=0
    for i in s[::-1]:
        #print(i)
        if i == " ":
            if count >=1:
                return count
        else:
            count+=1
    return count        
#print(word(s))

#n=4
#for i in range(1,11):
#print(n ,'*' , i ,"=" , n * i )
#n=int(input("enter the number: "))
#rows = int(input("Enter number of rows: "))
n=6
k=0
"""for i in range(1,n+1):
    for j in range(1,(n-i)+1):
        print(end="  ")
    
    while k!=(2*i-1):
        print('* ',end="")
        k+=1
    k=0
    print()     """   


#di={"rams":23,"venkat":26,"ramudu":20}
di={'jan':100,'feb':150,'march':90,'APRIL':140}
val=list(di.values())
key=list(di.keys())
#for i in range(len(val)-1):
    #if val[i] < val[i+1]:
    #   print(key[i+1])
val.sort()
key.sort()
for k,v in zip(val,key):
    print(k,":",v)

    