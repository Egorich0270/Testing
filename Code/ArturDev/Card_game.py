import random


class Card:
    card_power_ter = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
                      '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}

    def __init__(self, suit, power):
        self.suit = suit
        self.power = power

    def __add__(self, other):
        if Card.card_power_ter.get(self.power) > Card.card_power_ter.get(other.power):
            return self.check_card()
        else:
            return other.check_card()

    def __sub__(self, other):
        if Card.card_power_ter.get(self.power) > Card.card_power_ter.get(other.power):
            return other
        else:
            return self

    def check_card(self):
        print(f'([{self.suit}] {self.power})', end=' ')


class Carddeck:
    def __init__(self):
        self.card_suit = ['♦', '♠', '♥', '♣']
        self.card_power = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        self.card_deck_preset = [Card(d, x) for x in self.card_power for d in self.card_suit]

    def deck_reader(self):
        for x in self.card_deck_preset:
            x.check_card()

    def card_drop(self):
        num = random.randint(0, len(self.card_deck_preset) - 1)
        self.card_deck_preset[num].check_card()
        self.card_deck_preset.remove(self.card_deck_preset[num])

    def deck_sort(self):
        for i in range(len(self.card_deck_preset)):
            for j in range(len(self.card_deck_preset)-1-i):
                if Card.card_power_ter.get(self.card_deck_preset[j].power) > Card.card_power_ter.get(self.card_deck_preset[j+1].power):
                    self.card_deck_preset[j], self.card_deck_preset[j+1] = self.card_deck_preset[j+1], self.card_deck_preset[j]
        self.deck_reader()

    def __len__(self):
        return len(self.card_deck_preset)


while True:
    card_deck = Carddeck()
    while len(card_deck) != 0:
        command = input('\n1)вывести колоду\n2)выбрасить карту\n3)сортировать\n4)перемешать\n5)дуэль\n')
        if command == '1':
            card_deck.deck_reader()
        elif command == '2':
            card_deck.card_drop()
        elif command == '3':
            card_deck.deck_sort()
        elif command == '4':
            random.shuffle(card_deck.card_deck_preset)
            card_deck.deck_reader()
        elif command == '5':
            pass

