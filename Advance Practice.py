
#******************** 1.Data Types    **************************************

#   1.Find the data type of every value in a mixed list.
'''
my_list = [2, 3.14, "Mohini", True, 5+2j, None]

for value in my_list:
    print(value, ":", type(value))
'''


#   2.Convert a nested list into a tuple of tuples.
'''
my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
result = tuple(tuple(i) for i in my_list)
print(result)
'''


#   3.Remove all duplicate values from a mixed list while preserving the original order.
'''
my_list = [10, "apple", 20, "banana", 10, "apple", 30, True]
result = []
for value in my_list:
    if value not in result:
        result.append(value)
print(result)
'''


#****************  2.Operators   **********************

#   4.Check whether a number is a power of 2 using operators.
'''
num = 33
if num > 0 and (num & (num - 1)) == 0:
    print(num, "is a power of 2")
else:
    print(num, "is not a power of 2")
'''


#   5.Swap two numbers using bitwise XOR.
'''
a = 10
b = 20

a = a ^ b
b = a ^ b
a = a ^ b

print("After swapping:")
print("a =", a)
print("b =", b)
'''


#   6.Find whether a number is divisible by both 4 and 6 using logical operators.
'''
num = 48
if num % 4 == 0 and num % 6 == 0:
    print(num, "is divisible by both 4 and 6")
else:
    print(num, "is not divisible by both 4 and 6")
'''


#   7.Calculate the total electricity bill using different unit rates.
'''
units = 250

if units <= 100:
    bill = units * 2

elif units <= 200:
    bill = (100 * 2) + (units - 100) * 3

else:
    bill = (100 * 2) + (100 * 3) + (units - 200) * 5

print("Electricity units:", units)
print("Total electricity bill: Rs.", bill)
'''


#*************  Conditional Statements  *******************

#   8.Check whether three sides can form a triangle.
'''
a = 5
b = 6
c = 7
if a + b > c and b + c > a and a + c > b:
    print("The sides can form a triangle")
else:
    print("The sides cannot form a triangle")
'''


#   9. Determine the type of triangle (Equilateral, Isosceles, Scalene).
'''
a = 3
b = 4
c = 5

if a == b and b == c:
    print("Equilateral Triangle")

elif a == b or b == c or a == c:
    print("Isosceles Triangle")

else:
    print("Scalene Triangle")
'''

#   10. Create a simple ATM menu (Withdraw, Deposit, Balance).
'''
balance = 5000

print("Welcome to ATM")
print("1. Withdraw")
print("2. Deposit")
print("3. Balance")

choice = int(input("Enter your choice: "))

if choice == 1:
    amount = int(input("Enter withdrawal amount: "))

    if amount <= balance and amount > 0:
        balance = balance - amount
        print("Withdrawal successful")
        print("Remaining balance:", balance)
    else:
        print("Insufficient balance or invalid amount")

elif choice == 2:
    amount = int(input("Enter deposit amount: "))

    if amount > 0:
        balance = balance + amount
        print("Deposit successful")
        print("Updated balance:", balance)
    else:
        print("Invalid amount")

elif choice == 3:
    print("Your balance is:", balance)

else:
    print("Invalid choice")
'''


#   11. Calculate income tax based on different tax slabs.
'''
income = 800000

if income <= 250000:
    tax = 0

elif income <= 500000:
    tax = (income - 250000) * 0.05

elif income <= 1000000:
    tax = (250000 * 0.05) + (income - 500000) * 0.20

else:
    tax = (250000 * 0.05) + (500000 * 0.20) + (income - 1000000) * 0.30

print("Annual Income:", income)
print("Income Tax:", tax)
'''


#   12. Create a menu-driven calculator using if-elif.
'''
print("Simple Calculator")

print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = int(input("Enter your choice: "))

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

if choice == 1:
    print("Addition =", a + b)

elif choice == 2:
    print("Subtraction =", a - b)

elif choice == 3:
    print("Multiplication =", a * b)

elif choice == 4:
    if b != 0:
        print("Division =", a / b)
    else:
        print("Cannot divide by zero")

else:
    print("Invalid choice")
'''


#   13. Print all prime numbers between 1 and n.
'''
n = 20
for num in range(2, n + 1):
    count = 0

    for i in range(1, num + 1):
        if num % i == 0:
            count = count + 1

    if count == 2:
        print(num, end=" ")
'''


#   14. Find the factorial of a number using a loop.
'''
num = 5
fact = 1

for i in range(1, num + 1):
    fact = fact * i

print("Factorial =", fact)
'''


