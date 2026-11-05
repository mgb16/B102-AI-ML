

#   1. Python program to check whether a number is even or odd
'''
num = int(input("Enter a number: "))
if num % 2 == 0:
    print(f"{num} is Even.")
else:
    print(f"{num} is Odd.") 
'''


#   2. Write a program to find the largest of three numbers.
'''
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

if (num1 >= num2) and (num1 >= num3):
    largest = num1
elif (num2 >= num1) and (num2 >= num3):
    largest = num2
else:
    largest = num3
print(f"The largest number is: {largest}") 
'''


#   3. choose the word that is Write a program to check whether a given number is prime.
'''
num = int(input("Enter a number: "))

if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print("Not Prime Number")
            break
    else:
        print("Prime Number")
else:
    print("Not a Prime Number")
'''


#   4. Write a program to print the Fibonacci series up to n terms.
'''
n = int(input("Enter the number of terms: "))

a = 0
b = 1
print("Fibonacci Series:")

for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c
    '''

#   5. Write a program to find the factorial of a number using a loop.
'''
num = int(input("Enter a number: "))
fact = 1

for i in range(1, num + 1):
    fact = fact * i

print("Factorial =", fact)
'''


#   6. Write a program to reverse a string without using [::-1].
'''
s = input("Enter a string: ")
rev = ""
for ch in s:
    rev = ch + rev

print("Reversed string:", rev)
'''


#   7.Write a program to check whether a string is a palindrome.
'''
s = input("Enter a string: ")

rev = ""
for ch in s:
    rev = ch + rev
if s == rev:
    print("Palindrome")
else:
    print("Not a Palindrome")
'''


#   8. Write a program to count the number of vowels and consonants in a string.
'''
s = input("Enter a string: ")
vowels = 0
consonants = 0
for ch in s:
    if ch.isalpha():
        if ch.lower() in "aeiou":
            vowels += 1
        else:
            consonants += 1

print("Vowels =", vowels)
print("Consonants =", consonants)
'''


#   9. Write a program to find the sum of all elements in a list.
'''
lst = [10, 20, 30, 40, 50]
total = 0
for i in lst:
    total = total + i
print("Sum of list elements =", total)
'''


#   10. Write a program to find the largest and smallest element in a list without using max() or min().
'''
lst = [10, 25, 5, 40, 15]
largest = lst[0]
smallest = lst[0]

for i in lst:
    if i > largest:
        largest = i
    if i < smallest:
        smallest = i

print("Largest element =", largest)
print("Smallest element =", smallest)
'''


#   11. Write a program to remove duplicate elements from a list.
'''
lst = [10, 20, 10, 30, 20, 40]

new_list = []

for i in lst:
    if i not in new_list:
        new_list.append(i)

print("List after removing duplicates:", new_list)
'''


#   12. Write a program to count how many times each element appears in a list using a dictionary.
'''
lst = [1, 2, 2, 3, 1, 2, 4]
freq = {}
for i in lst:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

print("Frequency:", freq)
'''


#   13. Write a program to find the second-largest number in a list.
'''
lst = [10, 20, 30, 40, 50]
largest = second = float('-inf')
for i in lst:
    if i > largest:
        second = largest
        largest = i
    elif largest > i > second:
        second = i

print("Second largest number:", second)
'''


#   14. Write a program to sort a list without using sort() or sorted().
'''
lst = [5, 2, 8, 1, 3]
for i in range(len(lst)):
    for j in range(i + 1, len(lst)):
        if lst[i] > lst[j]:
            lst[i], lst[j] = lst[j], lst[i]

print("Sorted list:", lst)
'''


#   15. Write a function that accepts a list of numbers and returns a list containing only the even numbers.
'''
def even_numbers(lst):
    even = []

    for i in lst:
        if i % 2 == 0:
            even.append(i)

    return even
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
print("Even numbers:", even_numbers(numbers))
'''


#   16. Write a program to find the frequency of each character in a string.
'''
s = input("Enter a string: ")
freq = {}
for ch in s:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

print("Character frequency:", freq)
'''


#   17. Write a program to check whether two strings are anagrams of each other.
'''
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

if sorted(s1.lower()) == sorted(s2.lower()):
    print("Strings are Anagrams")
else:
    print("Strings are Not Anagrams")
'''


#   18. Write a program to find all duplicate values in a list.
'''
lst = [10, 20, 30, 20, 40, 10, 50]

duplicates = []

for i in lst:
    if lst.count(i) > 1 and i not in duplicates:
        duplicates.append(i)

print("Duplicate values:", duplicates)
'''


#19.Write a program that takes a sentence and finds the longest word.sentence = input("Enter a sentence: ")
'''
words = sentence.split()
longest = ""

for word in words:
    if len(word) > len(longest):
        longest = word

print("Longest word:", longest)
'''


#   20.Create a simple student marks program that:
#   accepts marks for 5 subjects,
#   calculates the total and percentage,
#   assigns a grade,and displays whether the student passed or failed.
'''
marks = []
for i in range(5):
    m = int(input("Enter marks: "))
    marks.append(m)

total = sum(marks)
percentage = total / 5

print("Total Marks:", total)
print("Percentage:", percentage)

if min(marks) < 35:
    grade = "F"
    result = "Fail"
elif percentage >= 90:
    grade = "A"
    result = "Pass"
elif percentage >= 75:
    grade = "B"
    result = "Pass"
elif percentage >= 60:
    grade = "C"
    result = "Pass"
else:
    grade = "D"
    result = "Pass"

print("Grade:", grade)
print("Result:", result)
'''