import tkinter as tk
from tkinter import ttk

class SettingsGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Gesture Controller Settings")
        self.window.geometry("300x280")

        ttk.Label(self.window, text="Sensitivity").pack()
        self.sensitivity = ttk.Scale(self.window, from_=1, to=10)
        self.sensitivity.set(5)
        self.sensitivity.pack()

        ttk.Label(self.window, text="Smoothing").pack()
        self.smooth = ttk.Scale(self.window, from_=1, to=10)
        self.smooth.set(4)
        self.smooth.pack()

        ttk.Button(self.window, text="Save Settings", command=self.save).pack(pady=20)

        self.window.mainloop()

    def save(self):
        print("Saved settings!")
