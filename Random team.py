from random import shuffle as s

def number_game(n):

    nums = list(range(1,n+1))

    players =[]

    for i in range(1,n+1):

        players.append(input(f'Enter player-{i} name : '))

    s(nums)

    d = dict(zip(players,nums))

    return d

   

   

no_of_players = int(input("Enter number of players : "))

print(number_game(no_of_players))
