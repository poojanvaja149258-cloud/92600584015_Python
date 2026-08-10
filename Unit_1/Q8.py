#8 Write a program to explain mutable and immutable objects in Python.

print("--- List (Mutable) ---")
List = [1, 2, 3]
print("Original ID:", id(List))

List.append(4)
print("Modified ID:", id(List))  


print("\n--- Integer (Immutable) ---")
n = 10
print("Original ID:", id(n))

n = n + 5
print("Modified ID:", id(n))  
