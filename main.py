from tkinter import messagebox
import tkinter as tk
from tkinter.ttk import Treeview

import db as db
import login
import my_config

MAIN_WINDOW_SIZE = "1200x800"

CLIENT_COLUMNS = ('Id', 'Nazwa', 'NIP', 'Ulica', 'Kod', 'Miasto')
CLIENT_COLUMNS_SIZE = (25, 200, 100, 120, 60, 100)

CLIENT_COLUMNS_FULL = ('Id', 'Nazwa', 'NIP', 'Telefon', 'Email', 'Ulica','Nr domu','Nr lokalu', 'Kod', 'Miasto')
CLIENT_COLUMNS_FULL_SIZE = (25, 200, 100, 100, 100, 100, 25, 25, 50, 80)

AUTO_COLUMN_FULL = ('Id', 'Nr rej.', 'Marka i model', 'Rocznik', 'Dostępność')
AUTO_COLUMN_FULL_SIZE = (25, 120, 150, 90, 100)

CAR_COLUMNS = ('Id', 'Nr rej.', 'Marka i model', 'Cena')
CAR_COLUMNS_SIZE = (25, 120, 150, 90)

PRODUCT_COLUMNS = ('Id', 'Produkt', 'Cena jed.', 'Dostępne', 'Opis')
PRODUCT_COLUMNS_SIZE = (25, 120, 50, 50, 130)

ORDER_COLUMNS = ('Id', 'Data zamówienie', 'Data wypożyczenia', 'Termin zwrotu', 'Rabat', 'Uwagi')
ORDER_COLUMNS_SIZE = (25, 100, 100, 100, 50, 200)

