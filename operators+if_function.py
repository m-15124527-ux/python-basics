age = 10 #This variable can be changed to test different ages
if age < 18:# this is if statement can let python decide which block of code to execute based on the condition
    print("You are a child.")
else: # this else statment will execute if the condition in the if statement is not met
    print("You are an adult.")
# there are also elif statements that can be used to check multiple conditions
# For example:
if age < 13:
    print("You are a child.")
elif age < 18:
    print("You are a teenager.")
else:
    print("You are an adult.") 
# and also there are operators that can be used in the if statement.I will show you some of them:
operators = {
    "==": "Equal to",
    "!=": "Not equal to",
    ">": "Greater than",
    "<": "Less than",
    ">=": "Greater than or equal to",
    "<=": "Less than or equal to"
}
