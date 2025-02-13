import random
level = input("choose level Easy or Hard").lower()

if level == "easy":
    print("Guess the number")
    number = random.randrange(1, 100)
    print(number)
    player_choice = input("guess number")
    while not (number == int(player_choice)):
        if int(player_choice) > number:
            print("your number is high")
            player_choice = input("guess number")
        else:
            print("your number is low")
            player_choice = input("guess number")
    print("Correct")

else:
    print("Guess the number")
    number = random.randrange(1, 100)
    print(number)
    attempt_remain = 5
    print(f"attempts remain {attempt_remain}")
    player_choice = input("guess number")
    while not (number == int(player_choice)):
        if int(player_choice) > number:
            print("your number is high")
            attempt_remain += -1
            print(f"attempts remain {attempt_remain}")
            player_choice = input("guess number")
            if attempt_remain == 1:
                break
        elif int(player_choice) < number:
            print("your number is low")
            attempt_remain += -1
            print(f"attempts remain {attempt_remain}")
            player_choice = input("guess number")
            if attempt_remain == 1:
                break
        else:
            print("Correct")

print("code end")