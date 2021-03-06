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
end="false"
while end=="false":
    command=input("Enter e to encrypt, d to decrypt, or q to quit: ")
    if command !="e" and command !="d" and command!="q":
        print("Did not understand command, try again.")
        end="false"
    elif command == "e":
        words=""
        secretnmbr=[]
        nmbrkey=[]
        encryptednmbr=[]
        secret=input("Message: ")
        key=input("Key: ")
        keycount=len(key)
        number=len(secret)
        secret=list(secret)
        for i in range (0,number):
            secretnmbr.append(associations.find(secret[i]))
        while len(key)<len(secret):
            key=key+key
        keycount=len(key)
        key=list(key)
        for i in range (0,keycount):
            nmbrkey.append(associations.find(key[i]))
        for i in range (0,number):
            if nmbrkey[i]+secretnmbr[i]>85:
                encryptednmbr.append(nmbrkey[i]+secretnmbr[i]-85)
            else:
                encryptednmbr.append(nmbrkey[i]+secretnmbr[i])
        encryptedcount=len(encryptednmbr)
        for i in range (0, encryptedcount):
            words=words+(association[encryptednmbr[i]])
        print(words)
        end="false"
    

    elif command == "d":
        words=""
        secret=input("Message: ")
        key=input("Key: ")
        secretnmbr=[]
        nmbrkey=[]
        encryptednmbr=[]
        keycount=len(key)
        number=len(secret)
        secret=list(secret)
        for i in range (0,number):
            secretnmbr.append(associations.find(secret[i]))
        while len(key)<len(secret):
            key=key+key
        keycount=len(key)
        key=list(key)
        for i in range (0,keycount):
            nmbrkey.append(associations.find(key[i]))
        for i in range (0,number):
            if secretnmbr[i]-nmbrkey[i]<0:
                encryptednmbr.append(secretnmbr[i]-nmbrkey[i]+85)
            else:
                encryptednmbr.append(secretnmbr[i]-nmbrkey[i])
        encryptedcount=len(encryptednmbr)
        for i in range (0, encryptedcount):
            words=words+(association[encryptednmbr[i]])
        print(words)
        end="false"
    elif command == "q":
        print("Goodbye!")
        end="true"
