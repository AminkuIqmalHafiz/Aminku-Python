# Python Data Validator & Sanitizer 

### Overview
This is a robust, terminal-based data validation script built entirely from scratch in Python. I designed this project to practice data , type checking. Instead of assuming data is always clean, this script processes a mock database of customer orders (a list of dictionaries) and strictly evaluates them against a set of flagging missing keys, incorrect data types, and invalid formats.

### What I Learned 
By building this project, I successfully implemented and understood the following core Python concepts:

* **Functions (`def`):** I structured my code to separate the high-level iteration logic (`validate`) from the granular, specific business rules (`validation_rule`), keeping the code clean and scalable.
* **Type Checking (`isinstance`):** I used the built-in `isinstance()` function to strictly enforce data types, ensuring that prices are numbers (`int` or `float`), items are lists, and emails are strings.
* **Set Operations (`set`):** I learned how to cast dictionary keys into a `set` to perform lightning-fast comparisons against a predefined "schema" (`key_set`). This instantly catches if an order is missing a required field or has unexpected extra fields.
* **Standard Library (`re` module):** I imported Python's built-in `re` library and utilized `re.fullmatch()` and `re.IGNORECASE` to enforce specific string patterns (like checking the format of an Order ID).
* **Dictionary Unpacking (`**`):** I used the double-asterisk `**` operator to elegantly unpack a dictionary's key-value pairs and pass them directly as keyword arguments into my validation function (`validation_rule(**dictionary)`).
* **List Comprehensions:** I learned how to write clean, one-line `for` loops inside brackets to quickly filter and return the specific keys that failed validation `[key for key, value in ... if not value]`.
* **Enumeration (`enumerate`):** Instead of just using a standard `for` loop, I used `enumerate()` to track the exact index of the loop. This allowed me to print highly specific error messages telling the user *exactly* which record (position) failed.

### Execution
To run this application natively in your terminal, ensure you have Python installed and run the following command in the directory where your file is saved:
```bash
python order_validator.py