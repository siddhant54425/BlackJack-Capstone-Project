import random
from replit import clear

def deal_card():
    cards=[11,1,2,3,4,5,6,7,8,9,10,10,10,10]
    pick_card=random.choice(cards)
    return pick_card

def calculate_score(cards):
    if sum(cards)==21 and len(cards)==2:
        return 0

    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
        return 1    

    return sum(cards)

def compare(user_score,computer_score):
    if user_score == computer_score:
        return "Draw"
    elif user_score == 0:
        return "You Win with a blackjack😎"
    elif computer_score == 0:
        return "opponent win with a blackjack😖"   
    elif user_score > 21:
        return "You went over, you loose😒"
    elif computer_score > 21:
        return "Computer went over, you win😉"   
    elif user_score > computer_score:
        return "You win🤩"
    else:
        return "You loose😣"                 

def play_game():

    user_cards=[]
    computer_cards=[]
    is_gameover=False
    
    for a in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    
    
    while not is_gameover:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f" Your cards: {user_cards} , Your score: {user_score}")
        print(f" Computer first card: {computer_cards[0]}")
        
        if user_score==0 or computer_score==0 or user_score>21:
            is_gameover=True
        else:
            user_should_deal=input("Type 'y' to get another card or 'n' to pass: ")
            if user_should_deal=='y':
                user_cards.append(deal_card())
            else:
                is_gameover=True        
    
    while computer_score!=0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score=calculate_score(computer_cards)

    print(f"   Your Final Hand: {user_cards}, your final score: {user_score}")
    print(f"   Computer Final Hand: {computer_cards}, computer final score: {computer_score}")
    print(compare(user_score, computer_score)) 

while input("Do you want to play the game of BlackJack, Type 'y' to play again or 'n' to not play: ")=='y':
    clear()
    play_game()   