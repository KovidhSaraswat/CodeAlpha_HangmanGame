# 🎮 Hangman Game - Python Implementation

A lightweight, terminal-based implementation of the classic Hangman word-guessing game built with Python[cite: 1]. Developed as part of the **CodeAlpha Python Programming Internship**[cite: 1, 3].

---

## 📌 Project Overview
This program randomly selects a secret word from a predefined list and challenges the user to guess it one letter at a time[cite: 1]. The user is given up to **6 incorrect attempts** before the game ends[cite: 1].

### Key Features
* 🎲 **Random Word Selection**: Built using Python's `random` module[cite: 1].
* 🛡️ **Input Validation**: Prevents duplicate guesses, multi-letter inputs, and non-alphabetic characters.
* 📊 **Dynamic Status Display**: Shows guessed letters, remaining attempts, and masked word state after every move.

---

## 🛠️ Tech Stack & Concepts Used
* **Language**: Python 3.x[cite: 1, 3]
* **Core Concepts**: `random` module, `while` loops, `if-else` branching, string manipulation, list iteration[cite: 1].

---

## 🚀 How to Run

1. **Clone the repository**:
   ```bash
   git clone [https://github.com/YOUR_GITHUB_USERNAME/CodeAlpha_HangmanGame.git](https://github.com/YOUR_GITHUB_USERNAME/CodeAlpha_HangmanGame.git)
   cd CodeAlpha_HangmanGame

2. Run the script:
   python hangman.py

3. OUTPUT Preview:
      === Welcome to Hangman Game ===

Word: _ _ _ _ _ _
Attempts remaining: 6
Guess a letter: p

Good job! 'p' is in the word.

Word: p _ _ _ _ _
Attempts remaining: 6
Guess a letter: e

Wrong guess! 'e' is not in the word.

Word: p _ _ _ _ _
Attempts remaining: 5
Guess a letter: y

Good job! 'y' is in the word.

Word: p y _ _ _ _
Attempts remaining: 5
Guess a letter: t

Good job! 't' is in the word.

Word: p y t _ _ _
Attempts remaining: 5
Guess a letter: h

Good job! 'h' is in the word.

Word: p y t h _ _
Attempts remaining: 5
Guess a letter: o

Good job! 'o' is in the word.

Word: p y t h o _
Attempts remaining: 5
Guess a letter: n

Good job! 'n' is in the word.

🎉 Congratulations! You guessed the word correctly!
