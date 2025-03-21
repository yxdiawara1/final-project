import random
import time
from datetime import datetime

celebrities = [
    {
        "name": "Beyonce",
        "clues": [
            "I am married to Jay-Z.",
            "I was a member of Destiny's Child.",
            "I am known as Queen Bey."
        ]
    },
    {
        "name": "Donald Trump",
        "clues": [
            "I was the president of the United States.",
            "I am a real estate developer.",
            "I was on a show called The Apprentice."
        ]
    },
    {
        "name": "Tom Hanks",
        "clues": [
            "I starred in Forest Gump.",
            "I am the voice of Woody in Toy Story.",
            "I played Captain Phillips."
        ]
    },
    {
        "name": "Ryan Reynolds",
        "clues": [
            "I am married to Blake Lively.",
            "I play Deadpool.",
            "I am a shareholder in Mint Mobile."
        ]
    },
    {
        "name": "Kevin Hart",
        "clues": [
            "I am married to a model.",
            "I am a comedian and actor.",
            "I starred in Night School."
        ]
    },
    {
        "name": "Taylor Swift",
        "clues": [
            "I am a singer-songwriter.",
            "I am known for my catchy pop songs.",
            "I have won many Grammy Awards."
        ]
    },
    {
        "name": "Dwayne Johnson",
        "clues": [
            "I am also known as 'The Rock'.",
            "I was a professional wrestler.",
            "I have starred in many action movies."
        ]
    },
    {
        "name": "Emma Watson",
        "clues": [
            "I played Hermione Granger in Harry Potter.",
            "I am an advocate for women's rights.",
            "I graduated from Brown University."
        ]
    },
    {
        "name": "Elon Musk",
        "clues": [
            "I am the CEO of Tesla and SpaceX.",
            "I am known for my innovative ideas.",
            "I am one of the richest people in the world."
        ]
    },
    {
        "name": "Oprah Winfrey",
        "clues": [
            "I have my own talk show.",
            "I am a philanthropist.",
            "I am known for my inspiring interviews."
        ]
    }
]

def play_game():
    # Starts the celebrity guessing game
    print("Welcome to 'Who am I?' - The Celebrity Guessing Game!")
    print("You'll be given clues about a celebrity, and your job is to guess who it is.")
    print("Choose how many clues you want before making a guess.")
    print("Let's get started!\n")

    player_name = input("Enter your name: ")
    score = 0

    # Input validation for num_rounds (max 10)
    while True:
        num_rounds = input("How many celebrities do you want to guess? (Maximum 10): ")
        if num_rounds.isdigit() and 1 <= int(num_rounds) <= 10:
            num_rounds = int(num_rounds)
            break
        else:
            print("Invalid input. Please enter a number between 1 and 10.")

    # Input validation for difficulty (easy/medium/hard)
    while True:
        difficulty = input("Choose difficulty (easy/medium/hard): ").strip().lower()
        if difficulty in ["easy", "medium", "hard"]:
            break
        else:
            print("Invalid input. Please choose from easy, medium, or hard.")

    print(f"Game started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    used_celebrities = []

    for round_num in range(num_rounds):
        # Select a celebrity not already used
        celeb = random.choice([c for c in celebrities if c not in used_celebrities])
        used_celebrities.append(celeb)
        print(f"\nCelebrity {round_num + 1}:")
        guessed_correctly = False
        clues_given = 0

        # change clue loop.
        for clue_index, clue in enumerate(celeb["clues"]):
            clues_given += 1
            print(f"Clue {clues_given}: {clue}")
            guess = input("Who is the celebrity? ").strip().lower()

            if guess == celeb["name"].lower():
                print("Correct!")
                score += 1
                guessed_correctly = True
                break  # Move to the next celebrity
            else:
                print("That's incorrect.")

                # Clue limit check based on difficulty
                if (difficulty == "hard" and clues_given == 1) or \
                   (difficulty == "medium" and clues_given == 2) or \
                   (clues_given == 3):  # Maximum 3 clues for easy
                    break
        if input("Need a hint? (yes/no): ").strip().lower() == "yes":
                print(f"Hint: The first letter of their name is {celeb['name'][0]}.")

        if not guessed_correctly:
            print(f"Out of clues! The correct answer was: {celeb['name']}")

           
    print("\nGame over!")
    print(f"{player_name}, your final score is: {score} out of {num_rounds}")

    # Log the final score with timestamps
    with open("celebrity_guess_game_score.txt", "a") as file:
        file.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - {player_name}: {score} out of {num_rounds}\n")

    print("Your score has been saved to the leaderboard.")
 # end game 
play_game()