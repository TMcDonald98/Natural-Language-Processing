#Team Member #1: Diego Valdez 
#Team Member #2: Thomas McDonald 
#Project 4: This project represents the Soundex algorithm as a finite state transducer
#Due: September 7, 2018
#
import re

def main():
    
    unencodedString = raw_input('What word would you like encode? ')
    encodedString= unencodedString[:1]
    unencodedString = unencodedString.lower()
    
    unencodedString = unencodedString[1:]
    for i in range(0,len(unencodedString)):
        if unencodedString[i] in ("a", "e", "h", "i", "o", "u", "w", "y"): 
            unencodedString = re.sub(unencodedString[i], "~", unencodedString)
        elif unencodedString[i] in ("b","f","p","v"):
            unencodedString = re.sub(unencodedString[i], "1", unencodedString)
        elif unencodedString[i] in ("c","g","j","k","q","s","x","z"):
            unencodedString = re.sub(unencodedString[i], "2", unencodedString)
        elif unencodedString[i] in ("d","t"):
            unencodedString = re.sub(unencodedString[i], "3", unencodedString)
        elif unencodedString[i] in ("l"):
            unencodedString = re.sub(unencodedString[i], "4", unencodedString)
        elif unencodedString[i] in ("m","n"):
            unencodedString = re.sub(unencodedString[i], "5", unencodedString)
        elif unencodedString[i] in ("r"):
            unencodedString = re.sub(unencodedString[i], "6", unencodedString)
    for i in range(0,(len(unencodedString)-1)):
        if unencodedString[i] == unencodedString[i+1]:
            unencodedString= unencodedString[:i]+"~"+unencodedString[i+1:]
    while "~" in unencodedString:
        unencodedString = re.sub("~", "", unencodedString)
    encodedString += unencodedString[:3]
    while len(encodedString) < 4:
        encodedString = encodedString+"0"
    
    print(encodedString)

main()
