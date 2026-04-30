import random
BOLD = '\033[1m'
END = '\033[0m'

def start(difficulty=0,high=0,low=1,attempts=7):
    print(F'{BOLD}WELCOME TO GUESS A NUMBER{END}')
    try:
        difficulty = int(input(f"{BOLD}Insert level difficulty.\n1-Easy\n2-Medium\n3-Hard\n=={END}"))
    except ValueError:
        print(f"{BOLD}Please enter an integer.{END}")
    if difficulty == 1:
         high=100
    elif difficulty == 2:
         high=150
    elif difficulty == 3:
         high=200
    secret = random.randint(low, high)
    for attempt in range(1,attempts+1):
        try:
            guess = int(input(f"{BOLD}Insert your guess. Attempt {attempt}/{attempts}: {END}"))
        except ValueError:
            print(f"{BOLD}Please enter an integer.{END}")
        if guess < secret :
            print(f"{BOLD}To Low :P {END}")
        elif guess > secret :
            print(f"{BOLD}To High :P {END}")
        else:
            print(f"{BOLD}Correct!, you got it in attempt {attempt}/{attempts} {END}")
            return True
        
    print (f"{BOLD}Out of attempts.The number was {secret}{END}")
    return False

def main():
    wins = losses = 0
    while True:
        if start():
            wins += 1
        else:
            losses += 1
        print(f"{BOLD}Score — Wins: {wins}  Losses: {losses}{END}")
        play_again = input(f"{BOLD}Play again? (Y/N){END}")
        if play_again in ('Y','y'):
            print(f"{BOLD}Restarting...{END}")
        else:
            print(f"{BOLD}Initiating exit. Exiting....{END}")
            break


main()

