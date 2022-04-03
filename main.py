"""
Learn By Doing - Morse Code Translator by DeShay K.
Github: https://github.com/deshayk
Medium: https://www.medium.com/@deshayk
LinkedIn: https://www.linkedin.com/in/deshayk/
"""

from morse import morse #import the morse code dictionary

def translateInput():
    str = input("Enter a sentence to translate: ").lower() #get the input from the user, lowercase it

    def getCharList(str):
      return [char for char in str] #return a list of characters from the input

    print(getCharList(str)) #print the list of characters from the input

#loop through the list of characters
    for x in getCharList(str): #for each character, check if it is in the morse code dictionary
      if x in morse:
        print(morse[x]) #if the character is in the morse dictionary, print the morse code for that character
      else:
        print("Sorry, that character is not in the morse code dictionary. Please use a valid character.") #if the character is not in the morse dictionary, print an error message

translateInput()    