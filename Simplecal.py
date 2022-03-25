# python simple calculator

f = int(input("Enter 1st number: "))
operator = input("choose the operator [+][-][×][÷]")
s = int(input("Enter 2nd number: "))
if operator == '+':
    print("Answer is:" , int(f) + int(s))
elif operator == '-':
    print('Answer is:' , int(f) - int(s))
elif operator == '*' or '×':
    print('Answer is:' , int(f) * int(s))
else:
    print('Answer is:' , int(f) / int(s))
