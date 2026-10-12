import random

random_float = random.random()
random_int = random.randint(1, 100)
random_uniform = random.uniform(10.5, 50.5)
random_step = random.randrange(2, 21, 2)

print("--- Random Module Operations ---")
print(f"Random float (0.0 to 1.0)           : {random_float}")
print(f"Random integer (1 to 100)           : {random_int}")
print(f"Random float (10.5 to 50.5)         : {random_uniform}")
print(f"Random even number (2 to 20)        : {random_step}")
