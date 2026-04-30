# Python CLI Number Guessing Game

### Overview
This is a fun, interactive Command Line Interface (CLI) mini-game built entirely from scratch in Python. I designed this project to practice controlling application flow, handling user input safely, and building software that runs in a continuous game loop. In this game, the user selects a difficulty level and attempts to guess a randomly generated secret number within a limited number of tries!

### What I Learned 
By building this project, I successfully implemented and understood the following core Python concepts:

* **Functions (`def`):** I structured my code into reusable blocks by separating the game logic (`start`) from the main application loop (`main`).
* **While Loop (`while True`):** I learned how to create an **infinite loop** that keeps the application running, allowing the player to keep playing new rounds and tracking their score without restarting the script.
* **For Loops(`for` loops):** I used a `for` loop combined with the `range()` function to strictly limit the player to a specific number of **attempts** (7 tries).
* **Selections (`if/elif/else`):** I routed the program's logic based on user input, using conditionals to set the **difficulty** (adjusting the max random number) and to give the player feedback on whether their guess was "Too Low" or "Too High."
* **Error Handling (`try-except`):** I implemented error catching to prevent the program from crashing. By catching a **`ValueError`**, the game gracefully handles instances where a user accidentally types a letter instead of a number.
* **Randomization (`random` module):** I imported Python's built-in `random` library and used **`randint()`** to dynamically generate a new secret number every time a round starts.
* **Terminal UI Styling (ANSI Codes):** I utilized **ANSI escape sequences** (`\033[1m`, `\033[0m`) to format the terminal output with bold text, making the game prompts stand out and feel like a real application.

### Execution
To run this application natively in your terminal, ensure you have Python installed and run the following command in the directory where your file is saved:
```bash
python number_guesser.py
```