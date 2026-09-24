# libraries
import random

# subroutines
# encrypt / decrypt plaintext
def usekey(plaintext, cryptiondict, mode):
  global letterlist
  cryptedword = ""
  for i in range(len(plaintext)):
    if plaintext[i] not in letterlist:
      print("Do not use special characters, only letters and numbers")
      return
    letter = plaintext[i]
    cryptedword += str(cryptiondict[letter])
  print(f"Your {mode}ed phrase is : ", cryptedword)

# generate an encryption key and flip to produce decryption key
def makekeys():
  global letterlist, encryptiondict
  checklist = []
  count = 0
  while count != len(letterlist):
    count += 1
    randletter = random.randint(0, len(letterlist) - 1)
    newletter = letterlist[randletter]
    while newletter in checklist:
      randletter = random.randint(0, len(letterlist) - 1)
      newletter = letterlist[randletter]
    if newletter not in checklist:
      encryptiondict.update({letterlist[count - 1] : newletter})
      checklist.append(newletter)
  decryptiondict = {}
  dictkeys = list(encryptiondict.keys())
  for key in dictkeys:
    decryptiondict[encryptiondict[key]] = key
  return decryptiondict

# determine whether encrypting or decrypting
def setmode():
  while True:
    mode = str(input("Select mode (encrypt / decrypt) : ")).lower()
    if mode == "encrypt" or mode == "decrypt":
      return mode
    else:
      print("Make sure you type 'encrypt' or 'decrypt'!")

# variables
plaintext = ""
firstcommand = True
letterlist = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u",
              "v","w","x","y","z","1","2","3","4","5","6","7","8","9","0"," ","A","B","C","D","E",
              "F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
encryptiondict = {"a" : [],"b" : [],"c" : [],"d" : [],"e" : [],"f" : [],"g" : [],
                  "h" : [],"i" : [],"j" : [],"k" : [],"l" : [],"m" : [],"n" : [],
                  "o" : [],"p" : [],"q" : [],"r" : [],"s" : [],"t" : [],"u" : [],
                  "v" : [],"w" : [],"x" : [],"y" : [],"z" : [],"1" : [],"2" : [],
                  "3" : [],"4" : [],"5" : [],"6" : [],"7" : [],"8" : [],"9" : [],
                  "0" : []," " : [],"A" : [],"B" : [],"C" : [],"D" : [],"E" : [],
                  "F" : [],"G" : [],"H" : [],"I" : [],"J" : [],"K" : [],"L" : [],
                  "M" : [],"N" : [],"O" : [],"P" : [],"Q" : [],"R" : [],"S" : [],
                  "T" : [],"U" : [],"V" : [],"W" : [],"X" : [],"Y" : [],"Z" : []}

# make keys and get mode from user
decryptiondict = makekeys()
mode = setmode()

# repeat until stop command is issued
while True:
  # collect data to be encrypted / decrypted or commands
  if firstcommand:
    plaintext = str(input(f"What do you want {mode}ing? (type 'help' for details) : "))
    firstcommand = False
  else:
    plaintext = str(input(f"What do you want {mode}ing? : "))
  
  # carry out command (if applicable) or encrypt / decrypt data
  match plaintext.lower():
    case "printencryptionkey":
      print("The encryption key is :", str(encryptiondict).replace("," , " |").replace(":" , " ->"))
    case "printdecryptionkey":
      print("The decryption key is :", str(decryptiondict).replace("," , " |").replace(":" , " ->"))
    case "printkeys":
      print("The encryption key is :", str(encryptiondict).replace("," , " |").replace(":" , " ->"), 
            "\nThe decryption key is :", str(decryptiondict).replace("," , " |").replace(":" , " ->"))
    case "changemode":
      mode = setmode()
    case "newkeys":
      decryptiondict = makekeys()
    case "help":
      print("Anything you type when in 'encrypt' will be encrypted through a randomly generated key. Anything you type when in 'decrypt' will be decrypted through the same randomly generated key. You may only use letters or numbers. To stop the program, type 'stop'. To print the key being used, type 'printencryptionkey' or 'printdecryptionkey' (depending on which way round you would like the key). You can also use 'printkeys' to print both. If you wish to generate new keys, use 'newkeys'. To change mode use 'changemode'")
    case "stop":
      print("The program has terminated")
      break
    case _:
      if mode == "encrypt":
        usekey(plaintext, encryptiondict, mode)
      elif mode == "decrypt":
        usekey(plaintext, decryptiondict, mode)
