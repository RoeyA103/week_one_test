from ..utils.deck import *


def create_player(name:str) -> dict:
    if not name:
        name = 'AI'
    player = {'name':name,'hand':[],'won_pile':[]}

    return player



def init_game() -> dict:
    p1 = create_player("dan")
    p2 = create_player("")
    deck1 = deck.create_deck()
    deck1 = deck.shuffle(deck1)
    p1['hand'].append(deck1[:26])
    p2['hand'].append(deck1[26:])
    return {'deck':deck1,'player_1':p1,'player_2':p2}


def play_round(p1:dict, p2:dict):
    player1_card = p1['hand'].pop()
    player2_card = p2['hand'].pop()
    result = deck.create_card(player1_card,player2_card)
    match result:
        case 'p1':
            p1['won_pile'].append(player1_card,player2_card)
            print(f"{p1['name']} won!")
        case 'p2':
            p2['won_pile'].append(player1_card, player2_card)
            print(f"{p2['name']} won!")
        case 'WAR':
            print("WAR!")



print(create_player(""))
