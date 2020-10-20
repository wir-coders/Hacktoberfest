import string

alphabet = "abcdefghijklmnopqrstuvwxyz"

def decryptCaesar(string, key):

    decryptedString = ""

    for i in string:
        position = alphabet.find(i)
        newPosition = (position - key) % 26
        decryptedString += alphabet[newPosition]
    
    return decryptedString

def encryptCaesar(string, key):

    encryptedString = ""

    for i in string:
        position = alphabet.find(i)
        newPosition = (position + key) % 26
        encryptedString += alphabet[newPosition]
    
    return encryptedString


string = "hacktoberfest"
key = 20

string = encryptCaesar(string, key)
print(f"The encrypted string is: {string}")

string = decryptCaesar(string, key)
print(f"The original string is: {string}")