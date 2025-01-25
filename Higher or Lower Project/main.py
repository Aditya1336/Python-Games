import art
import random
import game_data
import os

score=0
alive=True
print(art.logo)

a = random.randrange(0,len(game_data.data))
while alive:

    if score>0:
        print(art.logo)
        print(f"That's Right! Your Score is {score}.")
    print(f"Compare A: {game_data.data[a]['name']}, a {game_data.data[a]['description']}, from {game_data.data[a]['country']}")
    print(art.vs)
    b = random.randrange(0,len(game_data.data))
    print(f"Compare B: {game_data.data[b]['name']}, a {game_data.data[b]['description']}, from {game_data.data[b]['country']}")

    dec = input("Who has more followers? 'A' or 'B' : ")
    if dec=='A':
        if game_data.data[a]['follower_count'] > game_data.data[b]['follower_count']:
            score+=1
        else:
            alive=False
    else:
        if game_data.data[b]['follower_count'] > game_data.data[a]['follower_count']:
            score+=1
        else:
            alive=False

    a=b



    if alive:
        os.system('cls')
    else:
        os.system('cls')
        print(art.logo)
        print("That's incorrect! Better luck next time!")



