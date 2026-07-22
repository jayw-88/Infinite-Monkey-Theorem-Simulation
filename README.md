# Infinite Monkey Theorem Simulation

A graphical simulation of the Infinite Monkey Theorem built with Python and Tkinter. Test the probability of random key presses generating specific English words or custom target strings in real-time.

---

## About the Theorem

The Infinite Monkey Theorem states that a monkey hitting keys at random on a typewriter keyboard for an infinite amount of time will almost surely type any given text—including the complete works of William Shakespeare. Given infinite time and iterations, even the most unlikely event approaches a probability of 1 (certainty).

---

## Features

- Tkinter GUI Dashboard: Multi-page graphical interface featuring custom styling and responsive controls.
- Custom Word Matching: Input any custom target word to see how many keystrokes it takes for the "monkey" to randomly generate it.
- Dictionary Filter by Length: Automatically select English words of a specific character length using an integrated dictionary file (words_alpha.txt).
- Non-blocking Multithreading: Runs background typing loops via Python's threading library to keep the GUI smoothly responsive.
- Keystroke Tracker: Displays real-time metrics showing how many random characters were typed before hitting a match.

---

## Prerequisites

- Python 3.8+
- Tkinter: Pre-installed with standard Python on Windows/macOS. On Linux, install via:

```bash
sudo apt-get install python3-tk
```

---

## Installation & Running

1. Clone the repository:

```bash
git clone [https://github.com/jayw-88/Infinite-Monkey-Theorem-Simulation.git](https://github.com/jayw-88/Infinite-Monkey-Theorem-Simulation.git)
cd Infinite-Monkey-Theorem-Simulation
```

2. Run the application:

```bash
python InfiniteMonkeyTheorem.py
```

---

## License

This project is open-source and available under the [MIT License](LICENSE).
