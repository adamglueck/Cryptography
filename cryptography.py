"""
cryptography.py
Author: Adam Glueck
Credit: Stack Overflow

Assignment:

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"
association=list(associations)
command=input("Enter e to encrypt, d to decrypt, or q to quit: ")
control=1
while control==1:
    
    if command !="e" and command !="d" and command!="q":
        print("Did not understand command, try again.")
    elif command == "e":
        words=""
        secretnmbr=[]
        nmbrkey=[]
        encryptednmbr=[]
        secret=input("message: ")
        key=input("key: ")
        keycount=len(key)
        number=len(secret)
        secret=list(secret)
        for i in range (0,number):
            secretnmbr.append(associations.find(secret[i]))
        multiply=int(1+(number/keycount))
        key=(key*(multiply+1))
        keycount=len(key)
        key=list(key)
        for i in range (0,keycount):
            nmbrkey.append(associations.find(key[i]))
        for i in range (0,number):
            encryptednmbr.append(nmbrkey[i]+secretnmbr[i])
        encryptedcount=len(encryptednmbr)
        for i in range (0, encryptedcount):
            words=words+(association[encryptednmbr[i]])
        print(words)
    
    

    elif command == "d":
        words=""
        secret=input("message: ")
        key=input("key: ")
        secretnmbr=[]
        nmbrkey=[]
        encryptednmbr=[]
        keycount=len(key)
        number=len(secret)
        secret=list(secret)
        for i in range (0,number):
            secretnmbr.append(associations.find(secret[i]))
        multiply=int(1+(number/keycount))
        key=(key*(multiply+1))
        keycount=len(key)
        key=list(key)
        for i in range (0,keycount):
            nmbrkey.append(associations.find(key[i]))
        for i in range (0,number):
            encryptednmbr.append(secretnmbr[i]-nmbrkey[i])
        encryptedcount=len(encryptednmbr)
        for i in range (0, encryptedcount):
            words=words+(association[encryptednmbr[i]])
        print(words)
    elif command == "q":
        print("Goodbye!")
        control=270
