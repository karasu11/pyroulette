import func

scorefile = 'pyroulette_score.dat'
highscore = func.load_highscore(scorefile)
main_loop = True
count = 0

while main_loop:
    menu_choice = func.main_menu()
    if menu_choice == 1:
        func.game_loop(count, scorefile, highscore)
    elif menu_choice == 2:
        func.display_highscore(scorefile)
    elif menu_choice == 3:
        func.display_rules()
    elif menu_choice == 4:
        main_loop = False
    else:
        print('Invalid input')
        
