# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0


# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.hand_list = []
        # create Hand object

    def __str__(self):
        ans = ""
        for i in range(len(self.hand_list)):
            temp = self.hand_list[i]
            ans += temp.get_suit()
            ans += temp.get_rank()
            
            ans += " "
        return ("Hand contains "+ans)
        

    def add_card(self, card):
        self.hand_list.append(card)
        # add a card object to a hand

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        value = 0
        ace_present = False
        for i in range(len(self.hand_list)):
            temp = self.hand_list[i]
            value += VALUES[temp.get_rank()]
            if (temp.get_rank() == "A"):
                ace_present = True
        #bust value is 21    
        if (ace_present == True and (value+10)<= 21):
            value += 10
        return value     
        # compute the value of the hand, see Blackjack video
   
    def draw(self, canvas, pos):
        for i in range(len(self.hand_list)):
            temp = self.hand_list[i]
            temp.draw(canvas,pos)
            pos[0] += CARD_SIZE[0]+20
            
        # draw a hand on the canvas, use the draw method for cards
               

        
# define deck class 
class Deck:
    def __init__(self):
        self.deck_list = []
        for i in SUITS:
            for j in RANKS:
                self.deck_list.append(Card(i,j))
                
        # create a Deck object

    def shuffle(self):
        random.shuffle(self.deck_list)
        # shuffle the deck 
        # use random.shuffle()

    def deal_card(self):
        
        return self.deck_list.pop()
        # deal a card object from the deck
        
    
    def __str__(self):
        ans = ""
        for i in range(len(self.deck_list)):
            temp = self.deck_list[i]
            ans += temp.get_suit()
            ans += temp.get_rank()
            
            ans += " "
        return ("Deck contains "+ans) 
            
        # return a string representing the deck



#define event handlers for buttons
def deal():
    global outcome, in_play , player_hand , dealer_hand , score
    if (in_play is True):
        
        outcome = " You Lose "
        score -= 1
        in_play = False
    elif (in_play is False ):
        outcome = ""
        
        deck_cards = Deck()
        deck_cards.shuffle()
        player_hand = Hand()
        dealer_hand = Hand()

        player_hand.add_card(deck_cards.deal_card())
        player_hand.add_card(deck_cards.deal_card())
        dealer_hand.add_card(deck_cards.deal_card())
        dealer_hand.add_card(deck_cards.deal_card())
        #print player_hand.get_value()
        #print dealer_hand.get_value()

        # your code goes here


        in_play = True
   

def hit():
    # replace with your code below
    global in_play,outcome , score
    if (in_play is True):
        player_hand.add_card(deck_cards.deal_card())
        #print player_hand.get_value()
        if (player_hand.get_value() > 21):
            outcome = " You went Bust and Lose "
            score -= 1
            in_play = False
    
 
    # if the hand is in play, hit the player
   
    # if busted, assign a message to outcome, update in_play and score
       
def stand():
    # replace with your code below
    global in_play , outcome ,score
    if (in_play is True ):
        in_play = False

        while (dealer_hand.get_value() < 17):
            dealer_hand.add_card(deck_cards.deal_card())

        if (dealer_hand.get_value()> 21):
            outcome = " You Win"
            score += 1
        elif (dealer_hand.get_value() >= player_hand.get_value()):
            outcome = " You Lose"
            score -= 1
        else :
            outcome = " You Win"
            score += 1
        # if hand is in play, repeatedly hit dealer until his hand has value 17 or more

        # assign a message to outcome, update in_play and score

# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    global outcome,in_play
    
    
           
    dealer_hand.draw(canvas , [100,150])
    player_hand.draw(canvas , [100,400])
    if (in_play is False):
        canvas.draw_text ("New Deal ? ",[375,380],20,"White")
        
    if (in_play is True):
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, [100+CARD_CENTER[0],150+CARD_CENTER[1]],CARD_SIZE)
        canvas.draw_text ("Hit or Stand ? ",[375,380],20,"White")
    canvas.draw_text(outcome, [375, 120], 20, 'White')
    canvas.draw_text("Black Jack", [100, 50], 30, 'White')
    canvas.draw_text("Dealer", [100, 120], 20, 'White')
    canvas.draw_text("Player", [100, 380], 20, 'White')
    canvas.draw_text("Score : "+str(score),[375,50],30,"White")
    
    #card = Card("S", "A")
    #card.draw(canvas, [300, 300])


# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deck_cards = Deck()
    
player_hand = Hand()
dealer_hand = Hand()
deal()
frame.start()


# remember to review the gradic rubric