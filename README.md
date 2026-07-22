# Infinite Monkey Theorem Simulation

A graphical simulation of the Infinite Monkey Theorem built with Python and Tkinter. This application lets you test the probability of random key presses generating specific English words or custom target strings in real-time.

---

## About the Theorem

The Infinite Monkey Theorem states that a monkey hitting keys at random on a typewriter keyboard for an infinite amount of time will almost surely type any given text—including the complete works of William Shakespeare.

While the probability of generating even a short word or sentence by pure chance is extraordinarily low, given infinite time and iterations, even the most unlikely event approaches a probability of 1 (certainty). This simulation brings that theoretical concept into an interactive visual GUI application!

---

## Features

- Tkinter GUI Dashboard: Multi-page graphical interface featuring custom styling, dark themes, and responsive controls.
- Custom Word Matching: Input any custom target word to see how many keystrokes it takes for the "monkey" to randomly generate it.
- Dictionary Filter by Length: Automatically select English words of a specific character length using an integrated dictionary file (words_alpha.txt).
- Non-blocking Multithreading: Runs background typing loops via Python's threading library, keeping the GUI smoothly responsive during computation.
- Keystroke Tracker: Displays real-time metrics showing how many random characters were typed before hitting a match.

---

## Prerequisites

- Python 3.8+
- Tkinter: Usually pre-installed with standard Python distributions on Windows and macOS. On Ubuntu/Debian Linux, install via:

```bash
sudo apt-get install python3-tk
```

---

## Installation & Setup

### 1. Clone the Repository

Clone this repository to your local machine:

```bash
git clone [https://github.com/jayw-88/Infinite-Monkey-Theorem-Simulation.git](https://github.com/jayw-88/Infinite-Monkey-Theorem-Simulation.git)
cd Infinite-Monkey-Theorem-Simulation
```

### 2. Verify File Structure

Ensure all necessary project files are present in the directory:

```text
Infinite-Monkey-Theorem-Simulation/
│
├── InfiniteMonkeyTheorem.py   # Main Python Tkinter application
├── Monkey.png                # Graphic asset for the start page
├── words_alpha.txt           # Dictionary dataset for English words
└── README.md                 # Project documentation
```

---

## Usage Guide

1. Launch the Application:
   Execute the python script from your terminal:
   ```bash
   python InfiniteMonkeyTheorem.py
   ```
   *(Or python3 InfiniteMonkeyTheorem.py depending on your environment)*

2. Navigate to Simulation:
   Click the Simulate button on the home screen.

3. Set Simulation Parameters:
   - Option A (Custom Word): Enter your target word into the Custom Word text field.
   - Option B (Word Length): Enter a number in the Word Length field to search for any matching English word of that length from words_alpha.txt.

4. Start the Simulation:
   Click Start Simulation. The algorithm will randomly select ASCII letters in the background until your target string is matched!

---

## How It Works

1. Random Generation: Letters are sampled at random from string.ascii_letters (a-z, A-Z).
2. Background Computation: The main interface delegates computation to a secondary thread so the UI remains interactive during long typing sequences:
   ```python
   while not found:
       inf_string += random.choice(alphabet)
       typed += 1
       for item in words:
           if inf_string.endswith(item):
               found = True
               ...
   ```
3. Thread-Safe UI Updates: Once a match is made, self.after() schedules GUI updates back on the main thread safely.

---

## License

This project is open-source and available under the [MIT License](LICENSE).