class CarsMenu:
    

    def __init__(self, master):
        
        self.master = master
        self.master.geometry(MAIN_WINDOW_SIZE)
        self.master.configure(bg=my_config.BACKGROUND)
        self.master.title(my_config.APP_NAME)

        
        self.frame = tk.Frame(self.master, bg=my_config.BACKGROUND)
        self.frame.pack()
       
        self.entry_frame = tk.Frame(self.master, bg=my_config.BACKGROUND)
        self.entry_frame.pack()
        
        self.listbox_frame = tk.Frame(self.master, bg=my_config.BACKGROUND)
        self.listbox_frame.pack()

        self.error_label = tk.Label()

        self.cars_tree = None
        self.login_entry = None
        self.email_entry = None
        self.phone_entry = None
        self.name_entry = None
        self.perm_entry = None
        self.id_auta_entry = None
        self.rejstracja_entry = None
        self.marka_entry = None
        self.rocznik_entry = None
        self.dostepnosc_entry = None

    def initialize_menu(self):
        
        self.frame.destroy()
        self.frame = tk.Frame(self.master, bg=my_config.BACKGROUND)
        self.frame.pack()

        self.entry_frame.destroy()
        self.entry_frame = tk.Frame(self.master, bg=my_config.BACKGROUND)
        self.entry_frame.pack()

        self.listbox_frame.destroy()
        self.listbox_frame = tk.Frame(self.master, bg=my_config.BACKGROUND)
        self.listbox_frame.pack()

        if self.error_label:
            self.error_label.destroy()

        
        auto_button = tk.Button(self.frame, text='Auta', command=self.initialize_menu,
                                    width=30, bg=my_config.FOREGROUND)
        auto_button.grid(row=0, column=0, pady=10)
        order_button = tk.Button(self.frame, text='Rezerwacja', command=self.go_to_order_window,
                                 width=30, bg=my_config.FOREGROUND)
        order_button.grid(row=0, column=1, )
        product_button = tk.Button(self.frame, text='Klienci', command=self.go_to_client_window,
                                   width=30, bg=my_config.FOREGROUND)
        product_button.grid(row=0, column=2)
        exit_button = tk.Button(self.frame, text='Wyloguj', command=self.exit_main_window,
                                width=30, bg=my_config.FOREGROUND)
        exit_button.grid(row=0, column=3)

        #label
        id_label = tk.Label(self.entry_frame, text='Nr ID:', bg=my_config.BACKGROUND)
        id_label.grid(row=1, column=0, sticky=tk.E)
        rej_label = tk.Label(self.entry_frame, text='Nr rej.:', bg=my_config.BACKGROUND)
        rej_label.grid(row=2, column=0, sticky=tk.E)
        marka_label = tk.Label(self.entry_frame, text='Marka i model:', bg=my_config.BACKGROUND)
        marka_label.grid(row=3, column=0, sticky=tk.E)
        rocznik_label = tk.Label(self.entry_frame, text='Data zakupu:', bg=my_config.BACKGROUND)
        rocznik_label.grid(row=4, column=0, sticky=tk.E)
        wolny_label = tk.Label(self.entry_frame, text='Dostępność:', bg=my_config.BACKGROUND)
        wolny_label.grid(row=5, column=0, sticky=tk.E)

        
        self.id_auta_entry = tk.Entry(self.entry_frame, width=30, bg=my_config.FOREGROUND)
        self.id_auta_entry.grid(row=1, column=1)
        self.rejstracja_entry = tk.Entry(self.entry_frame, width=30, bg=my_config.FOREGROUND)
        self.rejstracja_entry.grid(row=2, column=1)
        self.marka_entry = tk.Entry(self.entry_frame, width=30, bg=my_config.FOREGROUND)
        self.marka_entry.grid(row=3, column=1)
        self.rocznik_entry = tk.Entry(self.entry_frame, width=30, bg=my_config.FOREGROUND)
        self.rocznik_entry.grid(row=4, column=1)
        self.dostepnosc_entry = tk.Entry(self.entry_frame, width=30, bg=my_config.FOREGROUND)
        self.dostepnosc_entry.grid(row=5, column=1)

        # buttons
        search_button = tk.Button(self.entry_frame, text='Szukaj', command=self.search_car,
                                  width=20, bg=my_config.FOREGROUND)
        search_button.grid(row=1, column=2, padx=20)
        update_button = tk.Button(self.entry_frame, text='Aktualizuj', command=self.update_car,
                                  width=20, bg=my_config.FOREGROUND)
        update_button.grid(row=2, column=2)
        update_button = tk.Button(self.entry_frame, text='Dodaj', command=self.update_car,
                                  width=20, bg=my_config.FOREGROUND)
        update_button.grid(row=3, column=2)
        clear_button = tk.Button(self.entry_frame, text='Wyczyść', command=self.clear_car_entries,
                                 width=20, bg=my_config.FOREGROUND)
        clear_button.grid(row=4, column=2)
        delete_button = tk.Button(self.entry_frame, text='Usuń', command=self.delete_car,
                                  width=20, bg=my_config.FOREGROUND)
        delete_button.grid(row=5, column=2)



        
        self.listbox_frame = tk.Frame(self.master, bg=my_config.BACKGROUND)
        self.listbox_frame.pack()

        # Ponowiona lista
        list_label = tk.Label(self.listbox_frame, text='Lista aut',
                              width=120, bg=my_config.BACKGROUND)
        list_label.grid(row=2, column=0)

        
        self.cars_tree = Treeview(self.listbox_frame, columns=AUTO_COLUMN_FULL,
                                       show='headings', height=10)
        self.cars_tree.grid(row=3, column=0)

        for column_name, width in zip(AUTO_COLUMN_FULL, AUTO_COLUMN_FULL_SIZE):
            self.cars_tree.column(column_name, width=width, anchor=tk.CENTER)
            self.cars_tree.heading(column_name, text=column_name)

        scrollbar = tk.Scrollbar(self.listbox_frame, orient=tk.VERTICAL)
        scrollbar.configure(command=self.cars_tree.set)
        self.cars_tree.configure(yscrollcommand=scrollbar)
        self.cars_tree.bind('<ButtonRelease-1>', self.get_selected_car)

        
        records = db.return_cars()
        for record in records:
            
            self.cars_tree.insert('', tk.END, values=record)

    def clear_car_entries(self):
        
        if self.error_label:
            self.error_label.destroy()

        self.id_auta_entry.delete(0, tk.END)
        self.rejstracja_entry.delete(0, tk.END)
        self.marka_entry.delete(0, tk.END)
        self.rocznik_entry.delete(0, tk.END)
        self.dostepnosc_entry.delete(0, tk.END)

    def search_car(self):
       
        try:
            if self.error_label:
                self.error_label.destroy()

            records = db.search_car(self.id_auta_entry.get(), self.rejstracja_entry.get(),
                                         self.marka_entry.get(), self.rocznik_entry.get(),
                                         self.dostepnosc_entry.get())

            for child in self.cars_tree.get_children():
                self.cars_tree.delete(child)
            for record in records:
                self.cars_tree.insert('', tk.END, values=record)

        except KeyError:
            pass


    def delete_car(self):
        
        if self.error_label:
            self.error_label.destroy()

        
        if not self.cars_tree.selection():
            self.error_message("Wybierz z listy")
            return

       
        selected_record = self.cars_tree.set(self.cars_tree.selection())
        record = db.return_car(selected_record[AUTO_COLUMN_FULL[0]])

        
        if record:
            car_info = "{}\n{}\n{}".format(record[0], record[1], record[2])

            
            answer = messagebox.askquestion('Autobaza', "Usuń:\n{}".format(car_info))
            if answer == 'Tak':
                db.delete_car(selected_record[AUTO_COLUMN_FULL[0]])
                
                self.initialize_menu()

        
        else:
            self.error_message("Nie istnieje w bazie")

    def update_car(self):
        
        if self.error_label:
            self.error_label.destroy()

       
        if not self.cars_tree.selection():
            self.error_message("Wybierz najpierw auto z listy")
            return

        
        if not self.rejstracja_entry.get():
            self.error_message("Nr rej nie może być pusty")
        elif not self.marka_entry.get():
            self.error_message("Marka nie może być pusta")
        elif not self.rocznik_entry.get():
            self.error_message("Rocznik nie może być pusty")
        elif self.dostepnosc_entry.get() not in ['0', '1']:
            self.error_message("Dostępność musi byc 1 lub 0")

        else:
            current_record = self.cars_tree.set(self.cars_tree.selection())
            db.update_car(current_record[AUTO_COLUMN_FULL[0]], self.rejstracja_entry.get(),
                               self.marka_entry.get(), self.rocznik_entry.get(), self.dostepnosc_entry.get())
            
            self.initialize_menu()


    def get_selected_car(self, event):
        
        self.clear_car_entries()
        if self.error_label:
            self.error_label.destroy()

        if self.cars_tree.selection():
            record = self.cars_tree.set(self.cars_tree.selection())

            self.id_auta_entry.insert(tk.END, record[AUTO_COLUMN_FULL[0]])
            self.rejstracja_entry.insert(tk.END, record[AUTO_COLUMN_FULL[1]])
            self.marka_entry.insert(tk.END, record[AUTO_COLUMN_FULL[2]])
            self.rocznik_entry.insert(tk.END, record[AUTO_COLUMN_FULL[3]])
            self.dostepnosc_entry.insert(tk.END, record[AUTO_COLUMN_FULL[4]])


    def error_message(self, name):
        
        if self.error_label:
            self.error_label.destroy()

        self.error_label = tk.Label(self.entry_frame, text=name,
                                    bg=my_config.BACKGROUND, fg=my_config.ERROR_FOREGROUND)
        self.error_label.grid(row=6, column=1)

    def go_to_order_window(self):
        
        self.frame.destroy()
        self.entry_frame.destroy()
        self.listbox_frame.destroy()
        application = OrdersMenu(self.master)
        application.initialize_menu()

    def go_to_client_window(self):
        
        self.frame.destroy()
        self.entry_frame.destroy()
        self.listbox_frame.destroy()
        application = ClientsMenu(self.master)
        application.initialize_menu()

    def exit_main_window(self):
       
        self.frame.destroy()
        self.entry_frame.destroy()
        self.listbox_frame.destroy()
        application = login.LoginWindow(self.master)
        application.initialize_login_window()


