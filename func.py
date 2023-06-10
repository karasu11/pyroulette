from random import randint
from time import sleep
from os import path
from pickle import dump, load


def main_menu():
    '''Present the player with a main menu for the game.'''
    print('### MAIN MENU ###')
    print('\n[1]: Play game\n[2]: View current high score\n[3]: View rules\n[4]'
          ': Quit')
    menu_choice = int(input('> '))
    return menu_choice


def game_loop(count, scorefile, highscore):
    '''Loop gameplay functionality.'''
    game_running = True
    while game_running:
        player_choice = spin_choice()
        if player_choice.lower() == 's':
            spin_result = spin()
            if spin_result == 1:
                print('BLAM! You died! Game over!\n')
                game_running = False
            else: 
                print('*click!* You survive this round!')
                count += 1
        elif player_choice.lower() == 'q':
            game_running = False
            print(f'You survived {count} rounds!')
            if path.exists(scorefile):
                if count > highscore[1]:
                    save_new_highscore(count, scorefile)
                    print('Your new high score has been saved!\n')
                    highscore= load_highscore(scorefile)
            else:
                save_new_highscore(count, scorefile)
                print('Your new high score has been saved!\n')
                highscore= load_highscore(scorefile)
        else: 
            print('Invalid input')


def spin_choice():
    """Let player choose whether to spin or not."""
    print('Press \'s\' to spin, or \'q\' to quit to menu')
    choice = input('> ')
    return choice


def spin():
    """Spin and return the result."""
    roll = randint(1, 6)
    print('Spinning...')
    sleep(2)
    return roll


def save_new_highscore(score, scorefile):
    '''Save the new highscore to the scorefile.'''
    entry = list()
    loop = True
    while loop:
        player_name = input('Enter your username (max 8 characters): ')
        if len(player_name) > 8:
            print('No more than 8 characters allowed!')
        else:
            entry.append(player_name)
            entry.append(score)
            pickle_handle = open(scorefile, 'wb')
            dump(entry, pickle_handle)
            pickle_handle.close()
            loop = False


def load_highscore(scorefile):
    '''Load the current highscore from the score file.'''
    if path.exists(scorefile):
        pickle_handle = open(scorefile, 'rb')
        data = load(pickle_handle)
        pickle_handle.close()
        return data


def display_highscore(scorefile):
    '''Load and display the current high score, if there is any.'''        
    if path.exists(scorefile):
        highscore = load_highscore(scorefile)
        print(f'\nCURRENT HIGH SCORE:\n{highscore[0]} - {highscore[1]}\n')
    else:
        print('\nNo high score has been saved yet!\n')


def display_rules():
    '''Display the rules of the game in a tidy way.'''
    print('\nThis is a Russian Roulette simulator.')
    print()
    print('You press \'s\' to spin the cylinder of an imaginary 6-shot revolver\n'
          'and press the trigger.')
    print()
    print('There is one bullet in the cylinder. Therefore there is a 1/6 \n'
          'chance of losing after each spin, as pressing the trigger with the \n'
          'bullet at the top of the cylinder would result in a fatal shot.')
    print()
    print('If you die, it\'s game over. The goal is to do as many spins as \n'
          'possible, but quit before dying.')
    print()
    print('If you make a new high score, you get to enter your player name, \n'
          'and your score will be saved until it is beaten.')
    print()
    print('Good luck!\n')
