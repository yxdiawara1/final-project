This project is a simple text-based game called the Celebrity Guessing Game. The user is asked to select how many rounds they want to play and how many clues they would like per round. A random celebrity is chosen, and the user will try to guess their name based on the clues provided. The game tracks the user's score and saves the results to a file.

**Testing Details**  
I tested the following:  
- **Input**: Ensured that inputs are handled correctly.  
- **Game Logic**: Verified that the correct number of clues is given and confirmed that the game ends appropriately, saving the scores to the `celebrity_guess_game_score.txt` file.

**Reflection**  
This project expanded my understanding of fundamental Python concepts, such as loops, conditionals, and file handling. Additionally, I explored the `datetime` module to log timestamps for each game session. One challenge I faced was handling user input to ensure that the user entered a valid number of rounds and clues. I solved this by adding a loop that checks if the input is within the acceptable range, prompting the user until they provide a valid response.