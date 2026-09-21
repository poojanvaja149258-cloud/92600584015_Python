# Program to find the sum of digits using while loop
# Taking input from the user
num = int(input("Enter a number: "))

sum = 0


while num > 0:
    digit = num % 10
    sum = sum + digit
    num = num // 10


print("Sum of digits:", sum)
