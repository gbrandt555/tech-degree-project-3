import random

from phrasehunter.phrase import Phrase

class Game:
    
    def __init__(self):
        self.missed = 0
        self.phrases = [Phrase("you cant handle the truth"), 
                        Phrase("why so serious"), 
                        Phrase("just keep swimming"), 
                        Phrase("i see dead people"), 
                        Phrase("there is no crying in baseball")
                        ]
        self.active_phrase = self.get_random_phrase()
        self.guesses = [" "]
    

    def get_random_phrase(self):
        return random.choice(self.phrases)


