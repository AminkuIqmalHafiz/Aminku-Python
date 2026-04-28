# Python CLI Interactive Calculator

### Overview
This is a lightweight, interactive Command Line Interface (CLI) calculator built entirely from scratch in Python. I designed this project to transition from writing basic, top-to-bottom scripts to building dynamic software that runs continuously and interacts with the user.

### What I Learned 
By building this project, I successfully implemented and understood the following core Python concepts:

* **Functions (`def`):** I moved away from writing repetitive code by turning them into function(`addition`, `substract`, `multiply`, `division`).
* **While Loop (`while True`):** I learned how to create an infinite loop that keeps the application running so the user can perform multiple calculations without having to restart the script every time.
* **Selection (`if/elif/else`):** I routed the program's logic based on user input, allowing the script to dynamically choose which math function to execute or whether to exit the loop.
* **Error Handling (`try-except`):** I implemented error catching to prevent the program from crashing. For example, exception on the `ValueError` and `ZeroDivisionError`help caught errors smoothly, and the loop continues.
* **Type Casting(`input` & `float`):** I learned how to pause the script to collect user input, and critically, how to convert that text input into floating-point numbers so the computer can perform actual math on them.
* **Terminal UI Styling (ANSI Codes):** I utilized ANSI escape sequences (`\033[1m`, `\033[31m`) to format the terminal output with bold text and red warning colors, making the CLI feel like a real application.

### Execution
To run this application natively in your terminal, ensure you have Python installed and run:
```bash
python cli_calculator.py