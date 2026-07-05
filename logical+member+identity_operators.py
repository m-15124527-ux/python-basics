# In Python, there are logical, member and identity operators.I will show all of them
logical_operators = { 
    "Logical operators"                    "Meaning"
        "and"                               "Both are true"
        "or"                                "only one is true"
        "not"                               "reverse true and false"
}  

member_operators = {
    "member operators"                      "Meaning"
         "in"                                "check if inside"
         "in not"                            "check if not inside"      
}
identity_operators = {
    "identity operators"                    "Meaning"
         "is"                               "same object"
         "is not"                           "different object"
}
#example for Logical operators
a = True
b = True
c = False
print(a and b)
print(a or c)
print(not c)
print("=========================")
#example for member operators
r = "apple"
print("a" in r)
print("k" not in r)
print("=========================")
#example for identity operators
t = ["Math"]
y = t
j = ["Math"]
print(t is y)
print(t is not j)