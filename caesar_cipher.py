
def encrypt(text,s):
    result = ""
 
    # traverse text
    for i in range(len(text)):
        char = text[i]
 
        # Encrypt uppercase characters
        if (char.isupper()):
            result += chr((ord(char) + s-65) % 26 + 65)
 
        # Encrypt lowercase characters
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)
 
    return result
text = "ATTACKATONCE"
s = 4
print "Text  : " + text
print "Shift : " + str(s)
print "Cipher: " + encrypt(text,s)
https://github.com/Kotappa2000/DLithe-Internship-Report/blob/41465ad4690185d0e700a4f168bd83bc53dcf732/caesar_cipher.py