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