class ClientsMenu:
    

    def __init__(self, master):
        
        self.master = master
        self.master.geometry(MAIN_WINDOW_SIZE)
        self.master.configure(bg=my_config.BACKGROUND)
        self.master.title(my_config.APP_NAME)

        
        self.frame = tk.Frame(self.master, bg=my_config.BACKGROUND)
        self.frame.pack()
        
        self.entry_frame = tk.Frame(self.master, bg=my_config.BACKGROUND)
        self.entry_frame.pack()
        
        self.listbox_frame = tk.Frame(self.master, bg=my_config.BACKGROUND)
        self.listbox_frame.pack()

        
        self.error_label = tk.Label()

        self.product_tree = None
        self.description_entry = None
        self.in_stock_entry = None
        self.product_name_entry = None
        self.product_price_entry = None

        self.client_tree = None

        self.client_id_entry = None
        self.client_name_entry = None
        self.NIP_entry = None
        self.client_tel_entry = None
        self.email_entry = None

        self.street_entry = None
        self.street_num_entry = None
        self.apt_num_entry = None
        self.city_code_entry = None
        self.city_entry = None



    def initialize_menu(self):
        
        self.frame.destroy()
        self.frame = tk.Frame(self.master, bg=my_config.BACKGROUND)
        self.frame.pack()

        self.entry_frame.destroy()
        self.entry_frame = tk.Frame(self.master, bg=my_config.BACKGROUND)
        self.entry_frame.pack()

        self.listbox_frame.destroy()
        self.listbox_frame = tk.Frame(self.master, bg=my_config.BACKGROUND)
        self.listbox_frame.pack()

        if self.error_label:
            self.error_label.destroy()

        
        auto_button = tk.Button(self.frame, text='Auta', command=self.go_to_car_window,
                                    width=30, bg=my_config.FOREGROUND)
        auto_button.grid(row=0, column=0, pady=10)
        order_button = tk.Button(self.frame, text='Rezerwacja', command=self.go_to_order_window,
                                 width=30, bg=my_config.FOREGROUND)
        order_button.grid(row=0, column=1, )
        product_button = tk.Button(self.frame, text='Klienci', command=self.initialize_menu,
                                   width=30, bg=my_config.FOREGROUND)
        product_button.grid(row=0, column=2)
        exit_button = tk.Button(self.frame, text='Wyloguj', command=self.exit_main_window,
                                width=30, bg=my_config.FOREGROUND)
        exit_button.grid(row=0, column=3)
        
                
        client_id_label = tk.Label(self.entry_frame, text='ID klienta:', bg=my_config.BACKGROUND)
        client_id_label.grid(row=0, column=0, sticky=tk.E)
        client_name_label = tk.Label(self.entry_frame, text='Nazwa:', bg=my_config.BACKGROUND)
        client_name_label.grid(row=1, column=0, sticky=tk.E)
        NIP_label = tk.Label(self.entry_frame, text='NIP:', bg=my_config.BACKGROUND)
        NIP_label.grid(row=2, column=0, sticky=tk.E)
        client_tel_label = tk.Label(self.entry_frame, text='Telefon:', bg=my_config.BACKGROUND)
        client_tel_label.grid(row=3, column=0, sticky=tk.E)
        client_email_label = tk.Label(self.entry_frame, text='Email:', bg=my_config.BACKGROUND)
        client_email_label.grid(row=4, column=0, sticky=tk.E)

        street_label = tk.Label(self.entry_frame, text='Ulica:', bg=my_config.BACKGROUND)
        street_label.grid(row=0, column=2, sticky=tk.E)
        street_num_label = tk.Label(self.entry_frame, text='Nr domu:', bg=my_config.BACKGROUND)
        street_num_label.grid(row=1, column=2, sticky=tk.E)
        apt_num_label = tk.Label(self.entry_frame, text='Nt lokalu:', bg=my_config.BACKGROUND)
        apt_num_label.grid(row=2, column=2, sticky=tk.E)
        city_code_label = tk.Label(self.entry_frame, text='Kod:', bg=my_config.BACKGROUND)
        city_code_label.grid(row=3, column=2, sticky=tk.E)
        city_label = tk.Label(self.entry_frame, text='Miasto:', bg=my_config.BACKGROUND)
        city_label.grid(row=4, column=2, sticky=tk.E)


        self.client_id_entry = tk.Entry(self.entry_frame, width=30, bg=my_config.FOREGROUND)
        self.client_id_entry.grid(row=0, column=1)
        self.client_name_entry = tk.Entry(self.entry_frame, width=30, bg=my_config.FOREGROUND)
        self.client_name_entry.grid(row=1, column=1)
        self.NIP_entry = tk.Entry(self.entry_frame, width=30, bg=my_config.FOREGROUND)
        self.NIP_entry.grid(row=2, column=1)
        self.client_tel_entry = tk.Entry(self.entry_frame, width=30, bg=my_config.FOREGROUND)
        self.client_tel_entry.grid(row=3, column=1)
        self.email_entry = tk.Entry(self.entry_frame, width=30, bg=my_config.FOREGROUND)
        self.email_entry.grid(row=4, column=1)

        self.street_entry = tk.Entry(self.entry_frame, width=30, bg=my_config.FOREGROUND)
        self.street_entry.grid(row=0, column=3)
        self.street_num_entry = tk.Entry(self.entry_frame, width=30, bg=my_config.FOREGROUND)
        self.street_num_entry.grid(row=1, column=3)
        self.apt_num_entry = tk.Entry(self.entry_frame, width=30, bg=my_config.FOREGROUND)
        self.apt_num_entry.grid(row=2, column=3)
        self.city_code_entry = tk.Entry(self.entry_frame, width=30, bg=my_config.FOREGROUND)
        self.city_code_entry.grid(row=3, column=3)
        self.city_entry = tk.Entry(self.entry_frame, width=30, bg=my_config.FOREGROUND)
        self.city_entry.grid(row=4, column=3)


        # przyciski
        add_button = tk.Button(self.entry_frame, text='Dodaj', command=self.add_client,
                               width=20, bg=my_config.FOREGROUND)
        add_button.grid(row=0, column=4, padx=20)
        search_button = tk.Button(self.entry_frame, text='Szukaj', command=self.search_product,
                                  width=20, bg=my_config.FOREGROUND)
        search_button.grid(row=1, column=4)
        update_button = tk.Button(self.entry_frame, text='Aktualizuj', command=self.update_product,
                                  width=20, bg=my_config.FOREGROUND)
        update_button.grid(row=2, column=4)
        clear_button = tk.Button(self.entry_frame, text='Wyczyść', command=self.clear_clients_entries,
                                 width=20, bg=my_config.FOREGROUND)
        clear_button.grid(row=3, column=4)
        delete_button = tk.Button(self.entry_frame, text='Usuń', command=self.delete_product,
                                  width=20, bg=my_config.FOREGROUND)
        delete_button.grid(row=4, column=4)

        list_label = tk.Label(self.listbox_frame, text='Lista klientów',
                              width=100, bg=my_config.BACKGROUND)
        list_label.grid(row=0, column=0, pady=(10,10))

        
        self.client_tree = Treeview(self.listbox_frame, columns=CLIENT_COLUMNS_FULL,
                                     show='headings', height=10)
        self.client_tree.grid(row=1, column=0)

        for column_name, width in zip(CLIENT_COLUMNS_FULL, CLIENT_COLUMNS_FULL_SIZE):
            self.client_tree.column(column_name, width=width, anchor=tk.CENTER)
            self.client_tree.heading(column_name, text=column_name)

        scrollbar = tk.Scrollbar(self.listbox_frame, orient=tk.VERTICAL)
        scrollbar.configure(command=self.client_tree.set)
        self.client_tree.configure(yscrollcommand=scrollbar)
        self.client_tree.bind('<ButtonRelease-1>', self.get_selected_clients)

        
        records = db.return_clients()
        for record in records:
            
            self.client_tree.insert('', tk.END, values=record)                    
            #self.client_tree.insert('', tk.END, values=[record[0], record[1], record[2], record[3], record[4], record[5]])
        
    def clear_product_entries(self):
        
        if self.error_label:
            self.error_label.destroy()

        self.product_name_entry.delete(0, tk.END)
        self.product_price_entry.delete(0, tk.END)
        self.in_stock_entry.delete(0, tk.END)
        self.description_entry.delete(0, tk.END)

    def clear_clients_entries(self):
        
        if self.error_label:
            self.error_label.destroy()

        self.client_id_entry.delete(0, tk.END)
        self.client_name_entry.delete(0, tk.END)
        self.NIP_entry.delete(0, tk.END)
        self.client_tel_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)

        self.street_entry.delete(0, tk.END)
        self.street_num_entry.delete(0, tk.END)
        self.apt_num_entry.delete(0, tk.END)
        self.city_code_entry.delete(0, tk.END)
        self.city_entry.delete(0, tk.END)

    def add_product(self):
        #nowy 
        if self.error_label:
            self.error_label.destroy()

        if not self.product_name_entry.get():
            self.error_message("Błąd nazwy")
        elif not my_config.is_float(self.product_price_entry.get()) or float(
                self.product_price_entry.get()) < 1.0:
            self.error_message("Dodaj cenę")
        elif not my_config.is_integer(self.in_stock_entry.get()) or int(
                self.in_stock_entry.get()) < 0:
            self.error_message("Dodaj ilość")

        
        else:
           
            if db.is_product_exists(self.product_name_entry.get()):
                self.error_message("'{}' Istnieje".format(self.product_name_entry.get()))

            else:
                db.add_product(self.product_name_entry.get(), self.product_price_entry.get(),
                               self.in_stock_entry.get(), self.description_entry.get())                
                self.initialize_menu()

    def add_client(self):
        #nowy klient
        if self.error_label:
            self.error_label.destroy()

        if not self.client_name_entry.get():
            self.error_message("Błąd nazwy")
        else:           
            if db.is_client_exists(self.client_name_entry.get()):
                self.error_message("'{}' Istnieje".format(self.client_name_entry.get()))

            else:
                db.add_client(self.client_name_entry.get(),
                               self.NIP_entry.get(),
                               self.client_tel_entry.get(),
                               self.email_entry.get(),
                               self.street_entry.get(),
                               self.street_num_entry.get(),
                               self.apt_num_entry.get(),
                               self.city_code_entry.get(),
                               self.city_entry.get())                
                self.initialize_menu()

    def search_product(self):
        
        if self.error_label:
            self.error_label.destroy()

        try:
            for child in self.product_tree.get_children():
                self.product_tree.delete(child)

            records = db.search_products(self.product_name_entry.get(), self.product_price_entry.get(),
                                         self.in_stock_entry.get(), self.description_entry.get())
            for record in records:
                
                self.product_tree.insert('', tk.END, values=record)

        except KeyError:
            pass

    def delete_product(self):
       #usun 
        if self.error_label:
            self.error_label.destroy()

       
        if not self.product_tree.selection():
            self.error_message("Wybierz z listy")
            return

        selected_record = self.product_tree.set(self.product_tree.selection())
        record = db.return_product(selected_record[PRODUCT_COLUMNS[0]])

        if record:
            product_info = "{}\n{}\n{}".format(record[1], record[2], record[3])

            
            answer = messagebox.askquestion('Autorent', "Usuń:\n{}".format(product_info))
            if answer == 'tak':
                db.delete_product(selected_record[PRODUCT_COLUMNS[0]])
                
                self.initialize_menu()

        
        else:
            self.error_message("Nie istnieje")

    def update_product(self):
        
        try:
            if self.error_label:
                self.error_label.destroy()

            
            if not self.product_tree.selection():
                self.error_message("Wybierz z listy")
                return

            
            if not self.product_name_entry.get():
                self.error_message("Dodaj nazwę")
            elif not my_config.is_float(self.product_price_entry.get()) or float(
                    self.product_price_entry.get()) < 1.0:
                self.error_message("Dodaj cenę")
            elif not my_config.is_integer(self.in_stock_entry.get()) or int(
                    self.in_stock_entry.get()) < 0:
                self.error_message("Dodaj ilość")

            else:
                
                record = self.product_tree.set(self.product_tree.selection())
                db.update_product(record[PRODUCT_COLUMNS[0]], self.product_name_entry.get(),
                                  self.product_price_entry.get(),
                                  self.in_stock_entry.get(), self.description_entry.get())

               
                self.initialize_menu()
        except KeyError:
            pass

    def get_selected_product(self, event):
        
        self.clear_product_entries()
        if self.error_label:
            self.error_label.destroy()
        try:
            if self.product_tree.selection():
                record = self.product_tree.set(self.product_tree.selection())
                self.product_name_entry.insert(tk.END, record[PRODUCT_COLUMNS[1]])
                self.product_price_entry.insert(tk.END, record[PRODUCT_COLUMNS[2]])
                self.in_stock_entry.insert(tk.END, record[PRODUCT_COLUMNS[3]])
                self.description_entry.insert(tk.END, record[PRODUCT_COLUMNS[4]])

        except KeyError:
            pass

    def get_selected_clients(self, event):
        
        self.clear_clients_entries()
        if self.error_label:
            self.error_label.destroy()
        try:
            if self.client_tree.selection():
                record = self.client_tree.set(self.client_tree.selection())
                
                self.client_id_entry.insert(tk.END, record[CLIENT_COLUMNS_FULL[0]])
                self.client_name_entry.insert(tk.END, record[CLIENT_COLUMNS_FULL[1]])
                self.NIP_entry.insert(tk.END, record[CLIENT_COLUMNS_FULL[2]])
                self.client_tel_entry.insert(tk.END, record[CLIENT_COLUMNS_FULL[3]])
                self.email_entry.insert(tk.END, record[CLIENT_COLUMNS_FULL[4]])

                self.street_entry.insert(tk.END, record[CLIENT_COLUMNS_FULL[5]])
                self.street_num_entry.insert(tk.END, record[CLIENT_COLUMNS_FULL[6]])
                self.apt_num_entry.insert(tk.END, record[CLIENT_COLUMNS_FULL[7]])
                self.city_code_entry.insert(tk.END, record[CLIENT_COLUMNS_FULL[8]])
                self.city_entry.insert(tk.END, record[CLIENT_COLUMNS_FULL[9]])

        except KeyError:
            pass


    def error_message(self, name):
       
        if self.error_label:
            self.error_label.destroy()

        self.error_label = tk.Label(self.entry_frame, text=name,
                                    bg=my_config.BACKGROUND, fg=my_config.ERROR_FOREGROUND)
        self.error_label.grid(row=4, column=1)

    def go_to_order_window(self):
       
        self.frame.destroy()
        self.entry_frame.destroy()
        self.listbox_frame.destroy()
        application = OrdersMenu(self.master)
        application.initialize_menu()

    def go_to_car_window(self):
        
        self.frame.destroy()
        self.entry_frame.destroy()
        self.listbox_frame.destroy()
        application = CarsMenu(self.master)
        application.initialize_menu()

    def exit_main_window(self):
        
        self.frame.destroy()
        self.entry_frame.destroy()
        self.listbox_frame.destroy()
        application = login.LoginWindow(self.master)
        application.initialize_login_window()


