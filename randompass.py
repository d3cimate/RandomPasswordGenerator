import string
import random
import os

try:
    purpose = input("[/\] Enter the website are you using the password for: ")
    username = input("[/\] Enter the username for the website: ")
    if os.path.exists("{0}.txt".format(purpose)) == True:
        output_file = open("{0}.txt".format(purpose), "a")
        print("[/\] {0}.txt already exists, adding onto it".format(purpose))
    elif os.path.exists("{0}.txt".format(purpose)) == False:
        output_file = open("{0}.txt".format(purpose), "w")
        print("[/\] {0}.txt does not exist and has been created".format(purpose))
    
    length = int(input("[/\] Characters for password: "))

    characters = string.ascii_letters + string.digits + string.punctuation

    password = ''

    for x in range(length):
        password += random.choice(characters)
    output_file.write("username: " + username + '\n' + "password: " + password + "\n")
    #print("[/\] Generated password is {0}".format(password))
    if os.path.exists("{0}.txt".format(purpose)) == True:
        print("[/\] {0}.txt already exists, adding onto it".format(purpose))
    print("[/\] Saved to {0}.txt".format(purpose))

except KeyboardInterrupt:
    print("\n[/\] Exit requested")