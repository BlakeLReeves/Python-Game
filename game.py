# player_name = 'Manuel'
# player_attack = 10
# player_heal = 16
# health = 100

# player = ['Manuel', 10, 16, 100]

player = {'name': 'Manuel', 'attack': 10, 'heal': 16, 'health': 100}
monster = {'name': 'Max', 'attack': 12, 'health': 100}
game_running = True

while game_running == True:

    print('Please select action')
    print('1) Attack')
    print('2) Heal')

    player_choice = input()
    player_health_lbl = 'Player Health: '
    monster_health_lbl = 'Monster Health: '

    if player_choice == 1:
        monster['health'] = monster['health'] - player['attack']
        player['health'] = player['health'] - monster['attack']
        print(monster_health_lbl + str(monster['health']))
        print(player_health_lbl + str(player['health']))
    elif player_choice == 2:
        print('Heal Player')
    else:
        print('Invalid Input')

    if player['health'] | monster['health'] <= 0:
        game_running = False