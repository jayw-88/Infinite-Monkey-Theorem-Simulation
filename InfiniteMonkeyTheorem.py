import string
import random
import threading
from pathlib import Path

import tkinter as tk
from tkinter import ttk

# Initialization
SCRIPT_DIR = Path(__file__).parent.resolve()
monkey_path = SCRIPT_DIR / 'Monkey.png'

SCRIPT_DIR = Path(__file__).parent.resolve()
file_path = SCRIPT_DIR / 'words_alpha.txt'

alphabet = string.ascii_letters
length = 0
words = []

# Functions
def masterfont(x):
    return ("Comic Sans MS", x)

# Classes
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Infinite Monkey Theorem")
        self.geometry("1300x775")
        self.resizable(False,False)
        self.lift()
        
        container = tk.Frame(self)
        container.pack(fill = "both", expand = False)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        
        # Theming
        style = ttk.Style(self)
        style.theme_use("clam")

        # Styles
        style.configure(
            "Regular.TButton",
            foreground = "white",
            background = "#1E1E1E",
            font = masterfont(24),
            )

        style.configure(
            "Exit.TButton",
            width = 2,
            height = 8,
            foreground = "black",
            background = "red",
            font = masterfont(12),
            )
        
        style.configure(
            "Back.TButton",
            width = 2,
            height = 8,
            foreground = "white",
            background = "#1E1E1E",
            font = masterfont(24),
            )
        
        style.configure(
            "Entry.TButton",
            foreground = "white",
            background = "#1E1E1E",
            font = masterfont(22),
        )
        
        style.map(
            "Regular.TButton",
            background=[("pressed", "#222222"), ("active", "#333333")],
            foreground=[("pressed", "white"), ("active", "white")]
        )
        
        style.map(
            "Exit.TButton",
            background=[("pressed", "#FF6767"), ("active", "#FF4F4F")],
            foreground=[("pressed", "black"), ("active", "black")]
        )
        
        style.map(
            "Back.TButton",
            background=[("pressed", "#222222"), ("active", "#333333")],
            foreground=[("pressed", "white"), ("active", "white")]
        )
        
        style.map(
            "Entry.TButton",
            background=[("pressed", "#222222"), ("active", "#333333")],
            foreground=[("pressed", "white"), ("active", "white")]
        )
        
        self.frames = {}
        
        for Page in (StartPage, SimulationPage):
            frame = Page(container, self)
            self.frames[Page] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        
        self.show_frame(StartPage)
        
    def show_frame(self, page_class):
        frame = self.frames[page_class]
        frame.tkraise()

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        
        # Labels & Images
        title = tk.Label(self,
                        text = "Infinite Monkey Theorem Simulation",
                        font = masterfont(36))

        desc = tk.Label(self,
                        text = "The infinite monkey theorem states that if you have a monkey randomly hitting keys on a keyboard for an infinite amount of time, it will\nbe able to type any given text, including the complete works of William Shakespeare. This theorem illustrates the concept of \nrandomness and infinity, suggesting that given enough time, even the most unlikely events can occur.",
                        font = masterfont(20))

        self.monkey_image = tk.PhotoImage(file = monkey_path)
        monkey_label = tk.Label(self, image = self.monkey_image)

        sim = tk.Label(self,
                    text = "This simulation lets you simulate this theorem and also adjust different parameters\nof the simulation to your own preference.",
                    font = masterfont(20))

        # Buttons
        start_button = ttk.Button(self, 
                                text = "Simulate",
                                command = lambda: controller.show_frame(SimulationPage),
                                style = "Regular.TButton")

        exit_button = ttk.Button(self, 
                                text = "X",
                                command = lambda: controller.destroy(),
                                style = "Exit.TButton")
        
        # Packing & Placing
        title.pack(pady = 10)
        desc.pack()
        monkey_label.pack(pady = 20)
        sim.pack(pady = 10)
        start_button.pack(pady = 10)
        exit_button.place(x = 1267, y = 0)

class SimulationPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        
        # Labels
        title = tk.Label(self, 
                               text = "Simulation Variables",
                               font = masterfont(36))
        word_length_label = tk.Label(self,
                                     text = "Word Length",
                                     font = masterfont(30))
        custom_word_label = tk.Label(self,
                                     text = "Custom Word",
                                     font = masterfont(30))
        self.found_label = tk.Label(self,
                            text = "",
                            font = masterfont(24))
        
        # Buttons
        self.start_simulation_button = ttk.Button(self,
                                             text = "Start Simulation",
                                             command = lambda: self.start_simulation(),
                                             style = "Regular.TButton")
        back_button = ttk.Button(self,
                                             text = "<-",
                                             command = lambda: controller.show_frame(StartPage),
                                             style = "Back.TButton")
        
        # Entries
        self.word_length_entry = tk.Entry(self, 
                                     width = 30, 
                                     font = masterfont(27))
        self.custom_word_entry = tk.Entry(self, 
                                     width = 30, 
                                     font = masterfont(27))
        
        # Packing & Placing
        title.pack(pady = 10)
        word_length_label.place(x = 190, y = 82.5)
        custom_word_label.place(x = 190, y = 155)
        back_button.place(x = 0, y = 0)
        self.word_length_entry.pack(pady = 10)
        self.custom_word_entry.pack(pady = 10)
        self.start_simulation_button.pack(pady = 10)
        self.found_label.pack(pady = 10)
        
    def no_input_popup(self):
        self.no_input = tk.Frame(self,
                                        bg = "#333333", 
                                        bd = 2, 
                                        relief = "solid", 
                                        width = 365, 
                                        height = 75)
        
        # Labels & Buttons
        no_input_label = tk.Label(self.no_input,
                                    text = "Please input all values.",
                                    font = masterfont(26))
        exit_button = ttk.Button(self.no_input,
                                    text = "X",
                                    command = lambda: self.no_input.destroy(),
                                    style = "Exit.TButton")

        # Placing
        self.no_input.place(x = 475, y = 350)
        no_input_label.place(x = 42, y = 8.5)
        exit_button.place(x = 330, y = 0)
        
    def start_simulation(self):
        words.clear()
        
        try:
            self.length = int(self.word_length_entry.get())
            length_bool = True
        except:
            length_bool = False
        
        self.custom_word = self.custom_word_entry.get()
        if not self.custom_word == "":
            custom_word_bool = True
        else:
            custom_word_bool = False
        
        if length_bool and not custom_word_bool:
            self.run_simulation = True
            self.custom_word_run = False
        elif not length_bool and custom_word_bool:
            self.run_simulation = True
            self.custom_word_run = True
        else:
            self.run_simulation = False
            self.no_input_popup()
            
        if self.run_simulation: 
            if self.custom_word_run:
                words.append(self.custom_word)
            else:
                dict_file = open(file_path,"r")
                for line in dict_file:
                    skip = False
                    isolated_word = line.strip()
                    if len(isolated_word) < self.length:
                        skip = True
                    if not skip:
                        words.append(isolated_word)
        
        self.start_simulation_button.config(state="disabled")
        
        thread = threading.Thread(
                target = self.run_monkey_simulation, daemon=True
        )
        thread.start()
    def run_monkey_simulation(self):
        found = False
        inf_string = ""
        self.typed = 0

        while not found:
            inf_string += random.choice(alphabet)
            self.typed += 1
            for item in words:
                if inf_string.endswith(item):
                    found = True
                    result = f"Found English word {item} after {self.typed} typed keys."
                    self.after(
                        0, lambda msg = result: self.finish_simulation(msg)
                    )
                    break
        
    def finish_simulation(self, result):
        self.found_label.config(text = result)
        self.start_simulation_button.config(state = "normal")

if __name__ == "__main__":
    App().mainloop()