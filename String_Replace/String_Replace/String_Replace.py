#1. User Input and Replace String Template “Hello <<UserName>>, How are you?”
#a. I/P -> Take User Name as Input. Ensure UserName has min 3 char
#b. Logic -> Replace <<UserName>> with the proper name
#c. O/P -> Print the String with User Name

message = "Hello User, How are you?"
print (message)
name = input('Please enter your name\n')
a = len(name)
if a > 3:
    new_message = message.replace('User', name)
    print (new_message)
else:    
    print('enter valid name, minimum 3 character')


