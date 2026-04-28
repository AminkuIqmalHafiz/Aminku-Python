BOLD = '\033[1m'
END = '\033[0m'
RED = '\033[31m'

def substract (a,b): return a - b
def multiply (a,b): return a * b
def addtion (a,b): return a + b
def division(a,b): 
    try:
        return a/b
    except ZeroDivisionError:
        print(f'{BOLD}{RED}Please number other than 0 for division.{END}')

while True:    
    print (f"{BOLD}Welcome to CLI Calculator{END}")

    try:
        Num1 = float(input(f"{BOLD}Insert Number 1: {END}"))
        Num2 = float(input(f"{BOLD}Insert Number 2: {END}"))
    except ValueError:
        print(f'{BOLD}{RED}Please insert integer or float number only.{END}')
        continue
    
        
    choice = input(f"{BOLD}What calc? (+, -, *, /): {END}")
    if choice == '+':
        print(f"Answer: {addtion(Num1, Num2)}")
    elif choice == '-':
        print(f"Answer: {substract(Num1, Num2)}")
    elif choice == '*':
        print(f"Answer: {multiply(Num1, Num2)}")
    elif choice == '/':
        print(f"Answer: {division(Num1, Num2)}")

    cancel = input(f"{BOLD}{RED}Do you wish to end? (Y/N): {END}")
    if cancel == 'Y':
        print (f"{BOLD}Initiating exit. Exiting....{END}")
        break
    elif cancel == 'N':
        print (f"{BOLD}Generating new calculation...{END}")
    else:
        print(f'{BOLD}{RED}Please insert Y or N number only.{END}')





