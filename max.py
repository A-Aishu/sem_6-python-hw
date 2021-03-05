num1 = 10
num2 = 14
num3 = 12
if (num1 >= num2) and (num1 >= num3):
   maximum = num1
elif (num2 >= num1) and (num2 >= num3):
   maximum = num2
else:
   maximum = num3

print("The maximum number is", maximum)
