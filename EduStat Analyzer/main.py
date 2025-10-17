from tkinter import *
from tkinter import filedialog
import numpy as np

THEME_COLOR = "#698C9E"

# Creating window

window = Tk()
window.title("EduStat Analyzer")
window.config(padx=20, pady=20, bg=THEME_COLOR)

# Title label

title_label = Label(window, text="EduStat Analyzer", fg="white", bg=THEME_COLOR, font=("Arial", 40))
title_label.grid(row=0, column=0, pady=20, columnspan=2)

# Institute name

institute_label = Label(window, text="Institute Name:", fg="white", bg=THEME_COLOR, font=("Arial", 25))
institute_label.grid(row=1, column=0, sticky="e")
institute_name = Entry(window, width=30)
institute_name.grid(row=1, column=1, pady=10)

# Institute class

institute_class_label = Label(window, text="Institute Class:", fg="white", bg=THEME_COLOR, font=("Arial", 25))
institute_class_label.grid(row=2, column=0, sticky="e")
institute_class = Entry(window, width=30)
institute_class.grid(row=2, column=1, pady=10)

# Data file selector

data_file_label = Label(window, text="Data File:", fg="white", bg=THEME_COLOR, font=("Arial", 25))
data_file_label.grid(row=3, column=0, sticky="e")

file_path_var = StringVar()
file_entry = Entry(window, textvariable=file_path_var, width=30)
file_entry.grid(row=3, column=1, pady=10, sticky="w")

def browse_file():
  file_path = filedialog.askopenfilename(title="Select Data File", filetypes=[("CSV Files", "*.csv"), ("All Files", "*.*")])
  file_path_var.set(file_path)

browse_button = Button(window, text="Browse", command=browse_file)
browse_button.grid(row=3, column=2, padx=10)

# Generate Stats button

def generate_stats():
  print("Institue Name : ",institute_name.get())
  print("Institue class : ",institute_class.get())
  #made numpy array...
  data = np.loadtxt(file_entry.get(), delimiter=",", skiprows=1, usecols=5)
  print(data)
  # mean
  print("Mean marks of class : ", np.mean(data)) 
  # median
  print("Meadian marks of class : ", np.median(data)) 
  # highest marks
  print("Highest marks of class : ", np.max(data))
  # lowest marks
  print("Lowest marks of class : ", np.min(data))
  # pass count
  pass_count = 0
  fail_count = 0
  for i in data:
    if i > 180:
      pass_count += 1
    else:
      fail_count += 1
  print("Pass count of class : ", pass_count)
  # fail count
  print("Fail count of class : ", fail_count)  

# Placeholder for future NumPy analysis logic

generate_button = Button(window, text="Generate Stats", command=generate_stats, font=("Arial", 20), bg="white")
generate_button.grid(row=4, column=0, columnspan=3, pady=30)

# Run window

window.mainloop()
