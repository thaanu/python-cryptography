from cryptography.fernet import Fernet
while True:
    print("Welcome to Enc")
    print("Hello, what would you like to do?")
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Make Key")
    print("4. Quit")
    option = input("Choose an option: ")
    
    # Encrypt
    if option == "1":
        kFileName = input("Enter key path: ")
        encFileName = input("Enter file path to encrypt: ")
        
        with open(kFileName+'.key', 'rb') as file:
            key = file.read()

        fernet = Fernet(key)

        with open(encFileName, 'rb') as file:
            original = file.read()

        encrypted = fernet.encrypt(original)

        with open(encFileName, 'wb') as encFile:
            encFile.write(encrypted)
        
        print("Encrypted successfully")
        
    # Decrypt
    elif option == "2":
        kFileName = input("Enter key path: ")
        decFileName = input("Enter file path to decrypt: ")
        
        with open(kFileName+'.key', 'rb') as file:
            key = file.read()

        fernet = Fernet(key)

        with open(decFileName, 'rb') as encFile:
            encStuff = encFile.read()

        decrypted = fernet.decrypt(encStuff)

        with open(decFileName, 'wb') as decFile:
            decFile.write(decrypted)
            
        print("Decrypted successfully")
    
    # Generate a key
    elif option == "3":
        kFileName = input("Enter key filename: ")
        key = Fernet.generate_key()
        with open(kFileName+'.key', 'wb') as filekey:
            filekey.write(key)
        print("Key generated successfully")
    
    # Quit
    elif option == "4":
        print("Good Bye")
        quit()
    else:
        print("Invalid option")

