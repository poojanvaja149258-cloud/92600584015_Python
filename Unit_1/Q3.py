#3 Write a program to perform arithmetic relational and logical operations using Python operators.

Val1 = int(input("Enter value one :"))
Val2 = int(input("Enter value two :"))

print("        Arthmetic Operation          ")
print("\n")
print(" Addition           :",Val1 + Val2)
print(" Subtraction       :",Val1 - Val2)
print(" Multiplication   :",Val1 * Val2)
print(" Division             :",Val1 / Val2)
print(" Module:",Val1 % Val2)

print("\n")

print("        relational Operation          ")
print(" Is equal to (Val1 == Val2) ",Val1 == Val2)
print(" Not equal to (Val1 != Val2) ",Val1 != Val2)
print(" Greater than (Val1  > Val2) ",Val1 > Val2)
print(" Less than (Val1  < Val2) ",Val1 < Val2)
print(" Greater or equal (Val1  >= Val2) ",Val1 >= Val2)
print(" Less or equal (Val1  <= Val2) ",Val1 <= Val2)

print("\n")
print("        Logical Operation          ")
X = True
Y = False
print(" AND Operator (X and Y) : ",X and Y)
print(" Or Operator  (X or Y) : ",X or Y)
print(" NOT Operator (not x) : ",not X)

