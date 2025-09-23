while True:
    num1 = float(input("Enter 1st number:"))
    num2 = float(input("Enter 2nd number:"))
    opr = input("Enter the operator:")
    if opr == '+':
        print(num1, ' + ' , num2, " = " , num1+num2, "\n") 

    elif opr == '-':
        print(num1, ' - ' , num2, " = " , num1-num2, "\n")
        
    elif opr == '*':
        print(num1, ' * ' , num2, " = " , num1*num2, "\n")

    elif opr == '/':
        print(num1, ' / ' , num2, " = " , num1/num2, "\n") 

    else :
        print("Please Enter a valid oprator! \n ")

    if not(1 < 5):
        break 
