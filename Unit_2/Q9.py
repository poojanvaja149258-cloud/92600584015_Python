# Program to demonstrate iterators and iterables
# Creating an iterable
numbers = [10, 20, 30, 40, 50]

print("Iterable:", numbers)

iterator = iter(numbers)

print("\nIterator elements:")
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
