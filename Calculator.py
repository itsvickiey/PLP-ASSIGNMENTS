print("Simple Calculator in python")
x=int(input("enter first no:"))
y=int(input("enter the second no:"))
operation=int(input("""Please choose the operation to be performed
                    1.Sum
                    2.Subtraction
                    3.Division 
                    4.Multiplication
"""))
print("Operation:",operation)
if  operation == 1:
   print("Sum:",x+y)
elif operation == 2:
 print("Subtraction:",x-y)
elif operation ==3:
  print("Division:",x/y)
elif operation==4:
 print("Multiplication:",x*y)
else:
 print("Please choose the valid operation")