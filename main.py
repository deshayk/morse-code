"""
Learn By Doing - Morse Code Translator by DeShay K.
Github: https://github.com/deshayk
Medium: https://www.medium.com/@deshayk
LinkedIn: https://www.linkedin.com/in/deshayk/
"""
'''
Program Notes:
I need to be able to print the morse code on a single line
'''
from morse_dictionary import morse #import the morse code dictionary

def main(): #main function
  
    print("\n") #new line
    print("Welcome to the Morse Code Translator!") #welcome message
    print("\n") #new line
    str = input("Enter a sentence to translate: ").lower() #get the input from the user, lowercase it

    def getCharList(str):
      return [char for char in str] #return a list of characters from the input

    print(getCharList(str)) #print the list of characters from the input

    #loop through the list of characters
    for x in getCharList(str): #for each character, check if it is in the morse code dictionary
      translation = [] #create a list to hold the translation
      if x in morse: #if the character is in the dictionary
        translation.append(morse[x]) #add the translation to the list
        final = ' '.join(translation) #join the translation list into a string
        finalTranslation = '' #create a list to hold the final translation
        for y in final: #for each character in the translation
          finalTranslation += y #add the character to the final translation
        print(finalTranslation) #print the final translation
      else:
        print("Sorry, that character is not in the morse code dictionary. Please use a valid character.") #if the character is not in the morse dictionary, print an error message

if __name__ == '__main__':  
    main() #run the main function