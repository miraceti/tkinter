from tkinter import *
import random
from tkinter import messagebox
import winsound
from PIL import Image, ImageTk

root = Tk()
root.title('Card Deck')
root.iconbitmap('ergo64.ico')
root.geometry('1200x800')
root.configure(background="green")

# stand
def stand():
    # keep track of winning
    global player_total, dealer_total, player_score
    player_total = 0
    dealer_total = 0
    
    # get the dealer score total
    for score in dealer_score:
        # add up score
        dealer_total += score
    
    for score in player_score:
        # add up score
        player_total += score
        
    # freeze the buttons
    card_button.config(state="disabled")
    stand_button.config(state="disabled")
    
    # logic 17 or 16
    if dealer_total >= 17:
        # check if bust
        if dealer_total > 21:
            # bust
            messagebox.showinfo("Player Wins!",f"Player Wins! Dealer: {dealer_total} Player: {player_total}")
        elif dealer_total == player_total:
            # tie
            messagebox.showinfo("Tie!",f"It's a Tie! Dealer: {dealer_total} Player: {player_total}")
        elif dealer_total > player_total:
            # dealer wins
            messagebox.showinfo("Dealer Wins!",f"Dealer Wins! Dealer: {dealer_total} Player: {player_total}")
        else:
            # player wins
            messagebox.showinfo("Player Wins!",f"Pmlayer Wins! Dealer: {dealer_total} Player: {player_total}")
    else:
        # add card to dealer
        dealer_hit()
        # recalculate stuff
        stand() 
        

# test for blackjack on shuffle
def blackjack_shuffle(player):
    # keep track of winning
    global player_total, dealer_total, player_score
    player_total = 0
    dealer_total = 0
    
    if player=="dealer":
        if len(dealer_score)==2:
            if dealer_score[0] + dealer_score[1] == 21:
                # update status
                blackjack_status["dealer"]="yes"
                
                # messagebox.showinfo("Dealer Wins!","Blackjack! Dealer Wins!")
                # # disable buttons
                # card_button.config(state="disabled")
                # stand_button.config(state="disabled")
        
    if player == "player":
        if len(player_score)==2:
            if player_score[0] + player_score[1] == 21:
                # update status
                blackjack_status["player"]="yes"
        else:
            # loop thru player scorelist and add up card
            for score in player_score:
                # add up score
                player_total += score
                
            if player_total == 21:
                blackjack_status["player"] = "yes"
                
            elif player_total > 21:
                # check for ace conversion
                for card_num , card in enumerate(player_score):
                    if card == 11:
                        player_score[card_num] = 1
                        
                        # clear player total and recalculate
                        player_total = 0
                        for score in player_score:
                            # add up score
                            player_total += score

                        # check for over 21
                        if player_total > 21 :
                            blackjack_status["player"] = "bust"  
                            
                else:
                    # check new totals for 21 or over 21
                    if  player_total  == 21:
                        blackjack_status["player"] = "yes"  
                    if  player_total  > 21:
                        blackjack_status["player"] = "bust"  
               
                # messagebox.showinfo("Player Wins!","Blackjack! Player Wins!")
                # # disable buttons
                # card_button.config(state="disabled")
                # stand_button.config(state="disabled")
    
    if len(dealer_score)== 2 and len(player_score)==2:
        # check for push ou Tie
        if blackjack_status["dealer"]=="yes" and blackjack_status["player"]=="yes":
            # it's a push or a tie egalité!
            messagebox.showinfo("Push!","It's a Tie!")
            card_button.config(state="disabled")
            stand_button.config(state="disabled")
    # check for dealer win
        elif blackjack_status["dealer"]=="yes" :
            messagebox.showinfo("Player Wins!","Blackjack! Player Wins!")
            # # disable buttons
            card_button.config(state="disabled")
            stand_button.config(state="disabled")
    # checkfor player win
        elif blackjack_status["player"]=="yes":
            messagebox.showinfo("Player Wins!","Blackjack! Player Wins!")
            # # disable buttons
            card_button.config(state="disabled")
            stand_button.config(state="disabled")

    #check for 21 during the game 
    else:
        if blackjack_status["dealer"]=="yes" and blackjack_status["player"]=="yes":
            # it's a push or a tie egalité!
            messagebox.showinfo("Push!","It's a Tie!")
            card_button.config(state="disabled")
            stand_button.config(state="disabled")
    # check for dealer win
        elif blackjack_status["dealer"]=="yes" :
            messagebox.showinfo("Player Wins!","21! Player Wins!")
            # # disable buttons
            card_button.config(state="disabled")
            stand_button.config(state="disabled")
    # checkfor player win
        elif blackjack_status["player"]=="yes":
            messagebox.showinfo("Player Wins!","21! Player Wins!")
            # # disable buttons
            card_button.config(state="disabled")
            stand_button.config(state="disabled")
            
    # check for player bust 
    if blackjack_status["player"]=="bust":
        messagebox.showinfo("Player Busts!",f"Player Loses! {player_total}")
        # # disable buttons
        card_button.config(state="disabled")
        stand_button.config(state="disabled")
                

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
    # keep track of winning
    global blackjack_status , player_total, dealer_total
    player_total = 0
    dealer_total = 0
    
    blackjack_status = {"dealer":"no", "player":"no"}
    # enable_disable buttons
    card_button.config(state="normal")
    stand_button.config(state="normal")
        
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
    global dealer, player, dscore, pscore,dealer_spot, player_spot,dealer_score,player_score
    dealer = []
    player = []
    dscore = []
    pscore = []
    dealer_score=[]
    player_score=[]
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
            # append to dealer_score list and convert facecards to 10or 11
            dcard = int(dealer_card.split("_",1)[0])
            if dcard==14:
                dealer_score.append(11)
            elif dcard==11 or dcard==12 or dcard ==13:
                dealer_score.append(10)
            else:
                dealer_score.append(dcard)
            
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
            
        # check for blackjack
        blackjack_shuffle("dealer")
        
def player_hit():
    global player_spot
    if player_spot < 5:
        try:
            # get the player card
            player_card = random.choice(deck)
            deck.remove(player_card)
            player.append(player_card)
            
            # append to player_score list and convert facecards to 10 or 11
            pcard = int(player_card.split("_",1)[0])
            if pcard==14:
                player_score.append(11)
            elif pcard==11 or pcard==12 or pcard ==13:
                player_score.append(10)
            else:
                player_score.append(pcard)
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
            
        # check for blackjack
        blackjack_shuffle("player")


  
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

stand_button = Button(button_frame, text="Stand!", font=("helvetica",14), command = stand)
stand_button.grid(row=0, column=2, padx=10)

shuffle()

root.mainloop()
