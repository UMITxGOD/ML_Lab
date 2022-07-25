def swap(*value):
    temp=value[0] 
    value[0]=value[1]
    value[1]=temp
    print("x",value[0])
    print("y",value[1])

x = int (input("Enter 1st Number : "))
y= int (input("Enter 2st Number : ")) 

print("After Swapping ")

swap(50,95)
