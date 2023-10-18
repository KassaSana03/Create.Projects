#pulling from other file and importing
from p1_random import P1Random
def main():
    #establishing variables that will be used later
    rng = P1Random()
    game_cont=True
    game_num=0
    play_wins=0
    dealer_wins=0
    tie=0
    while game_cont: #while loop
        game_num +=1     #adding to current #
        print(f"START GAME #{game_num}")
        player_hands=0
        dealer_hands=0
        #initial cards
        player_cards =rng.next_int(13)+1#establishing var

        if player_cards==1:
            #The next 15 lines of code is just assigning what the cards are worth
            print("Your card is a ACE!")
            player_cards=1
        elif 2<= player_cards<=10:#numbers in between
            print(f"Your card is a {player_cards}!")
        elif player_cards==11:
            print("Your card is a Jack!")
            player_cards=10
        elif player_cards==12:
            print("Your card is a Queen!")
            player_cards=10
        elif player_cards==13:
            print("Your card is a KING!")
            player_cards=10
        player_hands += player_cards
        print(f"Your hand is: {player_hands}")
        #Turn is yours
        #creating new loop
        while player_hands<21:
            print("1. Get another card\n2. Hold hand\n3. Print statistics\n4. Exit")
            option = int(input("Choose an option: "))
            if  option==1:
                player_cards=rng.next_int(13)+1
                if player_cards==1:
                    print("Your card is a ACE!")
                    player_cards=1
                elif 2<= player_cards<=10:
                    print(f"Your card is a {player_cards}!")
                elif player_cards==11:
                    print(f"Your card is a Jack!")
                    player_cards=10
                elif player_cards ==12:
                    print(f"Your card is a Queen!")
                    player_cards=10
                elif player_cards ==13:
                    print(f"Your card is a KING!")
                    player_cards=10
                player_hands+=player_cards
                print(f"Your hand is: {player_hands}")
                if player_hands == 21:
                    print("BLACKJACK! You win!")
                    play_wins += 1
                elif player_hands > 21:
                    print("You exceeded 21! You lose.")
                    dealer_wins+=1
            elif option==2:
                #Dealer

                dealer_cards=rng.next_int(11)+16
                if dealer_cards==1:
                    dealer_cards=1
                elif 11<=dealer_cards<=13:
                    dealer_cards=10
                dealer_hands+=dealer_cards
                print(f"Dealer's hand:{dealer_hands}")
                print(f"Your hand is: {player_hands}")
                #Figures out the winner
                if dealer_hands>21:
                    play_wins+=1
                    print("You win!")
                elif dealer_hands>player_hands:
                    print("Dealer wins!")
                    dealer_wins+=1
                elif dealer_hands==player_hands:
                    print("It's a tie! No one wins!")
                    tie+=1
                elif dealer_hands < player_hands:
                    print("You win!")
                    play_wins+=1
                break
            elif option == 3:
                print(f"Number of Player wins: {play_wins}")
                print(f"Number of Dealer wins: {dealer_wins}")
                print(f"Number of tie games: {tie}")
                print(f"Total # of games played is: {game_num-1}")
                if game_num > 1:
                    win_perc = (play_wins / (game_num-1)) * 100
                else:
                    win_perc = 0.0
                print(f"Percentage of Player wins: {win_perc:.1f}%")
            elif option==4:
                game_cont=False
                break
            else:
                print("Invalid input!")
                print("Please enter an integer value between 1 and 4.")
if __name__=="__main__":
    main()



