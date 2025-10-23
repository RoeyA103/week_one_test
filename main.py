from utils.deck import *
from  utils.cards_table import *
from  game_logic.game import  *



if __name__=="__main__":
    new_game = init_game()
    player1 = new_game['player_1']
    player2 = new_game['player_2']

    run_game(player1,player2)
