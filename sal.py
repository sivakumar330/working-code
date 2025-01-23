salary = int(input("salary:"))
age = int(input("age:"))
if(salary>=20000 or age<=25):
    loan = int(input("loan:"))
    if(loan>50000):
        print("maximum loan amount is 50000")
    else:
        print("eligible for loan")
else:
    print("not eligible for loan")
        