#   15. Print the Fibonacci series up to n terms
'''
n = 10

a = 0
b = 1

for i in range(n):
    print(a, end=" ")

    c = a + b
    a = b
    b = c
    '''

#   16. Check whether a number is an Armstrong number.
'''
num = 153

temp = num
digits = len(str(num))
total = 0

while temp > 0:
    digit = temp % 10
    total = total + digit ** digits
    temp = temp // 10

if total == num:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")
'''


#   17. Reverse a number and check if it is a palindrome.
'''
num = 121

temp = num
rev = 0

while temp > 0:
    digit = temp % 10
    rev = rev * 10 + digit
    temp = temp // 10

print("Reversed number:", rev)

if num == rev:
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")
'''


#   18. Find the Greatest Common Divisor (GCD) of two numbers
'''
a = 12
b = 18

while b != 0:
    temp = b
    b = a % b
    a = temp

print("GCD =", a)
'''


#   19. Write a function to check if a string is a palindrome
'''
def palindrome(s):
    if s == s[::-1]:
        print("Palindrome")
    else:
        print("Not Palindrome")

word = "Wisdoms"
palindrome(word)
'''


 #  20. Write a function to count vowels and consonants in a string                  
'''
def count_letters(s):
    vowels = 0
    consonants = 0

    for ch in s:
        if ch.isalpha():
            if ch.lower() in "aeiou":
                vowels += 1
            else:
                consonants += 1

    print("Vowels:", vowels)
    print("Consonants:", consonants)


text = "Hello World"
count_letters(text)
'''


#   21. Create a function to calculate simple and compound interest
'''
def interest(p, r, t):
    si = (p * r * t) / 100

    amount = p * (1 + r / 100) ** t
    ci = amount - p

    print("Simple Interest:", si)
    print("Compound Interest:", ci)

p = 10000
r = 5
t = 2

interest(p, r, t)
'''


#   22. Write a function to return all factors of a number
'''
def factors(num):
    result = []

    for i in range(1, num + 1):
        if num % i == 0:
            result.append(i)

    return result
n = 12
print("Factors:", factors(n))
'''


#   23. Write a function to find the second-largest number in a list
'''
def second_largest(lst):
    unique = list(set(lst))

    if len(unique) < 2:
        return "Second largest does not exist"

    unique.sort()

    return unique[-2]

numbers = [10, 20, 30, 40, 50]

print("Second largest:", second_largest(numbers))
'''


#******************************   6.Lists  *****************************************
#   24. Merge two lists without duplicates.
'''
list1 = [10, 20, 30, 40]
list2 = [30, 40, 50, 60]

result = []

for i in list1 + list2:
    if i not in result:
        result.append(i)

print("Merged list:", result)
'''


#   25. Find the second-largest and second-smallest elements
'''
numbers = [10, 20, 30, 40, 50]

unique = list(set(numbers))
unique.sort()

if len(unique) >= 2:
    print("Second smallest:", unique[1])
    print("Second largest:", unique[-2])
else:
    print("Not enough distinct elements")
'''


#   26. Rotate a list to the left by k positions
'''
numbers = [1, 2, 3, 4, 5]
k = 2
k = k % len(numbers)
result = numbers[k:] + numbers[:k]
print("Rotated list:", result)
'''


#   27. Separate even and odd numbers into two lists
'''
numbers = [10, 15, 20, 25, 30, 35, 40]

even = []
odd = []
for i in numbers:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

print("Even numbers:", even)
print("Odd numbers:", odd)
'''


#   28. Find the common elements between two lists
'''
list1 = [10, 20, 30, 40, 50]
list2 = [30, 40, 50, 60, 70]

common = []

for i in list1:
    if i in list2 and i not in common:
        common.append(i)

print("Common elements:", common)
'''

#*********************   Tuples and Sets    ************************

#   29. Count the frequency of each element in a tuple
'''
t = (10, 20, 10, 30, 20, 10, 40)

for i in set(t):
    print(i, "appears", t.count(i), "times")
'''


#   30. Find the union, intersection, and difference of two sets
'''
A = {10, 20, 30, 40}
B = {30, 40, 50, 60}

print("Union:", A.union(B))
print("Intersection:", A.intersection(B))
print("Difference:", A.difference(B))
'''


#   31. Check whether one set is a subset of another

A = {10, 20}
B = {10, 20, 30, 40, 50}

if A.issubset(B):
    print("A is a subset of B")
else:
    print("A is not a subset of B")