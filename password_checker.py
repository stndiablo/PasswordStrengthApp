import tkinter as tk
from tkinter import ttk, messagebox
import re
import random
import string

def check_strength(password):
    feedback = []
    score = 0

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Use at least 8 characters")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add an uppercase letter")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add a lowercase letter")

    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Add a number")

    if re.search(r"[!@#$%^&*()_+]", password):
        score += 1
    else:
        feedback.append("Add a special character")

    return score, feedback

def evaluate_password(event=None):
    password = entry.get()
    score, feedback = check_strength(password)

    levels = ["Very Weak", "Weak", "Medium", "Good", "Strong", "Very Strong"]
    colors = ["red", "orangered", "orange", "gold", "yellowgreen", "green"]

    strength_bar["value"] = score * 20
    strength_label.config(text=levels[score], fg=colors[score])
    tips.config(text="\n".join(feedback) if feedback else "Great password!")

def toggle_password():
    if entry.cget('show') == '':
        entry.config(show='*')
        toggle_btn.config(text='Show')
    else:
        entry.config(show='')
        toggle_btn.config(text='Hide')

def generate_password():
    characters = string.ascii_letters + string.digits + "!@#$%^&*()_+"
    new_password = ''.join(random.choice(characters) for _ in range(12))
    entry.delete(0, tk.END)
    entry.insert(0, new_password)
    evaluate_password()

def suggest_password():
    name = "Abhinav"
    suggestion = name.capitalize() + "@" + str(random.randint(1000, 9999))
    messagebox.showinfo("Suggestion", f"Try: {suggestion}")

# GUI Setup
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("420x330")
root.resizable(False, False)
root.configure(bg="white")

tk.Label(root, text="Enter Password", font=("Arial", 14), bg="white", fg="black").pack(pady=10)

frame = tk.Frame(root, bg="white")
frame.pack()

entry = tk.Entry(frame, show="*", font=("Arial", 14), width=25, fg="black", bg="white")
entry.pack(side=tk.LEFT, padx=5)
entry.bind("<KeyRelease>", evaluate_password)

toggle_btn = tk.Button(frame, text="Show", command=toggle_password)
toggle_btn.pack(side=tk.LEFT)

generate_btn = tk.Button(root, text="Generate Password", command=generate_password)
generate_btn.pack(pady=5)

suggest_btn = tk.Button(root, text="Suggest Based on Name", command=suggest_password)
suggest_btn.pack(pady=5)

strength_label = tk.Label(root, text="Strength", font=("Arial", 12), bg="white", fg="black")
strength_label.pack(pady=5)

strength_bar = ttk.Progressbar(root, length=250, maximum=100)
strength_bar.pack(pady=5)

tips = tk.Label(root, text="", font=("Arial", 10), fg="gray", bg="white")
tips.pack(pady=10)

root.mainloop()
