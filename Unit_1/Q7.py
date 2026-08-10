#7. Write a program to create a dictionary and demonstrate dictionary methods and iteration.

Dict = {1:"RED",
             2:"BLUE",
             "BLACK":3}

print(Dict[1])
print(Dict[2])
print(Dict["BLACK"])

print(Dict.get("RED"))

Dict["Yellow"] = 3 
print(Dict)

Dict.pop("BLACK")
print(Dict)

for name, score in Dict.items():
    print(f"{name} scored {score}")
