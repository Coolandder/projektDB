import sqlite3

import my_config

MY_CONNECTION = sqlite3.connect('autorent.db')


def is_user_exists(login, email):
    
    with MY_CONNECTION as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT exists(SELECT 1 FROM pracownik WHERE login=?)", (login,))
        if cursor.fetchone()[0] == 1:
            return my_config.CUSTOMER_LOGIN

        cursor.execute("SELECT exists(SELECT 1 FROM pracownik WHERE email=?)", (email,))
        if cursor.fetchone()[0] == 1:
            return my_config.CUSTOMER_EMAIL
        return my_config.CUSTOMER_ABSENT


def is_client_id_exist(client_id) -> bool:
    
    with MY_CONNECTION as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT exists(SELECT 1 FROM klienci WHERE id_klienta=?)", (client_id,))
        return cursor.fetchone()[0] == 1


def add_user(login, password, first_name, second_name, position, email):
    #nowy user
    with MY_CONNECTION as connection:
        connection.execute(
            """
            INSERT INTO pracownik            
            (login,passwd,imie,nazwisko,stanowisko,email)
            VALUES(?,?,?,?,?,?)
            """,
            (login, password, first_name, second_name, position, email))

def return_clients():
   #klienci
    with MY_CONNECTION as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM klienci")
        return cursor.fetchall()

def return_cars():
   #auta
    with MY_CONNECTION as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT id_auta, nr_rejestracyjny, marka_model, rocznik, dostepne FROM auta")
        return cursor.fetchall()

def return_all_cars():
   #auta
    with MY_CONNECTION as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM auta")
        return cursor.fetchall()

def return_client(client_id):
    
    with MY_CONNECTION as connection:
        cursor = connection.cursor()
        cursor.execute(
            """
            SELECT * FROM klienci
            WHERE id_klienta=?
            """,
            (client_id,))
        return cursor.fetchone()

def return_car(car_id):
    
    with MY_CONNECTION as connection:
        cursor = connection.cursor()
        cursor.execute(            
            """
            SELECT id_auta, nr_rejestracyjny, marka_model, rocznik, dostepne
            FROM auta
            WHERE id_auta=?
            """,            
            (car_id,))
        return cursor.fetchone()


def search_car(id_auta="", nr_rejestracyjny="", marka_model="", rocznik="", dostepne=""):
    with MY_CONNECTION as connection:
        cursor = connection.cursor()
        cursor.execute(
            """
            SELECT id_auta, nr_rejestracyjny, marka_model, rocznik, dostepne
            FROM auta
            WHERE id_auta=? OR nr_rejestracyjny=? OR marka_model=? OR rocznik=? OR dostepne=?
            """,
            (id_auta, nr_rejestracyjny, marka_model, rocznik, dostepne))
        return cursor.fetchall()

def delete_car(car_id):
    #usun auto
    with MY_CONNECTION as connection:
        connection.execute("DELETE FROM auta WHERE id_auta=?", (car_id,))


def update_car(id_auta, nr_rejestracyjny, marka_model, rocznik, dostepne):
    #update
    with MY_CONNECTION as connection:
        connection.execute(
            """            
            UPDATE auta
            SET nr_rejestracyjny=?, marka_model=?, rocznik=?, dostepne=?
            WHERE id_auta=?
            """,            
            (nr_rejestracyjny, marka_model, rocznik, dostepne, id_auta))


def user_perm(login, password):
    
    with MY_CONNECTION as connection:
        cursor = connection.cursor()
        cursor.execute(
            """
            SELECT id_pracownik, perm
            FROM pracownik
            WHERE login=? and passwd=?
            """,
            (login, password))
        record = cursor.fetchone()
        if record is None:
            return False, -1
        return record[0], record[1]
    
# oferta



def is_product_exists(product_name) -> bool:
    
    with MY_CONNECTION as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT exists(SELECT 1 FROM Products WHERE product_name=?)", (product_name,))
        return cursor.fetchone()[0] == 1

def is_client_exists(client_name) -> bool:
    
    with MY_CONNECTION as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT exists(SELECT 1 FROM klienci WHERE nazwa=?)", (client_name,))
        return cursor.fetchone()[0] == 1

def is_product_id_exists(product_id) -> bool:
    
    with MY_CONNECTION as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT exists(SELECT 1 FROM Products WHERE id_product=?)", (product_id,))
        return cursor.fetchone()[0] == 1

def is_auto_id_exists(auto_id) -> bool:
    
    with MY_CONNECTION as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT exists(SELECT 1 FROM auta WHERE id_auta=?)", (auto_id,))
        return cursor.fetchone()[0] == 1


def return_product(product_id):
    
    with MY_CONNECTION as connection:
        cursor = connection.cursor()
        cursor.execute(
            """
            SELECT id_product, product_name, product_price, in_stock, description
            FROM Products
            WHERE id_product=?
            """,
            (product_id,))
        return cursor.fetchone()

def return_auto(auto_id):
    
    with MY_CONNECTION as connection:
        cursor = connection.cursor()
        cursor.execute(
            """
            SELECT id_auta, nr_rejestracyjny, marka_model, cena_wypoz_jeden_dzien
            FROM auta
            WHERE id_auta=?
            """,
            (auto_id,))
        return cursor.fetchone()


def return_products():
    
    with MY_CONNECTION as connection:
        cursor = connection.cursor()
        cursor.execute(
            """
            SELECT id_product, product_name, product_price, in_stock, description
            FROM Products
            """)
        return cursor.fetchall()


def add_product(name, price, stock, description):
    #dodaj do bazy
    with MY_CONNECTION as connection:
        connection.execute(
            """
            INSERT INTO Products
            (product_name, product_price, in_stock, description)
            VALUES (?,?,?,?)
            """,
            (name, price, stock, description,))

