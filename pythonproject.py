from random import randint
A = 1
J = 10
K = 10
Q = 10
all_cards = [A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, K, Q]
new_list = []
for x in range(len(all_cards)):
    z = 0
    while z < 4:
        new_list.append(all_cards[x])
        z += 1
player_1_counter = 0
player_1_final_val = 21313
player_2_final_val = 12312
player_2_counter = 0
print("Player 1's turn.")
#starting cards for deck
player_1_counter += new_list[randint(0, len(new_list)-1)]
player_1_counter += new_list[randint(0, len(new_list)-1)]
print(player_1_counter)
while player_1_counter != player_1_final_val:
    if player_1_counter > 21:
        player_1_final_val = player_1_counter
        print("Value over 21, player 1 you lose")
    elif player_1_counter == 21:
        player_1_final_val = player_1_counter
        print("you got 21!")
    elif player_1_counter <= 21:
        next_instruction1 = input("Would you like to 'hit' or 'stand?")
        if next_instruction1 == 'hit':
            player_1_counter += new_list[randint(0, len(new_list)-1)]
            print(player_1_counter)
        elif next_instruction1 == 'stand':
            player_1_final_val = player_1_counter
print("player 2's turn.")
player_2_counter += new_list[randint(0, len(new_list)-1)]
player_2_counter += new_list[randint(0, len(new_list)-1)]
print(player_2_counter)
while player_2_counter != player_2_final_val:
    if player_2_counter > 21:
        player_2_final_val = player_2_counter
        print("Value over 21, player 2 you lose")
    elif player_2_counter == 21:
        player_2_final_val = player_2_counter
        print("you got 21!")
    elif player_2_counter < 21:
        next_instruction2 = input("Would you like to 'hit' or 'stand?")
        if next_instruction2 == 'hit':
            player_2_counter += new_list[randint(0, len(new_list)-1)]
            print(player_2_counter)
        elif next_instruction2 == 'stand':
            player_2_final_val = player_2_counter
if player_2_final_val == player_1_final_val:
    print("its a tie! restart the game to try again.")
elif player_1_final_val > player_2_final_val:
    if player_1_final_val <= 21:
        print("player 1 won! congrats.")
    elif player_1_final_val > 21:
        print("player 2 won! congrats")
elif player_2_final_val > player_1_final_val:
    print("player 2 won! congrats")
    if player_2_final_val <= 21:
        print("player 2 won! congrats.")
    elif player_2_final_val > 21:
        print("player 1 won! congrats")