# Necessary dependency
import random
# Name of class
class Encryption(object):
    # Initialization function
    def __init__(self,key_seed,layers,characters):
        # Setting the random seed for key generation
        self.key_seed = key_seed
        # All of the potential characters to be used in input string and key
        self.alphabet = list("""{}""".format(characters))
        # Right now the key is nothing
        self.key = None
        # The number of layers represent the number of occurences of recursive obfuscation
        # Can be seen as a secondary key
        self.layers = layers
        # Temporary variable to hold text
        self.iterText = None
        # Encryption dictionary
        self.encrypt = {}
        # Decryption dictionary
        self.decrypt = {}

    # Function to generate keys randomly based off of the random seed, used in an iterative manner
    def __iterGenKey(self,key_seed):
        # first we create a temporary key - which is a copy of the alphabet set in the init function
        key = self.alphabet.copy()
        # then we randomize that temporary key based on the key seed passed in in this function specifically
        # the key seed is dynamic throughout this program
        random.Random(key_seed).shuffle(key)
        # then we set the key to self.key
        self.key = key
        # then we set the encryption and decryption dictionaries to use to encrypt and decrypt themessage
        for i in range(len(self.alphabet)):
            self.encrypt[self.alphabet[i]] = self.key[i]
        for i in range(len(self.alphabet)):
            self.decrypt[self.key[i]] = self.alphabet[i]

    # this function takes in some text, and encodes it based on the information in the encryption dictionary
    # think of a randomized ceasars cipher
    def __iterEncode(self,text):
        text = list(text)
        encoded_text = []
        for i in text:
            encoded_text.append(self.encrypt[i])
        return ''.join(encoded_text)

    # this function takes in some text, and decodes it based on the information in the decryption dictionary
    # again - it is similar to a randomized ceasar cipher
    def __iterDecode(self,text):
        text = list(text)
        decoded_text = []
        for i in text:
            decoded_text.append(self.decrypt[i])
        return ''.join(decoded_text)

    # this function takes in text, and for every single character in the text, generates a new random key
    # and places that new letter in a new list which is then joined to a string
    def __charEncode(self,text):
        self.iterText = text
        hypertext = []
        for j in list(range(len(self.iterText))):
            self.__iterGenKey(self.key_seed*j)
            #print(''.join(self.key))
            #print()
            hypertext.append(self.__iterEncode(self.iterText[j]))
        return "".join(hypertext)

    # This function reverses the process from the last function
    def __charDecode(self,text):
        self.iterText = text
        hypertext = []
        for j in list(range(len(self.iterText)))[::-1]:
            self.__iterGenKey(self.key_seed*j)
            #print(self.key)
            #print()
            hypertext.insert(0,self.__iterDecode(self.iterText[j]))
        return "".join(hypertext)

    # This function obfuscates the encrypted text by iteratively repeating the entire process up to this point
    # to the number of layers specified
    def encode(self,text):
        self.iterText = text
        for i in range(self.layers):
            self.iterText = self.__charEncode(self.iterText)
        return self.iterText

    # This function un-obfuscates the process by iteratively repeating the entire process up to this point in reverse
    def decode(self,text):
        self.iterText = text
        for i in range(self.layers):
            self.iterText = self.__charDecode(self.iterText)
        return self.iterText

# Essentially what this class does, is take in text, generate a totally random key (based on random seed), that varies
# for each letter. It then does this whole process for the encrypted text repeatedly through as many layers as you want.
# Do decrypt the text is simply to reverse the process.
