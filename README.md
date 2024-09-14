# Wordle Game in Python

This project is a simple **Wordle game** built using Python's Tkinter library.

## Features
- **Interactive GUI** with Tkinter.
- Feedback on guesses using **green**, **yellow**, and **red** color codes.
- Character tracking for already guessed letters.

## How to Play
1. **Enter a 5-letter word** in the input box.
2. After each guess, letters will be color-coded:
   - 💚 **Green** if the letter is in the correct position.
   - 💛 **Yellow** if the letter is in the word but wrong position.
   - ❤️ **Red** if the letter is not in the word.

3. You have **6 attempts** to guess the correct word.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/wordle-game.git
   cd wordle-game
    ```

2. Install any required dependencies:
    Tkinter is usually included with Python, but you can ensure it’s installed by running:
    ```bash
    pip install tk
    ```

3. Run the game:
    ```bash
    python wordle_game.py
    ```

---

## How to Play

1. **Start the game**: Run the Python script and the game window will open.
2. **Guess a word**: Enter a 5-letter word in the input box.
3. **Feedback**: Each letter in the word will be highlighted:
   - **💚 Green** if the letter is in the correct position.
   - **💛 Yellow** if the letter is in the word but in the wrong position.
   - **❤️ Red** if the letter is not in the word at all.
4. **Character Tracking**: The game will show all possible characters at the top, and will cross out the ones you’ve guessed already.
5. **Attempts**: You have six attempts to guess the correct word.

---

## Game Rules

- You must guess a **5-letter word**.
- For each guess, the game provides color-coded feedback:
  - **Green**: Correct letter in the correct position.
  - **Yellow**: Correct letter in the wrong position.
  - **Red**: Letter not in the word.
- You have **six attempts** to guess the correct word.

---

## Project Structure

```bash
├── WORDLE
│   ├── WORDLE.py
│   ├── README.MD
│   ├── word.txt #contains all words for the file


```

## Contributing

Contributions are welcome! Here's how you can help:
1. Fork the repository.
2. Create a new feature branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Additional Notes

- This game is inspired by the popular online Wordle game. It is a personal project for learning Python and Tkinter.
- The word list is sourced from common 5-letter English words, but you can modify `words.txt` to include your own list of words.

---

### Acknowledgments
- The original [Wordle](https://www.powerlanguage.co.uk/wordle/) game for inspiration.
- The Python community for excellent resources on Tkinter.

