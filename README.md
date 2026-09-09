# Password Validator in Python

A lightweight Python script that handles password authentication with retry limits, attempt tracking, and standard control flow mechanisms.

## Features

* **Attempt Limiting:** Restricts the user to a set number of password attempts.
* **Dynamic Feedback:** Adjusts pluralization and status messages based on remaining tries.
* **Execution Control:** Terminates process flow upon reaching the attempt limit using a standard `while-else` structure.

## Usage

Run the script directly using Python 3:

```bash
python main.py

```

## How It Works

1. Prompts the user to enter a password.
2. Compares input against the stored password.
3. Decrements the attempt count on each failure.
4. Outputs warning messages with remaining tries.
5. Exits gracefully on success or lockout.
