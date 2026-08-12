#10. Write a program to demonstrate recursion using factorial or Fibonacci series.

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
number = int(input("Enter a number: "))

result = factorial(number)
print(f"The factorial of  is {result}")

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)

terms = int(input("Enter number of terms: "))
for i in range(terms):
    print(fibonacci(i), end=" ")
