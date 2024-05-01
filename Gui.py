import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import sys
import os
import Organizer

def browse_folder(path_entry):
    directory = filedialog.askdirectory()
    path_entry.delete(0, tk.END)
    path_entry.insert(0, directory)

def start_organizing(input_path, output_path):
    progress_bar['value'] = 0
    root.update_idletasks()

    def update_progress(value):
        print(f"Updating progress to: {value}%")
        progress_bar['value'] = value
        root.update_idletasks()

    Organizer.main_process(input_path.get(), output_path.get(), update_progress)
    
    messagebox.showinfo("Success", "Files have been organized successfully!")

root = tk.Tk()
root.title("File Organizer")
root.geometry('650x500')

if getattr(sys, 'frozen', False):
    application_path = sys._MEIPASS
else:
    application_path = os.path.dirname(os.path.abspath(__file__))
icon_path = os.path.join(application_path, 'Files.ico')
root.iconbitmap(default=icon_path)

frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

input_label = tk.Label(frame, text="Select Input Directory:")
input_label.pack(fill='x', expand=True, pady=(0, 5))
input_path = tk.Entry(frame, width=50)
input_path.pack(fill='x', expand=True, pady=(0, 5))
input_button = tk.Button(frame, text="Browse...", command=lambda: browse_folder(input_path))
input_button.pack(fill='x', expand=True, pady=(0, 10))

output_label = tk.Label(frame, text="Select Output Directory:")
output_label.pack(fill='x', expand=True, pady=(0, 5))
output_path = tk.Entry(frame, width=50)
output_path.pack(fill='x', expand=True, pady=(0, 5))
output_button = tk.Button(frame, text="Browse...", command=lambda: browse_folder(output_path))
output_button.pack(fill='x', expand=True, pady=(0, 10))

progress_bar = ttk.Progressbar(frame, orient="horizontal", length=400, mode="determinate")
progress_bar.pack(pady=(0, 10))

start_button = tk.Button(frame, text="Start Organizing", command=lambda: start_organizing(input_path, output_path))
start_button.pack(fill='x', expand=True, pady=(0, 10))

root.mainloop()
