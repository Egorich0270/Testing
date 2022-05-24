import random
from random import *
class Card:

    def __init__(self, suit, power):
        self.suit = suit
        self.power = power

    def check_card(self):
        print(f'([{self.suit}] {self.power})', end=' ')


def deck_reader(list):
    for x in list: x.check_card()


card_suit = ['♦', '♠', '♥', '♣']
card_power = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
card_deck_preset = [Card(d, x) for x in card_power for d in card_suit]

while True:
    card_deck = card_deck_preset
    while len(card_deck)!=0:
        command = input('\n1)вывести колоду\n2)выбрасить карту\n3)сортировать\n4)перемешать\n')
        if command == '1':
            deck_reader(card_deck)
        elif command == '2':
            pass
        elif command == '3':
            pass
        elif command =='4':
            card_deck = random.shuffle(card_deck)
            deck_reader(card_deck)