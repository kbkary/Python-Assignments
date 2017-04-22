while True:
    print ('Enter your age: ')
    age = input()
    if age.isdecimal():
        break
    else:
        print ('Please enter the age as a number!')

while True:
    print ('Enter your password:')
    password = input()
    if password.isalnum():
        break
    else:
        print ('Please enter password again!\n(Password contains only alphabets and numbers)')
               
print ('\n***SUCCESS***')        
    
