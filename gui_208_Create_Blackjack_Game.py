from tkinter import *
import random
from PIL import Image, ImageTk

root = Tk()
root.title('Card Deck')
root.iconbitmap('ergo64.ico')
root.geometry('1200x800')
root.configure(background="green")

def resize_cards(card):
    # open image
    our_card_img = Image.open(card)
    
    # resize the image
    our_card_resize_img = our_card_img.resize((150,218))
    global our_card_image
    our_card_image = ImageTk.PhotoImage(our_card_resize_img)
    
    # return that card
    return our_card_image

def shuffle():
    # cleat all the old cards from previous game
    dealer_label_1.config(image='')
    dealer_label_2.config(image='')
    dealer_label_3.config(image='')
    dealer_label_4.config(image='')
    dealer_label_5.config(image='')
    
    player_label_1.config(image='')
    player_label_2.config(image='')
    player_label_3.config(image='')
    player_label_4.config(image='')
    player_label_5.config(image='')
    
    suits = ["diamonds", "clubs", "hearts", "spades"]
    values = range(2,15)
    # 11:jack 12:queen 13:king 14:Ace
    global deck
    deck = []
    for suit in suits:
        for value in values:
            deck.append(f'{value}_of_{suit}')
    
    print(deck)
    print(len(deck))
    
    # create our players
    global dealer, player, dscore, pscore,dealer_spot, player_spot
    dealer = []
    player = []
    dscore = []
    pscore = []
    dealer_spot = 0
    player_spot = 0
     
    # shuffle 2 cards for player and dealer 
    dealer_hit()
    dealer_hit()
    player_hit()
    player_hit()
    
    
    # put number of remain cards in tittle bar
    root.title(f'il reste {len(deck)} cartes')
    
    # get the score
    # score(dealer_card, player_card)

def deal_cards():
    try:
        # get the dealer card
        card= random.choice(deck)
        deck.remove(card)
        dealer.append(card)
        global dealer_image
        dealer_image = resize_cards(f'images/cartes/{card}.gif')
        dealer_label.config(image=dealer_image)
        # dealer_label.config(text=card)
        # dealer_label.config(text=card)
        
    
        # get the player card
        card = random.choice(deck)
        deck.remove(card)
        player.append(card)
        # player_label.config(text=card)
        global player_image
        player_image = resize_cards(f'images/cartes/{card}.gif')
        player_label.config(image=player_image)
        # player_label.config(text=card)
        # put number of remain cards in tittle bar
        root.title(f'il reste {len(deck)} cartes')
        
        # get the score
        # score(dealer_card, player_card)
    
    except:
        if dscore.count("x")== pscore.count("x"):
            root.title(f'Egalité D:{dscore.count("x")} à P:{pscore.count("x")}')
        elif  dscore.count("x") > pscore.count("x"):
            root.title(f'GAME OVER - Dealer gagne D:{dscore.count("x")} à P:{pscore.count("x")}')
        else:
            root.title(f'GAME OVER - Player gagne  D:{dscore.count("x")} à P:{pscore.count("x")}')
            
            # root.title(f'il ne reste plus de cartes')
            # print(dscore)

def score(dealer_card, player_card):
    #split out card numbers
    dealer_card = int(dealer_card.split("_",1)[0])# on ne retient que le premier element de la découpe donc le nombre   
    player_card = int(player_card.split("_",1)[0])
    
    # compare card numbers
    if dealer_card == player_card:
        score_label.config(text="Egalité , rejouer !")
        
    elif dealer_card > player_card:
        score_label.config(text="Dealer gagne !")
        dscore.append("x")
        
    else:
        score_label.config(text="Player gagne !")
        pscore.append("x")
    
    root.title(f'il reste {len(deck)} cartes [ Dealer: {dscore.count("x")} / Player: {pscore.count("x")} ')

def dealer_hit():
    global dealer_spot
    if dealer_spot < 5:
        try:
            # get the player card
            dealer_card = random.choice(deck)
            deck.remove(dealer_card)
            dealer.append(dealer_card)
            # player_label.config(text=card)
            global dealer_image1, dealer_image2, dealer_image3, dealer_image4, dealer_image5
                        
            if dealer_spot == 0:
                dealer_image1 = resize_cards(f'images/cartes/{dealer_card}.gif')
                dealer_label_1.config(image=dealer_image1)
                # increment player_spot counter
                dealer_spot += 1
            elif dealer_spot == 1:
                # resize card
                dealer_image2 = resize_cards(f'images/cartes/{dealer_card}.gif')
                # ouput card to screen
                dealer_label_2.config(image=dealer_image2)
                # increment player_spot counter
                dealer_spot += 1
            elif dealer_spot == 2:
                # resize card
                dealer_image3 = resize_cards(f'images/cartes/{dealer_card}.gif')
                # ouput card to screen
                dealer_label_3.config(image=dealer_image3)
                # increment player_spot counter
                dealer_spot += 1
            elif dealer_spot == 3:
                # resize card
                dealer_image4 = resize_cards(f'images/cartes/{dealer_card}.gif')
                # ouput card to screen
                dealer_label_4.config(image=dealer_image4)
                # increment player_spot counter
                dealer_spot += 1
            elif dealer_spot == 4:
                # resize card
                dealer_image5 = resize_cards(f'images/cartes/{dealer_card}.gif')
                # ouput card to screen
                dealer_label_5.config(image=dealer_image5)
                # increment player_spot counter
                dealer_spot += 1
                                    
            # player_label.config(text=card)
            # put number of remain cards in tittle bar
            root.title(f'il reste {len(deck)} cartes')
        except:
            root.title(f'il ne reste plus de cartes')

