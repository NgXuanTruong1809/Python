game_list = [' ',' ',' ',' ',' ',' ',' ',' ',' ']

def display_game(game_list):
    print('{:^3}|{:^3}|{:^3}'.format(game_list[0],game_list[1],game_list[2]))
    print('-' * 11)
    print('{:^3}|{:^3}|{:^3}'.format(game_list[3],game_list[4],game_list[5]))
    print('-' * 11)
    print('{:^3}|{:^3}|{:^3}'.format(game_list[6],game_list[7],game_list[8]))

print('Thứ tự của trò chơi như sau : ')
display_game([1,2,3,4,5,6,7,8,9])
print('Người chơi 1 sẽ bắt đầu trước. Bắt đầu chơi game nhé !!!')

def player_input():
    choice = ''
    while choice.upper() not in ['X','O']:
        choice = input('Người chơi 1 chọn X hay O: ')
        if choice.upper() not in ['X','O']:
            print('Chọn sai giá trị X/O !!! Vui lòng nhập lại')
    player1 = choice.upper()
    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'
    return player1, player2

def game_over(mylist):
    if (
        (mylist[0] == mylist[1] == mylist[2] != ' ') or (mylist[3] == mylist[4] == mylist[5] != ' ') or (mylist[6] == mylist[7] == mylist[8] != ' ') or
        (mylist[0] == mylist[3] == mylist[6] != ' ') or (mylist[1] == mylist[4] == mylist[7] != ' ') or (mylist[2] == mylist[5] == mylist[8] != ' ') or
        (mylist[0] == mylist[4] == mylist[8] != ' ') or (mylist[2] == mylist[4] == mylist[6] != ' ')   
        ):
        return True
    return False

def position_replace():
    choice = ''
    while choice not in [1,2,3,4,5,6,7,8,9]:
        choice = input('Chọn vị trí để điền (1-9) : ')
        if choice not in [1,2,3,4,5,6,7,8,9]:
            print('Vị trí chọn không hợp lệ')
    return int(choice)

def replace_gamelist(game_list, position, player):
    game_list[position] = player
    return game_list

def game_play():
    player1, player2 = player_input()

