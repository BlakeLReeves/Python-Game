# player_name = 'Manuel'
# player_attack = 10
# player_heal = 16
# health = 100

# player = ['Manuel', 10, 16, 100]

from random import randint

game_running = True

while game_running == True:
    
    new_round = True
    player = {'name': 'Manuel', 'attack': 10, 'heal': 16, 'health': 100}
    monster = {'name': 'Max', 'attack_min': 10, 'attack_max': 20, 'health': 100}

    print('---' * 7)
    print('Enter Player Name:')
    print('---' * 7)
    player['name'] = input()

    print('---' * 7)
    print(player['name'] + ' has ' + str(player['health']) + ' health.')
    print(monster['name'] + ' has ' + str(monster['health']) + ' health.')

    while new_round == True:


        player_won = False
        monster_won = False

        print('---' * 7)
        print('Please select action')
        print('---' * 7)
        print('1) Attack')
        print('2) Heal')
        print('3) Exit Game')
        print('---' * 7)

        player_choice = input()
        player_health_lbl = player['name'] + "'s" + ' Health: '
        monster_health_lbl = monster['name'] + "'s" + ' Health: '

        if player_choice == 1:

            monster['health'] = monster['health'] - player['attack']
            if monster['health'] <= 0:
                player_won = True

            else:
                monster_attack = randint(monster['attack_min'], monster['attack_max'])
                player['health'] = player['health'] - monster_attack
                if player['health'] <= 0:
                    monster_won = True

        elif player_choice == 2:

            player['health'] = player['health'] + player['heal']
            player['health'] = player['health'] - monster_attack
            if player['health'] <= 0:
                monster_won = True

        elif player_choice == 3:

            print('---' * 7)
            print('Exited Game')
            print('---' * 7)

            print('Results:')
            print('---' * 7)
            print(monster_health_lbl + str(monster['health']))
            print(player_health_lbl + str(player['health']))
            print('---' * 7)

            new_round = False
            game_running = False

        else:

            print('Invalid Input')

        if player_won == False and monster_won == False:
            print('---' * 7)
            print(player['name'] + ' has ' + str(player['health']) + ' health left.')
            print(monster['name'] + ' has ' + str(monster['health']) + ' health left.')

        elif player_won:
            print('---' * 7)
            print(player['name'] + ' won!')

            print('---' * 7)
            print('Results:')
            print('---' * 7)
            print(monster_health_lbl + str(monster['health']))
            print(player_health_lbl + str(player['health']))
            print('---' * 7)

            new_round = False

        elif monster_won:
            print('---' * 7)
            print(monster['name'] + ' the monster ' + ' won...')
            
            print('---' * 7)
            print('Results:')
            print('---' * 7)
            print(monster_health_lbl + str(monster['health']))
            print(player_health_lbl + str(player['health']))
            print('---' * 7)

            new_round = False