"""
cryptography.py
Author: <your name here>
Credit: <list sources used, if any>

Assignment:

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"

command=input("Enter e to encrypt, d to decrypt, or q to quit: ")
if command !="e" and command !="d" and command!="q":
    print("Did not understand command, try again.")
elif command == "e":
    secret=input("message")
    key=input("key")
elif command == "d":
    secret=input("message")
    key=input("key")
elif command == "q":
    print("Goodbye!")
print(associations.find("e"))
