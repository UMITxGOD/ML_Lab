number = int (input("Enter Number : "))
temp=number
number_oprator = int (input("Enter Number Operator : "))
number+=3

print("Adding Number By ",number_oprator,", Number become",number)
number=temp
number*=3

print("Multipying Number By ",number_oprator,", Number become",number)

number=temp
number/=3

print("Dividing Number By ",number_oprator,", Number become",number)
number=temp
number%=3

print("Modulo Number By ",number_oprator,", Number become",number)
