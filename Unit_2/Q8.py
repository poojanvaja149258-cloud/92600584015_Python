# Program to demonstrate local, global and nonlocal variables
# Global variable
x = 10
def outer_function():
   
    y = 20

    def inner_function():
        
        z = 30

        print("Global variable:", x)
        print("Nonlocal variable:", y)
        print("Local variable:", z)

    inner_function()
    
outer_function()
