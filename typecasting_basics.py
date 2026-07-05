# typecasting is the process of converting one data type to another data type
# there are str(), int(), float(), bool() functions to convert data types
# there are also got the type() fuction that's tell us what type of data
# example of typecasting
v = 10
b = "string"
r = 3.14
print(type(v))
print(type(b))
print(type(r))
# converting int to str
v = str(v)
print(type(v))
# converting str to int
b = int(b)  # this will raise an error because "string" cannot be converted
# converting float to int
r = int(r)
print(type(r))
