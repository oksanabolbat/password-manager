import tkinter as tk

window = tk.Tk()
window.minsize(width=240, height=240)
window.config(pady=20, padx=20, bg="#fff")
window.title("Password manager")


bg_canvas = tk.Canvas(width=200, height=200, bg="#fff",highlightthickness=0)
bg_image = tk.PhotoImage(file="logo.png")
bg_canvas.create_image(100, 100, image=bg_image)
bg_canvas.grid(row=1,column=1)
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window.mainloop()