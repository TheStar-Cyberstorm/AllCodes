# Members who worked on this from The Star group
# Abram Bender, Brian Mulhair, Bryce Ditto, Troy Chiasson
# Desc: Encrypts or decrypts strings entered by user with vigenere cypher
#       Must be run from terminal specifying encryption or decryption with
#       -e or -d respectively
# Run in Python3

import sys

# returns if an ascii value fits within the range of ascii 
# values corresponding uppercase and lowercase letters
def isLetter(char):
    return (char>=65 and char<=90) or (char>=97 and char<=122)

# Takes a string and a key and encrypts that string using viginere cyper
def encrypt(string, key):
    result = ""
    # loops through all characters in the string and adds the encrypted
    # character to the result that will be returned
    k = 0
    for i in range(len(string)):
        plain = ord(string[i])
        #if the character is a letter
        if(isLetter(plain)):
            #get the corresponding key character
            keyChar = ord(key[k])
            k+=1
            #check case on plain text character and key character
            pdiff = 0
            kdiff = 0
            if(plain <= 90):
                pdiff = 65
            else:
                pdiff = 97
            if(keyChar <= 90):
                kdiff = 65
            else:
                kdiff = 97
            #encrypt letter
            plain-=pdiff
            keyChar-=kdiff
            char=(plain+keyChar)%26+pdiff
            result+=chr(char)
        #if the character is not a letter
        else:
            result+=chr(plain)
    # return the encrypted result
    return result

# Takes a string and a key and decrypts that string using viginere cyper
def decrypt(string, key):
    result = ""
    # loops through all characters in the string and adds the decrypted
    # character to the result that will be returned
    k = 0
    for i in range(len(string)):
        plain = ord(string[i])
        #if the character is a letter
        if(isLetter(plain)):
            #get the corresponding key character
            keyChar = ord(key[k])
            k+=1
            #check case on plain text character and key character
            pdiff = 0
            kdiff = 0
            if(plain <= 90):
                pdiff = 65
            else:
                pdiff = 97
            if(keyChar <= 90):
                kdiff = 65
            else:
                kdiff = 97
            #encrypt letter
            plain-=pdiff
            keyChar-=kdiff
            char=(26+plain-keyChar)%26+pdiff
            result+=chr(char)
        #if the character is not a letter
        else:
            result+=chr(plain)
    # return the decrypted result
    return result

# get the mode and key from the system arguments
mode = sys.argv[1]
kInput = sys.argv[2]

# Remove all non letters from the key
key = ""
for i in range(len(kInput)):
    if(isLetter(ord(kInput[i]))):
        key+=kInput[i]

# check if the mode is decryption
if(mode == "-d"):
    # decrypt the user input until they exit the loop
    while(True):
        a = input("Enter text to decrypt: ")
        
        print("Decrypted text: ",decrypt(a,key))

# check if the mode is encryption
elif(mode == "-e"):
    # encrypt the user input until they exit the loop
    while(True):
        a = input("Enter text to encrypt: ")

        print("Encrypted Text: ",encrypt(a,key))
        
# In case the user entered an incorrect mode
else:
    print("No correct mode selected. Please enter a valid mode\nEncryption: -e\nDecryption: -d")