def player_hit():
    global player_spot
    if player_spot < 5:
        try:
            # get the player card
            player_card = random.choice(deck)
            deck.remove(player_card)
            player.append(player_card)
            # player_label.config(text=card)
            global player_image1, player_image2, player_image3, player_image4, player_image5
                        
            if player_spot == 0:
                player_image1 = resize_cards(f'images/cartes/{player_card}.gif')
                player_label_1.config(image=player_image1)
                # increment player_spot counter
                player_spot += 1
            elif player_spot == 1:
                # resize card
                player_image2 = resize_cards(f'images/cartes/{player_card}.gif')
                # ouput card to screen
                player_label_2.config(image=player_image2)
                # increment player_spot counter
                player_spot += 1
            elif player_spot == 2:
                # resize card
                player_image3 = resize_cards(f'images/cartes/{player_card}.gif')
                # ouput card to screen
                player_label_3.config(image=player_image3)
                # increment player_spot counter
                player_spot += 1
            elif player_spot == 3:
                # resize card
                player_image4 = resize_cards(f'images/cartes/{player_card}.gif')
                # ouput card to screen
                player_label_4.config(image=player_image4)
                # increment player_spot counter
                player_spot += 1
            elif player_spot == 4:
                # resize card
                player_image5 = resize_cards(f'images/cartes/{player_card}.gif')
                # ouput card to screen
                player_label_5.config(image=player_image5)
                # increment player_spot counter
                player_spot += 1
                                    
            # player_label.config(text=card)
            # put number of remain cards in tittle bar
            root.title(f'il reste {len(deck)} cartes')
        except:
            root.title(f'il ne reste plus de cartes')

def stands():
    pass
  
my_frame= Frame(root, bg="green")
my_frame.pack(pady=20)

dealer_frame = LabelFrame(my_frame, text="Dealer", bd=0)
dealer_frame.pack(padx=20, ipadx=20)

player_frame = LabelFrame(my_frame, text="Player", bd=0)
player_frame.pack( ipadx=20, pady=10)

# put dealer cards in frame
dealer_label_1 = Label(dealer_frame, text="")
dealer_label_1.grid(row=0, column=0, pady=20, padx=20)

dealer_label_2 = Label(dealer_frame, text="")
dealer_label_2.grid(row=0, column=1, pady=20, padx=20)

dealer_label_3 = Label(dealer_frame, text="")
dealer_label_3.grid(row=0, column=2, pady=20, padx=20)

dealer_label_4 = Label(dealer_frame, text="")
dealer_label_4.grid(row=0, column=3, pady=20, padx=20)

dealer_label_5 = Label(dealer_frame, text="")
dealer_label_5.grid(row=0, column=4, pady=20, padx=20)

# create player images/cards put player cards in frames
player_label_1 = Label(player_frame, text="")
player_label_1.grid(row=1, column=0,pady=20, padx=20)

player_label_2 = Label(player_frame, text="")
player_label_2.grid(row=1, column=1,pady=20, padx=20)

player_label_3 = Label(player_frame, text="")
player_label_3.grid(row=1, column=2,pady=20, padx=20)

player_label_4 = Label(player_frame, text="")
player_label_4.grid(row=1, column=3,pady=20, padx=20)

player_label_5 = Label(player_frame, text="")
player_label_5.grid(row=1, column=4,pady=20, padx=20)

# score label
# score_label = Label(root, text="", font=("helvetica",14), bg="green")
# score_label.pack()

# create button frame
button_frame = Frame(root, bg="green")
button_frame.pack(pady=20)

shuffle_button = Button(button_frame, text="Shuffle Deck", font=("helvetica",14), command=shuffle)
shuffle_button.grid(row=0, column=0)

card_button = Button(button_frame, text="Hit Me!", font=("helvetica",14), command = player_hit)
card_button.grid(row=0, column=1, padx=10)

stand_button = Button(button_frame, text="Stand!", font=("helvetica",14), command = stands)
stand_button.grid(row=0, column=2, padx=10)

shuffle()

root.mainloop()
