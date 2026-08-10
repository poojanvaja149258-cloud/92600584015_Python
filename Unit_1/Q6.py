#6. Write a program to illustrate the use of tuples and sets with basic operations.
Tuple = (10, 20, 30, 40, 20)
print("Tuple:", Tuple)

print("First item in tuple:", Tuple[0])

print("Count of 20 in tuple:", Tuple.count(20))

print("Index of 30 in tuple:", Tuple.index(30))

Set = {1, 2, 3, 4, 5}
print("\nInitial Set:", Set)

Set.add(6)
print("After adding 6:", Set)

Set.remove(2)
print("After removing 2:", Set)

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print("\nUnion:", A | B)

print("Intersection:", A & B)

print("Difference (A - B):", A - B)
