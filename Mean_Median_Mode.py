from statistics import mode
from math import sqrt



# finding mean median mode and standard deviation
#mean 
data=[40,41,45,60,40,52,46,40,50,50,50,50] # enter the data...
n=len(data)
sum=0

for x in data:
    sum+=x
mean =sum/n
print("Mean of the data ",mean)





# meadian
#for meadian we have to sort the data 
data.sort()
print("sorted data")

for x in data:
    print(x)

if n%2==0:
    m1=data[n//2]
    m2= data[(n//2) -1]
    median= (m1+m2)/2
else:
    median=data[n//2]

print("median of data",median)





# standerd deviation
#squrt(sum of (data-mean )**2)/n-1
sum =0
if x in data:
    sum +=(x-mean)**2
standard_deviation=sqrt(sum/(n-1))
print("standard deviation of data",standard_deviation)





# # mode of data
#(using statistic library)
data_mode= mode(data)
print("mode of data",data_mode)





# mode of data
single_data=[]
repeated_data =[]

for x in data:
    if x not in single_data:
        single_data.append(x)
    else:
        repeated_data.append(x)
mode_data= set(repeated_data)
print(mode_data)
count=0 
addcount=[]

for i in mode_data:
    for x in data:
        if i==x:
            count+=1
    addcount.append(count)
    count=0
print(addcount)

for x in addcount:
    for i in range (0,len(addcount)):
        if x<=addcount[i]:
            result = i

print("mode of data",list(mode_data)[result])


