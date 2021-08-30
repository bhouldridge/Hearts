import random

class Card:
    
    face_value_dict = {'Two':2,
                       'Three':3,
                       'Four':4,
                       'Five':5,
                       'Six':6,
                       'Seven':7,
                       'Eight':8,
                       'Nine':9,
                       'Ten':10,
                       'Jack':11,
                       'Queen':12,
                       'King':13,
                       'Ace':14}
    suits = ('Clubs', 'Hearts', 'Spades', 'Diamonds')
    
    def __init__(self, face, suit):

        self.face = face
        self.value = Card.face_value_dict[self.face]
        self.suit = suit

    def __repr__(self):
        return(self.face + ' of ' + self.suit)
    
    
class Deck:
    
    suits = ('Dimonds', 'Clubs', 'Hearts', 'Spades')
    faces = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine',
             'Ten', 'Jack', 'Queen', 'King', 'Ace')
    
    def __init__(self):
        self.cards = []
        for suit in self.suits:
            for face in self.faces:
                self.cards.append(Card(face,suit))
    
    def shuffle(self):
        random.shuffle(self.cards)
        
    def deal(self):
        return self.cards.pop(0)
    