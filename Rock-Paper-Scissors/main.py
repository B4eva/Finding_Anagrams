
import random

while True:

 print(f'\nYou are playing Rock, Papper, Scissors\n Enter Either R, P, S and wait for the CPU to Challenge you')
 player_option = input("Enter a choice : ").lower()

 computer_options = ['R', 'P', 'S']

 cpu_choice = (random.choice(computer_options)).lower()
 print(f"\nYou chose {player_option}, computer chose {cpu_choice}.\n")


 if(player_option == cpu_choice):
     print('its a tie, Enter options again')
 elif player_option == 'r':
    if(cpu_choice == 's'):
        print(f'\n Rock smashes scissors, Player_1 wins')
    else:
        print('Papper covers Rock, Cpu wins')
 elif(player_option == 'p'):
    if(cpu_choice == 'r'):
        print(f'\n Papper covers Rock. Player_1 wins')
    else:
        print(f'\n Scissors cuts paper, cpu wins')
 elif(player_option == 's'):
    if(cpu_choice == 'p'):
        print(f'\n Scissors cuts papper, player_1 wins')
    else:
        print(f'\n Rock smashes scissors, Cpu wins')
 elif(player_option not in cpu_choice):
     print('Your choice was not known, try again with r, s or p')
 play_agian = input(f'\nPlay again? (y/n) :' )
 if(play_agian.lower() == 'n'):
     break

   