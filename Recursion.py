#Q1: Write a recursive function to calculate the sum of first n natural numbers.
'''n = int(input("Enter the number to find the sum of first n natural numbers: "))
def sum(n):
    if n == 0:
        return 0
    return sum(n-1) + n
calc = sum(n)
print(calc)'''

#Q2: Write a recursive function to print all elements in a list. (Hint : use list & index as parameters.)
'''list = [1, 2, 3, 4, 5]
def print_list(list, idx=0):
    if(idx == len(list)):
        return
    print(list[idx], end="~")
    print_list(list, idx+1)
print_list(list)'''

#Q3: Write a recursive function to calculate the factorial of a number n. (n is the parameter.)
'''n = int(input("Enter the number to find the factorial: "))
def fact(n):
    if (n==0 or n==1):
        return 1
    else:
        return n*fact(n-1)
print(fact(n))'''