import random


class Card:
    card_power_ter = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
                      '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}

    def __init__(self, suit, power):
        self.__suit = suit
        self.__power = power

    def __add__(self, other):
        if Card.card_power_ter.get(self.__power) > Card.card_power_ter.get(other.__power):
            return self.check_card()
        else:
            return other.check_card()

    def __sub__(self, other):
        if Card.card_power_ter.get(self.__power) > Card.card_power_ter.get(other.__power):
            return other
        else:
            return self

    def check_card(self):
        print(f'([{self.__suit}] {self.__power})', end=' ')


def deck_reader(list):
    for x in list:
        x.check_card()


card_suit = ['♦', '♠', '♥', '♣']
card_power = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
card_deck_preset = [Card(d, x) for x in card_power for d in card_suit]

while True:
    card_deck = card_deck_preset
    while len(card_deck) != 0:
        command = input('\n1)вывести колоду\n2)выбрасить карту\n3)сортировать\n4)перемешать\n5)дуэль\n')
        if command == '1':
            deck_reader(card_deck)
        elif command == '2':
            num = random.randint(0, len(card_deck)-1)
            card_deck[num].check_card()
            card_deck.remove(card_deck[num])

        elif command == '3':
            pass
        elif command == '4':
            random.shuffle(card_deck)
            deck_reader(card_deck)
        elif command == '5':
            num = random.randint(1, len(card_deck) - 1)
            card_deck[num].check_card()
            print()
            print('vs')
            card_deck[num-1].check_card()
            print()
            print(card_deck[num] + card_deck[num-1], 'WIN')
            card_deck.remove(card_deck[num] - card_deck[num-1])