class OrdersMenu:
    
    def __init__(self, master):
       
        self.master = master
        self.master.geometry(MAIN_WINDOW_SIZE)
        self.master.configure(bg=my_config.BACKGROUND)
        self.master.title(my_config.APP_NAME)

        self.frame = tk.Frame(self.master, bg=my_config.BACKGROUND)
        self.frame.pack()
        
        self.entry_frame = tk.Frame(self.master, bg=my_config.BACKGROUND)
        self.entry_frame.pack()
        
        self.orders_frame = tk.Frame(self.master, bg=my_config.BACKGROUND)
        self.orders_frame.pack()
        self.products_customers_frame = tk.Frame(self.master, bg=my_config.BACKGROUND)
        self.products_customers_frame.pack()

        
        self.error_label = tk.Label()

        self.order_tree = None
        self.product_tree = None
        self.customers_tree = None
        self.id_client_entry = None
        self.id_auto_entry = None
        self.price_entry = None
        self.order_date_entry = None
        self.rent_date_entry = None
        self.comment_entry = None

    def initialize_menu(self):
        
        self.frame.destroy()
        self.frame = tk.Frame(self.master, bg=my_config.BACKGROUND)
        self.frame.pack()

        self.entry_frame.destroy()
        self.entry_frame = tk.Frame(self.master, bg=my_config.BACKGROUND)
        self.entry_frame.pack()

        self.orders_frame.destroy()
        self.orders_frame = tk.Frame(self.master, bg=my_config.BACKGROUND)
        self.orders_frame.pack()

        self.products_customers_frame.destroy()
        self.products_customers_frame = tk.Frame(self.master, bg=my_config.BACKGROUND)
        self.products_customers_frame.pack()

        if self.error_label:
            self.error_label.destroy()

        
        auto_button = tk.Button(self.frame, text='Auta', command=self.go_to_car_window,
                                    width=30, bg=my_config.FOREGROUND)
        auto_button.grid(row=0, column=0, pady=10)
        order_button = tk.Button(self.frame, text='Rezerwacja', command=self.initialize_menu,
                                 width=30, bg=my_config.FOREGROUND)
        order_button.grid(row=0, column=1, )
        product_button = tk.Button(self.frame, text='Klienci', command=self.go_to_client_window,
                                   width=30, bg=my_config.FOREGROUND)
        product_button.grid(row=0, column=2)
        exit_button = tk.Button(self.frame, text='Wyloguj', command=self.exit_main_window,
                                width=30, bg=my_config.FOREGROUND)
        exit_button.grid(row=0, column=3)

       #label
        id_clients_label = tk.Label(self.entry_frame, text='ID Klienta:', bg=my_config.BACKGROUND)
        id_clients_label.grid(row=0, column=0, sticky=tk.E)
        id_ID_auta_label = tk.Label(self.entry_frame, text='ID Auta:', bg=my_config.BACKGROUND)
        id_ID_auta_label.grid(row=1, column=0, sticky=tk.E)
        price_label = tk.Label(self.entry_frame, text='Rabat', bg=my_config.BACKGROUND)
        price_label.grid(row=2, column=0, sticky=tk.E)
        order_date_label = tk.Label(self.entry_frame, text='Data zamówienia:', bg=my_config.BACKGROUND)
        order_date_label.grid(row=3, column=0, sticky=tk.E)
        rent_date_label = tk.Label(self.entry_frame, text='Data wypożyczenia:', bg=my_config.BACKGROUND)
        rent_date_label.grid(row=4, column=0, sticky=tk.E)
        comment_label = tk.Label(self.entry_frame, text='Uwagi:', bg=my_config.BACKGROUND)
        comment_label.grid(row=5, column=0, sticky=tk.E)

        
        self.id_client_entry = tk.Entry(self.entry_frame, width=30, bg=my_config.FOREGROUND)
        self.id_client_entry.grid(row=0, column=1)
        self.id_auto_entry = tk.Entry(self.entry_frame, width=30, bg=my_config.FOREGROUND)
        self.id_auto_entry.grid(row=1, column=1)
        self.price_entry = tk.Entry(self.entry_frame, width=30, bg=my_config.FOREGROUND)
        self.price_entry.grid(row=2, column=1)
        self.order_date_entry = tk.Entry(self.entry_frame, width=30, bg=my_config.FOREGROUND)
        self.order_date_entry.grid(row=3, column=1)
        self.rent_date_entry = tk.Entry(self.entry_frame, width=30, bg=my_config.FOREGROUND)
        self.rent_date_entry.grid(row=4, column=1)
        self.comment_entry = tk.Entry(self.entry_frame, width=30, bg=my_config.FOREGROUND)
        self.comment_entry.grid(row=5, column=1)

        # przyciski
        search_button = tk.Button(self.entry_frame, text='Szukaj', command=self.search_order, width=20,
                                  bg=my_config.FOREGROUND)
        search_button.grid(row=0, column=2, padx=20)
        add_button = tk.Button(self.entry_frame, text='Dodaj', command=self.add_order,
                               width=20, bg=my_config.FOREGROUND)
        add_button.grid(row=1, column=2, padx=20)
        add_button = tk.Button(self.entry_frame, text='Aktualizuj', command=self.add_order,
                               width=20, bg=my_config.FOREGROUND)
        add_button.grid(row=2, column=2, padx=20)
        clear_button = tk.Button(self.entry_frame, text='Wyczyść', command=self.initialize_menu,
                                 width=20, bg=my_config.FOREGROUND)
        clear_button.grid(row=3, column=2)
        delete_button = tk.Button(self.entry_frame, text='Usuń', command=self.delete_order,
                                  width=20, bg=my_config.FOREGROUND)
        delete_button.grid(row=4, column=2)
        
        list_label = tk.Label(self.orders_frame, text='Rezerwacje', bg=my_config.BACKGROUND)
        list_label.grid(row=0, column=0, pady=(10, 10))

        self.order_tree = Treeview(self.orders_frame, columns=ORDER_COLUMNS, show='headings', height=8)
        self.order_tree.grid(row=1, column=0, padx=100)

        scrollbar_y = tk.Scrollbar(self.orders_frame, orient=tk.VERTICAL)
        scrollbar_y.configure(command=self.order_tree.set)
        scrollbar_x = tk.Scrollbar(self.orders_frame, orient=tk.HORIZONTAL)
        scrollbar_x.configure(command=self.order_tree.xview())
        self.order_tree.configure(yscrollcommand=scrollbar_y)
        self.order_tree.configure(xscrollcommand=scrollbar_x)
        self.order_tree.bind('<ButtonRelease-1>', self.order_list_manager)

        for column_name, width in zip(ORDER_COLUMNS, ORDER_COLUMNS_SIZE):
            self.order_tree.column(column_name, width=width, anchor=tk.CENTER)
            self.order_tree.heading(column_name, text=column_name)

       
        list_label1 = tk.Label(self.products_customers_frame, text='Zamówione auta',
                               width=25, bg=my_config.BACKGROUND)
        list_label1.grid(row=0, column=0)

        self.product_tree = Treeview(self.products_customers_frame,
                                     columns=CAR_COLUMNS, show='headings', height=8)
        self.product_tree.grid(row=1, column=0, padx=10)
        scrollbar_y = tk.Scrollbar(self.products_customers_frame, orient=tk.VERTICAL)
        scrollbar_y.configure(command=self.product_tree.set)
        scrollbar_x = tk.Scrollbar(self.products_customers_frame, orient=tk.HORIZONTAL)
        scrollbar_x.configure(command=self.order_tree.xview())
        self.product_tree.configure(yscrollcommand=scrollbar_y)
        self.product_tree.configure(xscrollcommand=scrollbar_x)
        self.product_tree.bind('<ButtonRelease-1>', self.product_list_manager)

        for column_name, width in zip(CAR_COLUMNS, CAR_COLUMNS_SIZE):
            self.product_tree.column(column_name, width=width, anchor=tk.CENTER)
            self.product_tree.heading(column_name, text=column_name)

       
        list_label2 = tk.Label(self.products_customers_frame, text='Klienci',
                               width=25, bg=my_config.BACKGROUND)
        list_label2.grid(row=0, column=1)
        self.customers_tree = Treeview(self.products_customers_frame,
                                       columns=CLIENT_COLUMNS, show='headings', height=8)
        self.customers_tree.grid(row=1, column=1)

        scrollbar_y = tk.Scrollbar(self.products_customers_frame, orient=tk.VERTICAL)
        scrollbar_y.configure(command=self.customers_tree.set)
        scrollbar_x = tk.Scrollbar(self.products_customers_frame, orient=tk.HORIZONTAL)
        scrollbar_x.configure(command=self.order_tree.xview())
        self.customers_tree.configure(yscrollcommand=scrollbar_y)
        self.customers_tree.configure(xscrollcommand=scrollbar_x)
        self.customers_tree.bind('<ButtonRelease-1>', self.customer_list_manager)

        for column_name, width in zip(CLIENT_COLUMNS, CLIENT_COLUMNS_SIZE):
            self.customers_tree.column(column_name, width=width, anchor=tk.CENTER)
            self.customers_tree.heading(column_name, text=column_name)

        
        records = db.return_orders()
        for record in records:
            self.order_tree.insert('', tk.END, values=[
                record[0], record[4], record[5], record[6], record[7], record[8]])

        
        records = db.return_all_cars()
        for record in records:
            self.product_tree.insert('', tk.END, values=[record[0], record[1], record[2], record[10]])

        
        records = db.return_clients()
        for record in records:
            self.customers_tree.insert('', tk.END, values=[record[0], record[1], record[2], record[5], record[8], record[9]])

    def add_order(self):
      
        if self.error_label:
            self.error_label.destroy()

       
        if not self.id_client_entry.get():
            self.error_message("Brak ID gościa")
        elif not self.id_auto_entry.get():
            self.error_message("Brak ID produktu")
        elif not my_config.is_integer(self.price_entry.get()) or int(self.price_entry.get()) < 1:
            self.error_message("Dodaj ilość")

        elif self.order_date_entry.get() not in ['0', '1']:
            self.error_message("Status musi wynosić 0 lub 1")
        elif self.rent_date_entry.get() not in ['0', '1']:
            self.error_message("Status musi wynosić 0 lub 1")
        elif not self.comment_entry.get():
            self.error_message("Brak lokalizacji")

        
        elif not db.is_client_id_exist(self.id_client_entry.get()) or not db.is_auto_id_exists(
                self.id_auto_entry.get()):
            self.error_message("ID nie istnieje")

       
        elif db.add_order(self.id_client_entry.get(), self.id_auto_entry.get(),
                          self.price_entry.get(), self.comment_entry.get(),
                          self.order_date_entry.get(), self.rent_date_entry.get()):

            self.initialize_menu()
        else:
            self.error_message("Brak wystarczającej ilości")

    def delete_order(self):
        #usun 
        if self.error_label:
            self.error_label.destroy()

       
        if not self.order_tree.selection():
            self.error_message("Wybierz z listy")
            return

       
        answer = messagebox.askquestion('Autorent', 'Usuń:\n')
        if answer == 'tak':
            selected_record = self.order_tree.set(self.order_tree.selection())
            db.delete_order(selected_record[ORDER_COLUMNS[0]])

            self.initialize_menu()

    def search_order(self):
        
        if self.error_label:
            self.error_label.destroy()

        records = db.search_orders(self.id_auto_entry.get(), self.id_client_entry.get(),
                                   self.price_entry.get(), self.order_date_entry.get(),
                                   self.rent_date_entry.get(), self.comment_entry.get())

        for child in self.order_tree.get_children():
            self.order_tree.delete(child)
        for record in records:
            self.order_tree.insert('', tk.END, values=[
                record[0], record[3], record[4], record[5], record[6], record[7]])

    def order_list_manager(self, event):
        
        if self.error_label:
            self.error_label.destroy()

        
        if self.order_tree.selection():
            current_record = self.order_tree.set(self.order_tree.selection())

            self.id_client_entry.delete(0, tk.END)
            self.id_auto_entry.delete(0, tk.END)
            self.price_entry.delete(0, tk.END)
            self.order_date_entry.delete(0, tk.END)
            self.rent_date_entry.delete(0, tk.END)
            self.comment_entry.delete(0, tk.END)

            order_data = db.return_order(current_record[ORDER_COLUMNS[0]])
            self.id_client_entry.insert(tk.END, order_data[1])
            self.id_auto_entry.insert(tk.END, order_data[2])

            self.price_entry.insert(tk.END, current_record[ORDER_COLUMNS[4]])
            self.order_date_entry.insert(tk.END, current_record[ORDER_COLUMNS[2]])
            self.rent_date_entry.insert(tk.END, current_record[ORDER_COLUMNS[3]])
            self.comment_entry.insert(tk.END, current_record[ORDER_COLUMNS[5]])

           
            record = db.return_client(order_data[1])
            for child in self.customers_tree.get_children():
                self.customers_tree.delete(child)            
            self.customers_tree.insert('', tk.END, values=[record[0], record[1], record[2], record[5], record[8], record[9]])
           
            record = db.return_auto(order_data[3])
            for child in self.product_tree.get_children():
                self.product_tree.delete(child)
            self.product_tree.insert('', tk.END, values=record)

    def product_list_manager(self, event):
        
        if self.error_label:
            self.error_label.destroy()

        
        if self.product_tree.selection():
            current_record = self.product_tree.set(self.product_tree.selection())

            self.id_auto_entry.delete(0, tk.END)
            self.id_auto_entry.insert(tk.END, current_record[CAR_COLUMNS[0]])

            
            records = db.return_auto_orders(current_record[CAR_COLUMNS[0]])
            for child in self.order_tree.get_children():
                self.order_tree.delete(child)

            for record in records:
                self.order_tree.insert('', tk.END, values=[
                    record[0], record[1], record[2], record[3], record[4], record[5]])

    def customer_list_manager(self, event):
        
        if self.error_label:
            self.error_label.destroy()

        
        if self.customers_tree.selection():
            current_record = self.customers_tree.set(self.customers_tree.selection())

            self.id_client_entry.delete(0, tk.END)
            self.id_client_entry.insert(tk.END, current_record[CLIENT_COLUMNS[0]])

            
            records = db.return_client_orders(current_record[CLIENT_COLUMNS[0]])
            for child in self.order_tree.get_children():
                self.order_tree.delete(child)

            for record in records:
                self.order_tree.insert('', tk.END, values=[
                    record[0], record[4], record[5], record[6], record[7], record[8]])

    def error_message(self, name):
        
        if self.error_label:
            self.error_label.destroy()

        self.error_label = tk.Label(self.frame, text=name, bg=my_config.BACKGROUND,
                                    fg=my_config.ERROR_FOREGROUND)
        self.error_label.grid(row=11, column=1)

    def go_to_car_window(self):
        
        self.frame.destroy()
        self.entry_frame.destroy()
        self.orders_frame.destroy()
        self.products_customers_frame.destroy()
        application = CarsMenu(self.master)
        application.initialize_menu()

    def go_to_client_window(self):
       
        self.frame.destroy()
        self.entry_frame.destroy()
        self.orders_frame.destroy()
        self.products_customers_frame.destroy()
        application = ClientsMenu(self.master)
        application.initialize_menu()

    def exit_main_window(self):
        
        self.frame.destroy()
        self.entry_frame.destroy()
        self.orders_frame.destroy()
        self.products_customers_frame.destroy()
        application = login.LoginWindow(self.master)
        application.initialize_login_window()
