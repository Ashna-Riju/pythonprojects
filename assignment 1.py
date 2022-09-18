#Assignment :1
import re
import csv

def emailvalidation(email):
    while True:
        pat ="^[a-zA-Z][a-zA-z0-9]+@[a-zA-Z]+\.[a-z]{2,4}$"
        if re.match(pat, email):
            print("Valid Email address")
            break
        else:
           email = input("Enter valid email address : ")
           continue
    return email

def passwrdvalidation(passwd):
    SpecialSym =['$', '@', '#', '%']
    val = True
    while True:  
        if len(passwd) < 5:
            print('length should be at least 5')
            val = False
            break
          
        if len(passwd) > 16:
            print('length should be not be greater than 16')
            val = False
            break
          
        if not any(char.isdigit() for char in passwd):
            print('Password should have at least one digit')
            val = False
            break
        if not any(char.isupper() for char in passwd):
            print('Password should have at least one uppercase letter')
            val = False
            break
        if not any(char.islower() for char in passwd):
            print('Password should have at least one lowercase letter')
            val = False
            break
        if not any(char in SpecialSym for char in passwd):
            print('Password should have at least one of the symbols $@#')
            val = False
            break
        else:
            print("Valid Password")
            val = True
            break
    if val == False:
        passwd = passwrdvalidation(input("Enter a valid password : "))
    return passwd

def register():
    email = emailvalidation( input("Enter your Email address:  "))
    passwd = passwrdvalidation(input("Enter a  Password : "))
    with open ('registerfile.csv', 'a', newline='') as f:
        csv_writer = csv.writer(f)
        l =[email, passwd]
        csv_writer.writerow(l)
        f.close()
    print("You have Succesully registered")
    
def update(user, new_pass):
    f = open("registerfile.csv", "r", newline='')
    reader_obj = csv.reader(f)
    l =[]
    
    for line in reader_obj:
        if line[0] == user:
            line[1] = new_pass
        l.append(line)    
    f.close()
    
    f= open("registerfile.csv", "w+", newline='')
    writer = csv.writer(f)
    writer.writerows(l)
    
    print("The password has been updated successfully")
    f.close()

    
def login():
    user = input("Enter your email address")
    passwd =input("Enter your password")
    f = open('registerfile.csv','r')
    reader_obj = csv.reader(f)
    for line in reader_obj:
        
        c = True
        if user in line[0]:
           
            if (line[1]==passwd):
                print("you have successfully logged in")
                break
            elif(line[1]!=passwd):
                print("You entered a wrong password")
             
                choice = input("Forgot password: Yes/No")
                if choice in 'yesYes':
                    print('''Enter your choice:
                                    1. do you want to change your password
                                    2. Do you want to retrieve your orginal password ''')
                    c = int(input())
                    if c == 1:
                        new_pass =passwrdvalidation(input("Enter the new password : "))
                        update(user, new_pass)
                        break
                    if c == 2:
                        print("your password is", line[1])
                        break
                else:
                    break
        else:
            c = False
    if c == False:
        print("Please Register yourself")
            
    f.close()     

c ='Y'
while 'Y':
    print("""Enter any one option
                        1. Register
                        2. Login""")
    choice = int(input())
    if choice == 1:
        register()
    if choice == 2:
        login()
    c = input("Do you want to continue : Y/N")
    if c == 'N':
        print("Thankyou for joining with us")
        break
    
   
