from cards_table import cards_rank , cards_suite
from random import randint


def create_card(rank:str, suite:str) -> dict:
    card = {'rank':rank,'suit':suite,'value':cards_rank[rank]}
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
    for rank in cards_rank:
        for suite in cards_suite:
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

