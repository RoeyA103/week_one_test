from deck import *

def create_player(name:str) -> dict:
    if not name:
        name = 'AI'
    player = {'name':name,'hand':[],'won_pile':[]}

    return player


def init_game() -> dict:
    p1 = create_player("dan")
    p2 = create_player("")
    deck1 = create_deck()
    deck1 = shuffle(deck1)
    p1['hand'].append(deck1[:26])
    p2['hand'].append(deck1[26:])
    return {'deck':deck1,'player_1':p1,'player_2':p2}


def play_round(p1:dict, p2:dict):
    player1_card = p1['hand'].pop()
    player2_card = p2['hand'].pop()
    result = compere_cards(player1_card,player2_card)
    match result:
        case 'p1':
            p1['won_pile'].append(player1_card,player2_card)
            print(f"{p1['name']} won!")
        case 'p2':
            p2['won_pile'].append(player1_card, player2_card)
            print(f"{p2['name']} won!")
        case 'WAR':
            print("war")


def war(p1:dict,p2:dict):
    win_deck =[]
    for _ in range(3):
        win_deck.append(p1['hand'].pop())
        win_deck.append(p2['hand'].pop())
        if not p1['hand'] or not p2['hand']:
            break

    result = play_round(p1,p2)
    match result:
        case 'p1':
            p1['won_pile'] += win_deck
        case 'p2':
            p2['won_pile'] += win_deck


