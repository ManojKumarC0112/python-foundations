#task 1
a=int(10)
b=float(0.55)
c=6
d=bool(True)
print(a)
print(b)
print(c)
print(d)
print(type(a))
print(type(b))
print(type(c))
print(type(d))


#task B
li=[1,2,3,4]
li[2]=10
print(li)

tupl=(1,2,3,4)
#tupl[1]=10
print(tupl)

print()
print()

#task C
def odd_even(num):
    if num%2==0:
        print("even")
        return
    else:
        print("odd")
        return
    
odd_even(7)
odd_even(10)


print()
#task D

try:
    num=int(input("Enter a number: "))
except ValueError:
    print("Invalid input. Please enter an integer.")