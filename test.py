

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

#____________________________________________-
from deck import *

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
    result = deck.compere_cards(player1_card,player2_card)
    match result:
        case 'p1':
            p1['won_pile'].append(player1_card,player2_card)
            print(f"{p1['name']} won!")
        case 'p2':
            p2['won_pile'].append(player1_card, player2_card)
            print(f"{p2['name']} won!")
        case 'WAR':
            war(p1 ,p2)


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


def cards_rank() -> dict:
    return   {'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':11,'Q':12,'K':13,'A':14}
def cards_suite() -> list:
    return ['S','H','C','D']

from cards_table import cards_rank , cards_suite
from random import randint
Cards_rank = cards_rank()
Cards_suite = cards_suite()

def create_card(rank:str, suite:str) -> dict:
    card = {'rank':rank,'suit':suite,'value':Cards_rank[rank]}
    return card

def compere_cards(p1_card:dict, p2_card:dict) -> str:
    if p1_card['value'] > p2_card['value']:
        return 'p1'
    elif p1_card['value'] < p2_card['value']:
        return 'p2'
    else:
        return "WAR"

def create_deck() -> list[dict]:
    deck = []
    for rank in Cards_rank:
        for suite in Cards_suite:
            deck.append(create_card(rank,suite))

    return deck


def shuffle(deck:list[dict]) -> list[dict]:
    for _ in range(1000):
        while True:
            index1 , index2 = randint(0,51) , randint(0,51)
            if index1 == index2:
                continue
            break
        deck[index1] , deck[index2] = deck[index2] , deck[index1]

    return deck





