from art import logo
from art import vs


from game_data import data
import random

def bring_data(data):
    game_data1 = random.choice(data)
    game_data2 = random.choice(data)
    return game_data1, game_data2
def print_data(gamedata):
    print(gamedata[0]['name'],gamedata[0]['description'],gamedata[0]['country'])
    print(vs)
    print(gamedata[1]['name'], gamedata[1]['description'], gamedata[1]['country'])
def compare_data(gamedata):
    if int(gamedata[0]['follower_count']) > int(gamedata[1]['follower_count']):
        return 'low'
    elif int(gamedata[0]['follower_count']) < int(gamedata[1]['follower_count']):
        return 'high'
    else:
        return True

gamedata = bring_data(data)
point = 0
print(logo)
while True:
    print_data(gamedata)
    player_choice = input("오른쪽이 더 높아 낮아. press high or low\n")
    if player_choice == "low":
        if player_choice == compare_data(gamedata):
            print("correct")
            point += 1
            print(f"your point is {point}")
        else:
            print("you wrong. game end")
            print(f"your point is {point}")
            break
    elif player_choice == "high":
        if player_choice == compare_data(gamedata):
            print("correct")
            point += 1
            print(f"your point is {point}")
        else:
            print("you wrong. game end")
            print(f"your point is {point}")
            break

