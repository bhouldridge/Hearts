import unittest
from hearts import Card
from hearts import Deck

class TestCard(unittest.TestCase):
    
    def setUp(self):
        self.card1 = Card('Two', 'Clubs')
    
    def test_card_face(self):
        
        self.assertEqual(self.card1.face, 'Two')
        
    def test_card_suit(self):
        
        self.assertEqual(self.card1.suit, 'Clubs')
    
    def test_card_value(self):
        
        self.assertEqual(self.card1.value, int(2))
        
    def test_repr(self):
        
        self.assertEqual(repr(self.card1), 'Two of Clubs')
        
class TestDeck(unittest.TestCase):
        
    def setUp(self):
        self.deck1 = Deck()
        
    def test_init(self):
        
        self.assertEqual(len(self.deck1.cards), 52)
        self.assertEqual(len(set(self.deck1.cards)), 52)
        
    def test_shuffle(self):
        
        original_order = self.deck1.cards
        self.deck1.shuffle()
        shuffled_order = self.deck1.cards
        self.assertNotEqual(original_order, shuffled_order)
        
if __name__=='__main__':
    unittest.main()
