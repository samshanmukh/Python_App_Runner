"""Python GUI software to open all listed softwares."""

import tkinter as tk
from tkinter import filedialog, Text
import os, subprocess, sys

root = tk.Tk()
apps = []

if os.path.isfile('save.txt'):
	with open('save.txt', 'r') as f:
		tempApps = f.read()
		tempApps = tempApps.split(',')
		apps = [x for x in tempApps if x.strip()]

def addApps():
	for widget in frame.winfo_children():
		widget.destroy()

	filename = filedialog.askopenfilename(initialdir="/", title="Select File", filetypes=(("all files", "*.*"), ("executables", "*.exe")))
	apps.append(filename)
	print(filename)
	for app in apps:
		label = tk.Label(frame, text=app, bg="gray")
		label.pack()

def runApps():
	for app in apps:
		if(sys.platform == "darwin"):
			subprocess.call(["open", app])
		elif(sys.platform == "linux"):
			subprocess.call(["xdg-open", app])
		else:
			os.startfile(app)

canvas = tk.Canvas(root, height=400, width=460, bg="#263D42")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

openFile = tk.Button(root, text="Open File", padx=10, pady=5, fg="white", bg="#263D42", command=addApps)
openFile.pack()

runApps = tk.Button(root, text="Run Apps", padx=10, pady=5, fg="white", bg="#263D42", command=runApps)
runApps.pack()

for app in apps:
	label = tk.Label(frame, text=app)
	label.pack()

root.mainloop()

with open('save.txt', 'w') as f:
	for app in apps:
		f.write(app + ',')