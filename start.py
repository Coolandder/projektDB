#Uruchom program: python start.py
import tkinter as tk

import login

root = tk.Tk()
application = login.LoginWindow(root)
application.initialize_login_window()
root.mainloop()
