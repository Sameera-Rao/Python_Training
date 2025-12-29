attempts=0

while attempts<3:
    password=input("Enter password:")
    
    if len(password)<8:
        print("Password must contain atleast 8 characters.")
    elif any(char.isdigit() for char in password)==False:
        print("Password must contain atleast one number.")
    elif any(char.isupper() for char in password)==False:
        print("Password must contain atleast one uppercase letter.")
    elif any(char.islower() for char in password) == False:
        print("Password must contain atleast one lowercase letter.")
    elif any(not char.isalnum() for char in password) == False:
        print("Password must contain atleast one special character.")
    else:
        print("Password created.")
        break
    
    attempts+=1

if attempts==3:
    print("Maximum attempts reached!!Access denied.")
