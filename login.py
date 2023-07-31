import tkinter as tk

import main
import db as db
import my_config


LOGIN_WINDOW_SIZE = '400x400'
FALSE_LOG_IN_VALUE = -1


class LoginWindow:
    

    def __init__(self, master):
        
        self.master = master
        self.master.title(my_config.APP_NAME)
        self.master.geometry(LOGIN_WINDOW_SIZE)
        self.master.configure(bg=my_config.BACKGROUND)
        self.frame = tk.Frame(self.master, bg=my_config.BACKGROUND, bd=10)

        
        self.error_label = tk.Label()

      
        self.login_entry = None
        self.password_entry = None
        self.name_entry = None
        self.phone_entry = None
        self.email_entry = None
        self.first_name_entry = None
        self.second_name_entry = None
        self.position_entry = None


    def initialize_login_window(self):
        #logowanie
        if self.frame:
            self.frame.destroy()
        self.frame = tk.Frame(self.master, bg=my_config.BACKGROUND, bd=20)

        #label
        login_label = tk.Label(self.frame, bg=my_config.BACKGROUND, text='Login:')
        login_label.grid(row=0, column=0, pady=(0, 5))
        password_label = tk.Label(self.frame, bg=my_config.BACKGROUND, text='Hasło:')
        password_label.grid(row=1, column=0)
        self.login_entry = tk.Entry(self.frame, bg=my_config.FOREGROUND, width=22)
        self.login_entry.grid(row=0, column=1, pady=(0, 5))
        self.password_entry = tk.Entry(self.frame, show='*', bg=my_config.FOREGROUND, width=22)
        self.password_entry.grid(row=1, column=1)

        # buttons
        login_button = tk.Button(self.frame, text='Logowanie', bg=my_config.FOREGROUND,
                                 command=self.login, width=16)
        login_button.grid(row=3, column=1, pady=(20, 0))
        create_button = tk.Button(self.frame, text='Rejestracja',
                                  bg=my_config.FOREGROUND, command=self.create_account, width=16)
        create_button.grid(row=4, column=1)
        self.frame.pack()

    def login(self):
        
        if self.error_label:
            self.error_label.destroy()

        #sprawdzenie
        if not self.login_entry.get():
            self.error_label = tk.Label(self.frame, text="Błędny login",
                                        fg=my_config.ERROR_FOREGROUND, bg=my_config.BACKGROUND)
            self.error_label.grid(row=2, column=1)
        elif not self.password_entry.get():
            self.error_label = tk.Label(self.frame, text="Błędne hasło",
                                        fg=my_config.ERROR_FOREGROUND, bg=my_config.BACKGROUND)
            self.error_label.grid(row=2, column=1)

        else:
            my_config.MY_ID, perm = db.user_perm(self.login_entry.get(), self.password_entry.get())
            if perm == FALSE_LOG_IN_VALUE or my_config.MY_ID == FALSE_LOG_IN_VALUE:
                self.error_label = tk.Label(self.frame, text="Błędne logowanie",
                                            fg=my_config.ERROR_FOREGROUND, bg=my_config.BACKGROUND)
                self.error_label.grid(row=2, column=1)
            elif perm == my_config.ADMIN_PERM:
                self.main_app()
            else:
                self.user_app()

    def create_account(self):
        #nowe konto
        self.frame.destroy()
        self.frame = tk.Frame(self.master, bg=my_config.BACKGROUND)
        self.frame.pack()

        #label
        login_label = tk.Label(self.frame, text='Login:', bg=my_config.BACKGROUND)
        login_label.grid(row=0, column=0, pady=(10, 0), sticky=tk.E)
        password_label = tk.Label(self.frame, text='Hasło:', bg=my_config.BACKGROUND)
        password_label.grid(row=1, column=0, sticky=tk.E, )
        first_name_label = tk.Label(self.frame, text='Imię:', bg=my_config.BACKGROUND)
        first_name_label.grid(row=2, column=0, sticky=tk.E)
        second_name_label = tk.Label(self.frame, text='Nazwisko:', bg=my_config.BACKGROUND)
        second_name_label.grid(row=3, column=0, sticky=tk.E)
        postion_label = tk.Label(self.frame, text='Stanowisko:', bg=my_config.BACKGROUND)
        postion_label.grid(row=4, column=0, sticky=tk.E)
        email_label = tk.Label(self.frame, text='Email:', bg=my_config.BACKGROUND)
        email_label.grid(row=5, column=0, sticky=tk.E)

        
        self.login_entry = tk.Entry(self.frame, width=18, bg=my_config.FOREGROUND)
        self.login_entry.grid(row=0, column=1, pady=(10, 0))
        self.password_entry = tk.Entry(self.frame, width=18, show='*', bg=my_config.FOREGROUND)
        self.password_entry.grid(row=1, column=1, pady=(10, 0))
        self.first_name_entry = tk.Entry(self.frame, width=18, bg=my_config.FOREGROUND)
        self.first_name_entry.grid(row=2, column=1, pady=(10, 0))
        self.second_name_entry = tk.Entry(self.frame, width=18, bg=my_config.FOREGROUND)
        self.second_name_entry.grid(row=3, column=1, pady=(10, 0))
        self.position_entry = tk.Entry(self.frame, width=18, bg=my_config.FOREGROUND)
        self.position_entry.grid(row=4, column=1, pady=(10, 0))
        self.email_entry = tk.Entry(self.frame, width=18, bg=my_config.FOREGROUND)
        self.email_entry.grid(row=5, column=1, pady=(10, 0))

        
        login_button = tk.Button(self.frame, text='Załóż konto', command=self.create_account_db,
                                 width=20, bg=my_config.FOREGROUND)
        login_button.grid(row=7, column=0, pady=(20, 0))
        create_button = tk.Button(self.frame, text='Logowanie', command=self.initialize_login_window,
                                  width=20, bg=my_config.FOREGROUND)
        create_button.grid(row=7, column=1, pady=(20, 0))

    def create_account_db(self):
        #rejestracja
        if self.error_label:
            self.error_label.destroy()

        #sprawdzenie
        if not self.login_entry.get():
            self.error_label = tk.Label(self.frame, text="Błędny login",
                                        fg=my_config.ERROR_FOREGROUND, bg=my_config.BACKGROUND)
            self.error_label.grid(row=6, column=1)
        elif len(self.password_entry.get()) < 8:
            self.error_label = tk.Label(self.frame, text="Hasło musi mieć min. 8 znaków",
                                        fg=my_config.ERROR_FOREGROUND, bg=my_config.BACKGROUND)
            self.error_label.grid(row=6, column=1)
        elif not self.first_name_entry.get():
            self.error_label = tk.Label(self.frame, text="Błąd imienia",
                                        fg=my_config.ERROR_FOREGROUND, bg=my_config.BACKGROUND)
            self.error_label.grid(row=6, column=1)
        elif not self.second_name_entry.get():
            self.error_label = tk.Label(self.frame, text="Błąd imienia",
                                        fg=my_config.ERROR_FOREGROUND, bg=my_config.BACKGROUND)
            self.error_label.grid(row=6, column=1)    
        elif not self.email_entry.get():
            self.error_label = tk.Label(self.frame, text="Błąd email",
                                        fg=my_config.ERROR_FOREGROUND, bg=my_config.BACKGROUND)
            self.error_label.grid(row=6, column=1)
        
        else:
            # szukanie w bazie
            exist = db.is_user_exists(self.login_entry.get(), self.email_entry.get())
            if exist == my_config.CUSTOMER_EMAIL:
                self.error_label = tk.Label(self.frame, text="Email zajęty.".format(exist),
                                            fg=my_config.ERROR_FOREGROUND, bg=my_config.BACKGROUND)
                self.error_label.grid(row=6, column=1)

            elif exist == my_config.CUSTOMER_LOGIN:
                self.error_label = tk.Label(self.frame, text="Login zajęty.".format(exist),
                                            fg=my_config.ERROR_FOREGROUND, bg=my_config.BACKGROUND)
                self.error_label.grid(row=5, column=1)
            else:
                db.add_user(self.login_entry.get(), self.password_entry.get(),
                                self.first_name_entry.get(), self.second_name_entry.get(),
                                self.position_entry.get(), self.email_entry.get())
                self.frame.destroy()
                application = LoginWindow(self.master)
                application.initialize_login_window()

    def main_app(self):
        #admin
        self.frame.destroy()
        application = main.CarsMenu(self.master)
        application.initialize_menu()

    def user_app(self):
        #user
        self.frame.destroy()
        application = main.CarsMenu(self.master)
        application.initialize_menu()      
