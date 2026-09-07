#import libraries
import random

#define subroutines
def usekey(a, b, c):
  global unencryptedword, encryptedword, letterlist
  for i in range(len(unencryptedword)):
    if unencryptedword[i] not in letterlist:
      print("Do not use special characters, only letters and numbers")
      return
    letter = unencryptedword[i]
    a.append(b[letter])
    encryptedword += a[0]
    a.remove(a[0])
  print(f"Your {c} phrase is : ", encryptedword)
  encryptedword = ""

def makekeys():
  global count, letterlist, checklist, encryptiondict, decryptiondict, displayencryptiondict, displaydecryptiondict
  count = 0
  while count != 63:
    count += 1
    randletter = random.randint(0, len(letterlist) - 1)
    newletter = letterlist[randletter]
    while newletter in checklist:
      randletter = random.randint(0, len(letterlist) - 1)
      newletter = letterlist[randletter]
    if newletter not in checklist:
      encryptiondict.update({letterlist[count - 1] : newletter})
      checklist.append(newletter)
  decryptiondict = {str(*encryptiondict[k]) : k for k in encryptiondict}
  displayencryptiondict = str(encryptiondict).replace("," , " |")
  displayencryptiondict = str(displayencryptiondict).replace(":" , " ->")
  displaydecryptiondict = str(decryptiondict).replace("," , " |")
  displaydecryptiondict = str(displaydecryptiondict).replace(":" , " ->")
  checklist = []

def setmode():
  global mode
  while mode != "encrypt" or mode != "decrypt":
    mode = str(input("Select mode (encrypt / decrypt) : ")).lower()
    if mode == "encrypt" or mode == "decrypt":
      break
    else:
      print("Make sure you type 'encrypt' or 'decrypt'!")

#variables, lists and dictionaries
passwordstr, encryptedword, unencryptedword, mode, commandnum = "", "", "", "", 0
letterlist, passwordlist, checklist, encryptedlist, decryptedlist = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","1","2","3","4","5","6","7","8","9","0"," ","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"], [], [], [], []
encryptiondict = {"a" : [],"b" : [],"c" : [],"d" : [],"e" : [],"f" : [],"g" : [],"h" : [],"i" : [],"j" : [],"k" : [],"l" : [],"m" : [],"n" : [],"o" : [],"p" : [],"q" : [],"r" : [],"s" : [],"t" : [],"u" : [],"v" : [],"w" : [],"x" : [],"y" : [],"z" : [],"1" : [],"2" : [],"3" : [],"4" : [],"5" : [],"6" : [],"7" : [],"8" : [],"9" : [],"0" : []," " : [],"A" : [],"B" : [],"C" : [],"D" : [],"E" : [],"F" : [],"G" : [],"H" : [],"I" : [],"J" : [],"K" : [],"L" : [],"M" : [],"N" : [],"O" : [],"P" : [],"Q" : [],"R" : [],"S" : [],"T" : [],"U" : [],"V" : [],"W" : [],"X" : [],"Y" : [],"Z" : []}

#make encryption and decryption keys
makekeys()

#setmode
setmode()

#collect input
while True:
  commandnum += 1
  if commandnum == 1:
    unencryptedword = str(input(f"What do you want {mode}ing? (type 'help' for details) : ")).lower()
  else:
    unencryptedword = str(input(f"What do you want {mode}ing? : ")).lower()
  
#carry out command (if applicable)
  if unencryptedword == "printencryptionkey":
    print("The encryption key is :", displayencryptiondict)
  elif unencryptedword == "printdecryptionkey":
    print("The decryption key is :", displaydecryptiondict)
  elif unencryptedword == "printkeys":
    print("The encryption key is :", displayencryptiondict, "\nThe decryption key is :", displaydecryptiondict)
  elif unencryptedword == "changemode":
    setmode()
  elif unencryptedword == "newkeys":
    makekeys()
  elif unencryptedword == "help":
    print("Anything you type when in 'encrypt' will be encrypted through a randomly generated key. Anything you type when in 'decrypt' will be decrypted through the same randomly generated key. You may only use letters or numbers. To stop the program, type 'stop'. To print the key being used, type 'printencryptionkey' or 'printdecryptionkey' (depending on which way round you would like the key). You can also use 'printkeys' to print both. If you wish to generate new keys, use 'newkeys'. To change mode use 'changemode'")
  elif unencryptedword == "stop":
    print("The program has terminated")
    break
  
#use key to encrypt/decrypt input
  elif mode == "encrypt":
    usekey(encryptedlist, encryptiondict, "encrypted")
  elif mode == "decrypt":
    usekey(decryptedlist, decryptiondict, "decrypted")
