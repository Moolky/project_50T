import tkinter as tk
import config_window

root = tk.Tk()
root.title("Data Processing Window")

def open_config_window():
    config_window.config_win()


def close_config_window():
    config_window.root.destroy()

open_config_button = tk.Button(root, text="Open Config Window", command=open_config_window)
open_config_button.pack()

close_config_button = tk.Button(root, text="Close Config Window", command=close_config_window)
close_config_button.pack()


root.mainloop()