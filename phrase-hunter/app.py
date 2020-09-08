from phrasehunter.game import Game
from phrasehunter.phrase import Phrase



if __name__ == "__main__":
    
    
    game = Game()
    phrase = Phrase(game.phrases)
    print(game.active_phrase.phrase)
    game.active_phrase.display(game.guesses)
    
    
    
    



