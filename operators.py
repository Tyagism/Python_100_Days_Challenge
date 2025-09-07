# here a and b have been defined
# using add operator (+) we added a & b values and stored it in c.

a = 5
b = 10
c = a+b
print(c)

# here we are using the augmented assignment operator (+=)
# it adds the right operand to the left operand and assigns the result to the left operand.

b += 3
print(b)

# now we are using the updated value of b i.e., 10+3 = 13
# # so the new value of c will be 5 + 13 = 18

c = a+b
print(c)

# now we use decrement operator (-=)
b -= 2
print(b)

# now we use multiplication operator (*=)
c *= 2
print(c)

# now we use division operator (/=)
print(b)
b /= 2
print(b)
# now we use floor division operator (//=)
c //= 3 # it gives the quotient value after division
print(c)

# now we use comparion operators
print(a==b) # it checks if a is equal to b or not
print(a!=b) # it checks if a is not equal to b
print(a>b)  # it checks if a is greater than b or not
print(a<b)  # it checks if a is less than b or not
print(a>=b) # it checks if a is greater than or equal to b
print(a<=b) # it checks if a is less than or equal to b

d = 3.14519
print(d==a)  # it checks if d is greater than a or not
print(type(d)) # it tells the datatype of d

print("now we use logical operators")
print(a>3 and b>10, print(a,b,c), print(a==b and b==c)) # it returns true if both the conditions are true
print(d==print(c))

# This is a Truth Table for OR Operator
print("true or false:", True or False)
print("False or false:", False or False)
print("true or True:", True or True)
print("False or true:", False or True)

# This is a Truth Table for and Operator
print("true and false:", True and False)
print("False and false:", False and False)
print("true and True:", True and True)
print("False and true:", False and True)
