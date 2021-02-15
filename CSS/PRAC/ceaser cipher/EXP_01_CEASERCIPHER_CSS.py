# NAME: TAUSEEF MUSHTAQUE ALI SHAIKH
# ROLL NO: 18CO63	CALSS: TE-CO
# EXPERIMENT NO. 01: IMPLEMENTATION OF CAESERCIPHER

def caesarCipher(message,key):
    cipher = "" 
 
    for i in range(len(message)): 
        char = message[i] 
       
        if (char.isupper()): 
            cipher += chr((ord(char) + key-65) % 26 + 65) 
        
        else: 
            cipher += chr((ord(char) + key - 97) % 26 + 97) 
  
    return cipher

print("")   
print("ENCRYPTION USING CaesarCipher")
print("")

msg = input("ENTER MESSAGE FOR ENCRYPTION: ")
print("")

key = int(input("ENTER KEY: "))
print("")

print("ENCRYPTED TEXT: ", caesarCipher(msg,key))