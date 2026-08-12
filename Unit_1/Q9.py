#9. Write a program to define and use user-defined functions with different types of arguments.

def Positional(name, age):
    print("Hello", name, "you are", age, "years old.")

def Default(name="Guest"):
    print("Welcome,", name)

def Keyword(player, score):
    print(player, "scored", score, "points.")

def Arbitrary(*numbers):
    print("Total sum is:", sum(numbers))

print("--- 1. Positional ---")
Positional("Alice", 21)

print("\n--- 2. Default ---")
Default()          
Default("Bob")

print("\n--- 3. Keyword ---")
Keyword(score=95, player="Charlie")

print("\n--- 4. Arbitrary ---")
Arbitrary(5, 10, 15)
