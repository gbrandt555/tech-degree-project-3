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
    

    def welcome(self):
        print("********************************\n^_^Welcome to Phrase Hunters^_^ \n********************************")
    

    def start(self):
        self.welcome()
        while self.missed < 5:
            print("Number missed: {}".format(self.missed))
            self.active_phrase.display(self.guesses)
            user_guess = self.get_guess()
            self.guesses.append(user_guess)
            self.active_phrase.check_guess(user_guess)
            if not self.active_phrase.check_guess(user_guess):
                self.missed += 1
            self.active_phrase.check_complete(self.guesses)
        self.game_over()

    def game_over(self):
        if self.missed == 5:
            print("You lose.")
        else:
            print("You win.")
                

    def get_guess(self):
        return input("\nEnter a letter: ")
        


