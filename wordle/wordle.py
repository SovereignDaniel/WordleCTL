import random

def main():
    win = False
    lose = 0
    wins = 0
    winRate = 0
    totalGames = 0

    while True:
        print("\nWordle!")
        print("1. Start a new game")
        print("2. Statistics")
        print("3. Credits?")
        print("4. Quit")
        choice = int(input())

        if choice == 1:
            win = start()
            if win:
                print("Congrats you won!")
                wins = wins + 1
            
            else:
                lose = lose + 1
                print("You lose!")
            
            totalGames = wins + lose
            
        if choice == 2:
            if totalGames > 0:
                winRate = (wins / totalGames) * 100

            print(f"Your winrate is {winRate}% out of {totalGames} games played")
           
        if choice == 3:
            credit()
        
        if choice == 4:
            break


def start():
    max_guesses = 6
    attempt = 0
    start = True
    win = False

    if start == True:
        print("New game started\n")
        start = False

    with open("wordle\wordList.txt") as file:
        words = [line.strip() for line in file]
        if len(words) > 0:
            random_word = random.choice(words).lower()

    while attempt < max_guesses and not win:
        print("Type in a 5 letter word")
        guess = input().lower() 

        if len(guess) != 5:
            print("Use a 5 letter word\n")
            continue
        
        elif guess == random_word:  
            win = True
            return True
            
        else:
            lc = {}
            for letter in random_word:
                lc[letter] = lc.get(letter, 0) + 1
            
            for i in range(len(guess)):
                if guess[i] == random_word[i]:
                    print("\nThe letter " + guess[i] + " is in the right position\n")
                    lc[guess[i]] -= 1
                

            wrong_letters = 0
            for i in range(len(guess)):
                if guess[i] != random_word[i] and guess[i] in lc and lc[guess[i]]:
                    print("\nThe letter " + guess[i] + " is in the word\n")
                    lc[guess[i]] -= 1
                elif guess[i] not in random_word:
                    wrong_letters += 1
            
            if wrong_letters == len(guess):
                print("No letters are right!\n")

        attempt += 1
    if attempt <= max_guesses:
        return False


def credit():
    print("This game was created by Daniel")

main()