def add_client(name, NIP, tel, email, street, street_num, apt_num, city_code, city):
    #dodaj klienta do bazy
    with MY_CONNECTION as connection:
        connection.execute(
            """
            INSERT INTO klienci            
            (nazwa, nip, telefon, email, ulica, nr_domu, nr_lokalu, kod_pocztowy, poczta)
            VALUES (?,?,?,?,?,?,?,?,?)
            """,
            (name, NIP, tel, email, street, street_num, apt_num, city_code, city))            

def search_products(name='', price='', stock='', description=''):
   
    with MY_CONNECTION as connection:
        cursor = connection.cursor()
        if description:
            cursor.execute(
                """
                SELECT id_product, product_name, product_price, in_stock, description
                FROM Products
                WHERE product_name=? OR product_price=? OR in_stock=? OR description=?
                """,
                (name, price, stock, description,))
        else:
            cursor.execute(
                """
                SELECT id_product, product_name, product_price, in_stock, description
                FROM Products
                WHERE product_name=? OR product_price=? OR in_stock=?
                """,
                (name, price, stock,))
        return cursor.fetchall()



def delete_product(product_id):
    #usun
    with MY_CONNECTION as connection:
        connection.execute("DELETE FROM Products WHERE id_product=?", (product_id,))


def update_product(product_id, name, price, stock, description):
    
    with MY_CONNECTION as connection:
        connection.execute(
            """
            UPDATE Products
            SET product_name=?, product_price=?, in_stock=?, description=?
            WHERE id_product=?
            """,
            (name, price, stock, description, product_id,))


def return_orders():
    #R2 lista zamówień
    with MY_CONNECTION as connection:
        cursor = connection.cursor()
        cursor.execute(
            """
            SELECT id_zamowienia, id_klienta, id_pracownik, id_auta, data_zamowienia, data_wypozyczenia, data_zwrotu, rabat, uwagi            
            FROM [zamowienia] join [reprezentanci]
            ON [zamowienia].id_reprezentanta = [reprezentanci].id_reprezentanta
            """)        
        records = cursor.fetchall()
        return records


def return_auto_orders(auto_id):
   
    with MY_CONNECTION as connection:
        cursor = connection.cursor()
        cursor.execute(
            """
            SELECT id_zamowienia, data_zamowienia, data_wypozyczenia, data_zwrotu, rabat, uwagi
            FROM [zamowienia]
            Where id_auta=?
            """,
            (auto_id,))
        return cursor.fetchall()


def return_client_orders(client_id):
    
    with MY_CONNECTION as connection:
        cursor = connection.cursor()
        cursor.execute(
            """            
            SELECT id_zamowienia, id_klienta, id_pracownik, id_auta, data_zamowienia, data_wypozyczenia, data_zwrotu, rabat, uwagi            
            FROM [zamowienia] join [reprezentanci]
            ON [zamowienia].id_reprezentanta = [reprezentanci].id_reprezentanta
            WHERE id_klienta=?
            """,
            (client_id,))
        return cursor.fetchall()


def add_order(customer_id, product_id, quantity, location, payment_status=0, send_status=0):
    
    in_stock = return_product(product_id)[3]
    if in_stock - float(quantity) < 0:
        return False

    with MY_CONNECTION as connection:
        
        connection.execute("UPDATE Products SET in_stock=? WHERE id_product=?",
                           (in_stock - float(quantity), product_id))

        
        total_price = float(return_product(product_id)[2]) * float(quantity)
        connection.execute(
            """
            INSERT INTO Orders
            (id_customer, id_product, quantity, total_price, payment_status, send_status, location)
            VALUES(?,?,?,?,?,?,?)
            """,
            (customer_id, product_id, quantity, total_price, payment_status, send_status, location))
        return True


def orders_product_info(customer_id):
    
    with MY_CONNECTION as connection:
        cursor = connection.cursor()
        cursor.execute(
            """
            SELECT o.id_order,p.product_name,o.quantity,o.total_price
            FROM Orders AS o
            NATURAL JOIN Products AS p
            WHERE o.id_customer=?
            """,
            (customer_id,))
        return cursor.fetchall()


def delete_order(order_id):
  
    with MY_CONNECTION as connection:
        connection.execute("DELETE FROM Orders WHERE id_order=?", (order_id,))


def search_orders(auto_id='', client_id='', price='', order_date='', rent_date='', comment=''):
    
    with MY_CONNECTION as connection:
        cursor = connection.cursor()
        cursor.execute(
            """            
            SELECT id_zamowienia,
            id_auta,
            id_klienta,            
            data_zamowienia,
            data_wypozyczenia,
            data_zwrotu,
            rabat,
            uwagi            
            FROM [zamowienia] join [reprezentanci]
            ON [zamowienia].id_reprezentanta = [reprezentanci].id_reprezentanta
            WHERE id_auta=? OR id_klienta=? OR rabat=? OR data_zamowienia=? OR data_wypozyczenia=? OR uwagi=?            
            """,
            (auto_id, client_id, price, order_date, rent_date, comment))
        return cursor.fetchall()


def return_order(order_id):
    #R1
    with MY_CONNECTION as connection:
        cursor = connection.cursor()
        cursor.execute(
            """
            SELECT id_zamowienia, id_klienta, id_pracownik, [zamowienia].id_auta, data_zamowienia, data_wypozyczenia, data_zwrotu, rabat, uwagi, cena_wypoz_jeden_dzien
            FROM [zamowienia] join [reprezentanci]
            ON [zamowienia].id_reprezentanta = [reprezentanci].id_reprezentanta
                join [auta]
                ON [auta].id_auta = [zamowienia].id_auta
            WHERE id_zamowienia=?
            """,
            (order_id,))
        return cursor.fetchone()
