#task 1
a=int(input("Enter an integer:"))

if(a>0):
   print("positive")
elif(a<0):
    print("negative")
else:
    print("zero")

#task 2
b=int(input("Enter first integer:"))

for i in range(1,b+1):
    if(i%2==0):
        print("Even")
    else:
        print("Odd")

#task 3
def countodd(c):
    count =0
    for i in range(1,c+1):
        if(i%2!=0):
            count+=1
    return count

c=int(input("Enter an integer:"))
print("Count of odd numbers from 1 to",c,"is",countodd(c))
