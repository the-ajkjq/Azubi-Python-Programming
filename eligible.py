name = input("Enter your name: ")
age = input("Enter your age: ")

try:  
    if int(age) >= 18:
        print("You are eligible, " + name)
    else:
        print("You are too young")
except: 
    print("Unsupported format")