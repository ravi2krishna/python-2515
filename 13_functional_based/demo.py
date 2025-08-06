# Without Functions
a = 10
b = 11
print(a+b)
print(a-b)
print(a*b)
print(a/b)

a = 12
b = 13
print(a+b)
print(a-b)
print(a*b)
print(a/b)

a = 20
b = 30
print(a+b)
print(a-b)
print(a*b)
print(a/b)

print("With Functions")

# With Functions
a = 30
b = 40
def arithmetic():
    print(a+b)
    print(a-b)
    print(a*b)
    print(a/b)

arithmetic() 

a = 40
b = 50
arithmetic() 

a = 50
b = 60
arithmetic() 

a = 70
b = 80
arithmetic() 

print("With Parameters")

# functions with parameters
def arithmetic(a,b):
    print(a+b)
    print(a-b)
    print(a*b)
    print(a/b)
    print(a)
    print(b)
# arithmetic() -> TypeError: arithmetic() missing 2 required positional arguments: 'a' and 'b'
# arithmetic(40) -> TypeError: arithmetic() missing 1 required positional argument: 'b'
arithmetic(10,20)
arithmetic(20,30)
arithmetic(30,40)
# Parameters defined are local to function, cannot be accessed 
# out side the function
# print(a)
# print(b)

# a & b -> parameters
# 10 & 20 -> arguments

# functions with parameters -> Positional Arguments
def arithmetic(a,b):
    print(a+b)
    print(a-b)
    print(a*b)
    print(a/b)
arithmetic(10,20)
arithmetic(20,10)

# functions with parameters -> Positional Arguments
def login(username,password):
    if username == "ravi" and password == "pass123":
        print("Login Success")
    else:
        print("Login Failed")
# login()
# login("ravi")
# login("ravi","pass")
# login("ravi","pass123") -> Correct 
login("pass123","ravi")
