# Simple Calculator with basic arithmetic operations
A = int(input("Enter Number1: "))
B = int(input("Enter Number2: "))
print("""Select operation \n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division""")
def add(A,B):
    return A+B
def sub(A,B):
    return A-B
def mul(A,B):
    return A*B
def div(A,B):
    if B != 0:
        return A / B
    else:
        return "0"
choice=int(input("Enter your choice: "))
if choice == 1:
    print("Result:",add(A,B))
elif choice == 2:
    print("Result:",sub(A,B))
elif choice == 3:
    print("Result:",mul(A,B))
elif choice == 4:
    print("Result:",div(A,B))
else:
    print("Enter correct choice")