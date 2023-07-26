number1=input("enter the 1st number")
number2=input("enter the 2nd number")
op=input("choose an operation:"
         "type 1 for addition"
         "type 2 for substraction"
         "type 3 for multiplication"
         "type 4 for division"
         "type 5 for raising to a power")
if float(op)==1:
    print(float(number1)+float(number2))
elif float(op)==2:
    choice=input("click A for number 1- number 2 or B for the opposite")
    if choice=="A":
        print(float(number1)-float(number2))
    elif choice=="B":
        print(float(number2)-float(number1))
elif float(op)==3:
    print(float(number1)*float(number2))
elif float(op)==4:
    choice1=input("please type C for number1/number 2 or D for the opposite")
    if choice1=="C":
        if float(number2)!=0:
            print(float(number1)//float(number2))
        elif float(number2)==0:
            print("can't devide by 0")
    elif choice1=="D":
        if float(number1)!=0:
            print(float(number2)//float(number1))
        elif float(number1)==0:
            print("can't devide by 0")
elif float(op)==5:
    choice2=input("if you want number 1 raised by number 2 type E and for the opposite type F")
    if choice2=="E":
        print(float(number1) ** float(number2))
    elif choice2=="F":
        print(float(number2) ** float(number1))