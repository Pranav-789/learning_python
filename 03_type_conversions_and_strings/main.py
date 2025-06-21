#strings and type conversion

stri = "A"
print("unicode of str as A: ", ord(stri))

character = 65
print("Character conversion from number: ", chr(character))

stringExample = "hello brother"

print(stringExample[3])
print(stringExample[-3])

print("\nConcept:String slicing")

a = "ProZero coder"
print(a[0:7:1])
print(a[8::1])

print("\nConcept:Type Conversion")

b = 12
print("Type of b: ",type(b))

b = str(b)
print("Type of b: ",type(b))

c = 13
print("Bool of c", bool(c)) 

"""
Type conversions
Explicit conversion
b  = int(b)
b = float(b)
b = bool(b)
b = str(b)
"""

#implicit conversion
print("Implicit conversion: ", (12/3), " ", type(12/3))
#automatic conversion by python
