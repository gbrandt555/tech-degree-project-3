class Phrase:
    
    def __init__(self, phrase):
        self.phrase = phrase

    
    def display(self, guesses):
        for letter in self.phrase:
            if guesses == letter:
                print("{}".format(letter),end=" ")
            else:
                print("_",end=" ")




