import re
#Follow all the Python conventions for a variable name. It must start with a lowercase letter and only contain letters, numbers, and underscores.Not be in a list of taken usernames. taken_usernames = ['admin','admin123', 'root']● If the username doesn’t meet these requirements, print either “Invalidusername” or “Username taken” based on the context, and continue
# Need to add len() for username requiments, maybe  /.append() to username & password

sign_up = '' # creating the Variables
create_password = ''

# Creating a variable for the taken usernames
taken_usernames = ['admin', 'root', 'admin123'] 

# Creating Messages in a single bracket to save space and to add in within while loop
err_mssgs=['Username is Invalid', 'Invaild User has entered Stop','Username is Already in Use', 'Password is Invalid', 'Password needs special character', 'Password requires number', 'No Speical Characters Allowed in Username','Invalid Username: No Capital Letters Allowed', 'Password needs to be At least eight characters long','Sign up Successful','Login Sucessful','Invalid Username or Password','']

#Create while loop to start process for Login in 
while True:
    sign_up =input("Please Create Username: ") # Create input for user to see
    create_password = input("Please Create Password: ")
    if sign_up =='stop': # Create a stop point if user enters "stop"
        print(err_mssgs[1])
        continue
    if sign_up in taken_usernames: # Combing statements to make sure first test passes
            print(err_mssgs[2])
            continue
    uppercase_test = sign_up[0].isupper() # Create a condition in which if the first letter is uppercase the loop starts at the top
    if uppercase_test:
         print(err_mssgs[7])
         continue
    
    sign_up_test = bool(re.match("^[A-Za-z0-9_]*$", sign_up)) # making sure there a no specials Characters for Username
    if not sign_up_test:
         print(err_mssgs[6])
         continue
    
    password_length_test = len(create_password) >= 8 # Creating a length requirement for password
    if not password_length_test:
         print(err_mssgs[8])
         continue
    
    password_chara_test = bool(re.search("[_!?@#$^&*_-]", create_password)) # making sure the password has to have a special Character for password
    if password_chara_test != None:
         print(err_mssgs[4])
         continue
    
    
    user_name_reg = sign_up # Linking these Variables together
    password_reg = create_password 
    print(err_mssgs[9])

    id_login = input("Sign in: Please Enter user id: ")
    password_id = input("Sign in: Please Enter Password: ")
    if id_login == user_name_reg and password_id == password_reg: # Linking these Variables together and making sure they match and if they don't breaking the loop 
         print(err_mssgs[10])
         break
    else:
         print(err_mssgs[11])

    