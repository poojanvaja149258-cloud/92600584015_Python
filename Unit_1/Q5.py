#5. Write a program to create and manipulate lists using indexing slicing and list comprehensions.

n = [10, 20, 30, 40, 50, 60]
print("Original list                       :", n)

print("First item (index 0)           :", n[0])
print("Last item (index -1)          :", n[-1])

print("First 3 items                      :", n[0:3])
print("Items from index 3 to end :", n[3:])
print("Reversed list                     :", n[::-1])

s = [x * x for x in n]
print("Squares of all numbers     :", s)
