# Fuction is a Block of statements that perform a specific task.

#Q1: WAF to print the length of a list. ( list is the parameter)
'''list = []
list.append(int(input("Enter the first element in the list: ")))
list.append(int(input("Enter the second element in the list: ")))
list.append(int(input("Enter the third element in the list: ")))
list.append(int(input("Enter the fourth element in the list: ")))
def L_of_list(list):
    print(len(list))
L_of_list(list)'''

#Q2: WAF to print the elements of a list in a single line. ( list is the parameter)
'''list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def print_list(list):
    for i in list:
        print(i, end=" ")
print_list(list)'''

#Q3: WAF to find the factorial of n. (n is the parameter)
'''n = int(input("Enter the number to find the factorial: "))
def factorial_of_n(n):
    factorial = 1
    for i in range(1, n+1):
        factorial *= i
    print(f"The factorial of {n} is: {factorial}")
factorial_of_n(n)'''

#Q4: WAF to convert USD to INR.
'''usd = float(input("Enter the amount in USD: "))
def usd_to_inr(usd):
    inr = usd * 82.74
    print(f"{usd} USD is equal to {inr} INR.")
usd_to_inr(usd)'''