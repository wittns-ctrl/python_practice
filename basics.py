print("welcome to e_calculate")

print("choose the operation of your choice:")
print("1. addition")
print("2. subtraction")
print("3. multiplication")
print("4. division")

choice = int(input("enter the choice number:"))

match choice:
    case 1:
        num1 = int(input("enter the first number:"))
        num2 = int(input("enter the second number:"))
        print(f"the sum is : {num1 + num2}")

    case 2:
        num1 = int(input("enter the first number:"))
        num2 = int(input("enter the second number:"))
        print(f"the difference is : {num1-num2}")
    case 3:
        num1 = int(input("enter the first number:"))
        num2 = int(input("enter the second number:"))
        print(f"the product is : {num1*num2}")    
    case 4:

       
        num1 = int(input("enter the first number:"))
        num2 = int(input("enter the second number:"))

        if num2 == 0:
            print("division by zero is not allowed")
        else:
         print(f"the quotient is : {num1/num2}")    