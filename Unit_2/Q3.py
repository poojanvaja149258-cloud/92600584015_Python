# Program to generate a multiplication table using for loop
# Taking input from the user
num = int(input("Enter a number: "))

for i in range(1, 11):
    print(num, "x", i, "=", num * i)
