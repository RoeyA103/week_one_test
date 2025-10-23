from game_logic.deck import *
from  game_logic.cards_table import *
from  game_logic.game import *



if __name__=="__main__":
    new_game = init_game()
    player1 = new_game['player_1']
    player2 = new_game['player_2']
    while player1['hand'] and player2['hand']:
        play_round(player1,player2)

    if len(player1['won_pile']) >  len(player2['won_pile']):
        print(f"{player1['name']} won!")
    elif   len(player1['won_pile']) <  len(player2['won_pile']):
        print(f"{player2['name']} won!")
    else:
        print("its a draw")
