INSERT INTO [klienci] ([id_klienta], [nazwa], [nip], [telefon], [email], [ulica], [nr_domu], [nr_lokalu], [kod_pocztowy], [poczta])
VALUES (1, 'Nowa Droga Sp. z o.o.', '526-555-22-12', '17 862 66 22', 'info@nowadroga.pl', 'Nowa', '5', '1', '35-222', 'Rzeszów');

INSERT INTO [klienci] ([id_klienta], [nazwa], [nip], [telefon], [email], [ulica], [nr_domu], [nr_lokalu], [kod_pocztowy], [poczta])
VALUES (2, 'Itaka SA', '813-177-55-22', '17 863 55 45', 'info@itakasa.pl', 'Parkowa', '12', '1', '32-202', 'Rzeszów');

INSERT INTO [klienci] ([id_klienta], [nazwa], [nip], [telefon], [email], [ulica], [nr_domu], [nr_lokalu], [kod_pocztowy], [poczta])
VALUES (3, 'Tesla SA', '822-111-55-22', '17 830 22 45', 'info@tesla.pl', 'Dobra', '10', '1', '32-204', 'Rzeszów');

INSERT INTO [klienci] ([id_klienta], [nazwa], [nip], [telefon], [email], [ulica], [nr_domu], [nr_lokalu], [kod_pocztowy], [poczta])
VALUES (4, 'GMX SA', '813-144-00-22', '17 663 22 45', 'info@gmx.pl', 'Niska', '2', '1', '32-211', 'Rzeszów');

INSERT INTO [klienci] ([id_klienta], [nazwa], [nip], [telefon], [email], [ulica], [nr_domu], [nr_lokalu], [kod_pocztowy], [poczta])
VALUES (5, 'IR System SA', '820-170-55-22', '17 555 55 33', 'info@irsystem.pl', 'Wielka', '22', '1', '32-215', 'Rzeszów');

INSERT INTO [klienci] ([id_klienta], [nazwa], [nip], [telefon], [email], [ulica], [nr_domu], [nr_lokalu], [kod_pocztowy], [poczta])
VALUES (6, 'Jan Migalski', '', '17 863 55 45', '', 'Parkowa', '22', '12', '32-202', 'Rzeszów');

----

INSERT INTO [reprezentanci] ([id_reprezentanta], [id_klienta], [imie], [nazwisko], [telefon], [email])
VALUES (1, 1, 'Ja', 'Nowak', '505 123 5150', 'jnowak@nowadroga.pl');

INSERT INTO [reprezentanci] ([id_reprezentanta], [id_klienta], [imie], [nazwisko], [telefon], [email])
VALUES (2, 1, 'Lech', 'Kotek', '525 551 613', 'lkotek@nowadroga.pl');

INSERT INTO [reprezentanci] ([id_reprezentanta], [id_klienta], [imie], [nazwisko], [telefon], [email])
VALUES (3, 2, 'Micha³', 'Arda', '522 152 356', 'mardan@itakasa.pl');

INSERT INTO [reprezentanci] ([id_reprezentanta], [id_klienta], [imie], [nazwisko], [telefon], [email])
VALUES (4, 3, 'Alek', 'Newski', '502 052 546', 'anewski@tesla.pl');

INSERT INTO [reprezentanci] ([id_reprezentanta], [id_klienta], [imie], [nazwisko], [telefon], [email])
VALUES (5, 4, 'Zeno', 'Laskowik', '601 512 576', 'zlaskowik@gmx.pl');

INSERT INTO [reprezentanci] ([id_reprezentanta], [id_klienta], [imie], [nazwisko], [telefon], [email])
VALUES (6, 5, 'Leszek', 'Drewniak', '51 521 569', 'ldrewniak@irsystem.pl');

INSERT INTO [reprezentanci] ([id_reprezentanta], [id_klienta], [imie], [nazwisko], [telefon], [email])
VALUES (7, 6, 'Ja', 'Migalski', '602 222 353', 'jmigalski@gmail.com');

----

INSERT INTO [pracownik] ([id_pracownik], [imie], [nazwisko], [stanowisko]) VALUES (1, 'Micha³', 'Janisz', 'Konsultant');

INSERT INTO [pracownik] ([id_pracownik], [imie], [nazwisko], [stanowisko]) VALUES (2, 'Rafa³', 'Michta', 'Konsultant');

INSERT INTO [pracownik] ([id_pracownik], [imie], [nazwisko], [stanowisko]) VALUES (3, 'Ja', 'Leski', 'Konsultant');

INSERT INTO [pracownik] ([id_pracownik], [imie], [nazwisko], [stanowisko]) VALUES (4, 'Ewa', 'Rokking', 'Kierownik');

----

INSERT INTO [auta] ([id_auta], [nr_rejestracyjny], [marka_model], [rocznik], [liczba_osob], [przest_bagazowa], [d³ugosc], [wysokosc], [szerokosc], [ladownosc], [cena_wypoz_jeden_dzien], [dostepne])
VALUES (1, 'RZA 1234', 'Ford Focus','2014-12-11', 5,500.00,1.50,0.80,1.20,550.00,100.00, 0);

INSERT INTO [auta] ([id_auta], [nr_rejestracyjny], [marka_model], [rocznik], [liczba_osob], [przest_bagazowa], [d³ugosc], [wysokosc], [szerokosc], [ladownosc], [cena_wypoz_jeden_dzien], [dostepne])
VALUES (2, 'RZB 1212', 'Ford Focus','2015-10-10', 5,500.00,1.50,0.80,1.20,550.00,100.00, 1);

INSERT INTO [auta] ([id_auta], [nr_rejestracyjny], [marka_model], [rocznik], [liczba_osob], [przest_bagazowa], [d³ugosc], [wysokosc], [szerokosc], [ladownosc], [cena_wypoz_jeden_dzien], [dostepne])
VALUES (3, 'RZB 1245', 'Ford Focus','2015-10-15', 5,500.00,1.50,0.80,1.20,550.00,100.00, 0);

INSERT INTO [auta] ([id_auta], [nr_rejestracyjny], [marka_model], [rocznik], [liczba_osob], [przest_bagazowa], [d³ugosc], [wysokosc], [szerokosc], [ladownosc], [cena_wypoz_jeden_dzien], [dostepne])
VALUES (4, 'RZC 1145', 'Opel Astra','2016-01-15', 5,500.00,1.50,0.80,1.20,550.00,100.00, 1);

INSERT INTO [auta] ([id_auta], [nr_rejestracyjny], [marka_model], [rocznik], [liczba_osob], [przest_bagazowa], [d³ugosc], [wysokosc], [szerokosc], [ladownosc], [cena_wypoz_jeden_dzien], [dostepne])
VALUES (5, 'RZC 2565', 'Opel Astra','2016-01-15', 5,500.00,1.50,0.80,1.20,550.00,100.00, 0);

INSERT INTO [auta] ([id_auta], [nr_rejestracyjny], [marka_model], [rocznik], [liczba_osob], [przest_bagazowa], [d³ugosc], [wysokosc], [szerokosc], [ladownosc], [cena_wypoz_jeden_dzien], [dostepne])
VALUES (6, 'RZC 2645', 'Opel Astra','2016-02-15', 5,500.00,1.50,0.80,1.20,550.00,100.00, 1);

INSERT INTO [auta] ([id_auta], [nr_rejestracyjny], [marka_model], [rocznik], [liczba_osob], [przest_bagazowa], [d³ugosc], [wysokosc], [szerokosc], [ladownosc], [cena_wypoz_jeden_dzien], [dostepne])
VALUES (7, 'RZC 2945', 'Opel Astra','2016-02-15', 5,500.00,1.50,0.80,1.20,550.00,100.00, 1);

INSERT INTO [auta] ([id_auta], [nr_rejestracyjny], [marka_model], [rocznik], [liczba_osob], [przest_bagazowa], [d³ugosc], [wysokosc], [szerokosc], [ladownosc], [cena_wypoz_jeden_dzien], [dostepne])
VALUES (8, 'RZC 4245', 'Renault Master','2016-04-15', 3,6500.00,2.50,1.20,1.70,1500.00,150.00, 1);

INSERT INTO [auta] ([id_auta], [nr_rejestracyjny], [marka_model], [rocznik], [liczba_osob], [przest_bagazowa], [d³ugosc], [wysokosc], [szerokosc], [ladownosc], [cena_wypoz_jeden_dzien], [dostepne])
VALUES (9, 'RZC 5215', 'Renault Master','2016-04-15', 3,6500.00,2.50,1.20,1.70,1500.00,150.00, 1);

INSERT INTO [auta] ([id_auta], [nr_rejestracyjny], [marka_model], [rocznik], [liczba_osob], [przest_bagazowa], [d³ugosc], [wysokosc], [szerokosc], [ladownosc], [cena_wypoz_jeden_dzien], [dostepne])
VALUES (10, 'RZD 1315', 'Fiat Ducato','2016-07-15', 3,6500.00,2.50,1.20,1.70,1500.00,150.00, 1);

INSERT INTO [auta] ([id_auta], [nr_rejestracyjny], [marka_model], [rocznik], [liczba_osob], [przest_bagazowa], [d³ugosc], [wysokosc], [szerokosc], [ladownosc], [cena_wypoz_jeden_dzien], [dostepne])
VALUES (11, 'RZE 2345', 'Fiat Ducato','2016-07-15', 3,6500.00,2.50,1.20,1.70,1500.00,150.00, 1);

----

INSERT INTO [zamowienia] ([id_zamowienia], [id_reprezentanta], [id_pracownik], [id_auta], [data_zamowienia], [data_wypozyczenia], [data_zwrotu], [rabat], [uwagi])
VALUES (1, 1, 1, 1,'2022-05-12','2022-05-18','2022-05-22',0.00, 'brak');

INSERT INTO [zamowienia] ([id_zamowienia], [id_reprezentanta], [id_pracownik], [id_auta], [data_zamowienia], [data_wypozyczenia], [data_zwrotu], [rabat], [uwagi])
VALUES (2, 3, 2, 2,'2022-05-13','2022-05-16','2022-05-20',0.00, 'brak');

INSERT INTO [zamowienia] ([id_zamowienia], [id_reprezentanta], [id_pracownik], [id_auta], [data_zamowienia], [data_wypozyczenia], [data_zwrotu], [rabat], [uwagi])
VALUES (3, 4, 2, 3,'2022-05-12','2022-05-20','2022-05-28',0.00, 'brak');

INSERT INTO [zamowienia] ([id_zamowienia], [id_reprezentanta], [id_pracownik], [id_auta], [data_zamowienia], [data_wypozyczenia], [data_zwrotu], [rabat], [uwagi])
VALUES (4, 1, 3, 4,'2022-05-23','2022-05-28','2022-06-08',0.00, 'brak');

INSERT INTO [zamowienia] ([id_zamowienia], [id_reprezentanta], [id_pracownik], [id_auta], [data_zamowienia], [data_wypozyczenia], [data_zwrotu], [rabat], [uwagi])
VALUES (5, 5, 1, 5,'2022-05-28','2022-05-29','2022-06-12',0.20, 'brak');

INSERT INTO [zamowienia] ([id_zamowienia], [id_reprezentanta], [id_pracownik], [id_auta], [data_zamowienia], [data_wypozyczenia], [data_zwrotu], [rabat], [uwagi])
VALUES (6, 6, 1, 6,'2022-06-04','2022-06-08','2022-06-18',0.20, 'brak');

INSERT INTO [zamowienia] ([id_zamowienia], [id_reprezentanta], [id_pracownik], [id_auta], [data_zamowienia], [data_wypozyczenia], [data_zwrotu], [rabat], [uwagi])
VALUES (7, 3, 2, 7,'2022-06-14','2022-06-18','2022-06-25',0.10, 'brak');

INSERT INTO [zamowienia] ([id_zamowienia], [id_reprezentanta], [id_pracownik], [id_auta], [data_zamowienia], [data_wypozyczenia], [data_zwrotu], [rabat], [uwagi])
VALUES (8, 7, 1, 1,'2022-06-22','2022-06-26','2022-06-30',0.00, 'brak');

INSERT INTO [zamowienia] ([id_zamowienia], [id_reprezentanta], [id_pracownik], [id_auta], [data_zamowienia], [data_wypozyczenia], [data_zwrotu], [rabat], [uwagi])
VALUES (9, 5, 1, 2,'2022-06-27','2022-06-29','2022-07-02',0.00, 'brak');

INSERT INTO [zamowienia] ([id_zamowienia], [id_reprezentanta], [id_pracownik], [id_auta], [data_zamowienia], [data_wypozyczenia], [data_zwrotu], [rabat], [uwagi])
VALUES (10, 1, 2, 4,'2022-07-02','2022-07-05','2022-07-15',0.20, 'brak');

INSERT INTO [zamowienia] ([id_zamowienia], [id_reprezentanta], [id_pracownik], [id_auta], [data_zamowienia], [data_wypozyczenia], [data_zwrotu], [rabat], [uwagi])
VALUES (11, 6, 2, 3,'2022-07-11','2022-07-15','2022-07-19',0.00, 'brak');

INSERT INTO [zamowienia] ([id_zamowienia], [id_reprezentanta], [id_pracownik], [id_auta], [data_zamowienia], [data_wypozyczenia], [data_zwrotu], [rabat], [uwagi])
VALUES (12, 7, 1, 5,'2022-07-16','2022-07-17','2022-07-22',0.00, 'brak');

INSERT INTO [zamowienia] ([id_zamowienia], [id_reprezentanta], [id_pracownik], [id_auta], [data_zamowienia], [data_wypozyczenia], [data_zwrotu], [rabat], [uwagi])
VALUES (13, 4, 3, 6,'2022-07-22','2022-07-26','2022-07-29',0.00, 'brak');

INSERT INTO [zamowienia] ([id_zamowienia], [id_reprezentanta], [id_pracownik], [id_auta], [data_zamowienia], [data_wypozyczenia], [data_zwrotu], [rabat], [uwagi])
VALUES (14, 5, 3, 2,'2022-07-29','2022-07-30','2022-08-22',0.30, 'brak');

INSERT INTO [zamowienia] ([id_zamowienia], [id_reprezentanta], [id_pracownik], [id_auta], [data_zamowienia], [data_wypozyczenia], [data_zwrotu], [rabat], [uwagi])
VALUES (15, 6, 4, 1,'2022-08-09','2022-08-14','2022-08-24',0.20, 'brak');

INSERT INTO [zamowienia] ([id_zamowienia], [id_reprezentanta], [id_pracownik], [id_auta], [data_zamowienia], [data_wypozyczenia], [data_zwrotu], [rabat], [uwagi])
VALUES (16, 1, 1, 3,'2022-08-11','2022-08-15','2022-08-29',0.20, 'brak');

INSERT INTO [zamowienia] ([id_zamowienia], [id_reprezentanta], [id_pracownik], [id_auta], [data_zamowienia], [data_wypozyczenia], [data_zwrotu], [rabat], [uwagi])
VALUES (17, 3, 2, 7,'2022-08-20','2022-08-24','2022-09-14',0.30, 'brak');

INSERT INTO [zamowienia] ([id_zamowienia], [id_reprezentanta], [id_pracownik], [id_auta], [data_zamowienia], [data_wypozyczenia], [data_zwrotu], [rabat], [uwagi])
VALUES (18, 4, 2, 8,'2022-08-27','2022-08-29','2022-09-20',0.30, 'brak');

INSERT INTO [zamowienia] ([id_zamowienia], [id_reprezentanta], [id_pracownik], [id_auta], [data_zamowienia], [data_wypozyczenia], [data_zwrotu], [rabat], [uwagi])
VALUES (19, 7, 1, 5,'2022-09-07','2022-09-11','2022-09-18',0.10, 'brak');

INSERT INTO [zamowienia] ([id_zamowienia], [id_reprezentanta], [id_pracownik], [id_auta], [data_zamowienia], [data_wypozyczenia], [data_zwrotu], [rabat], [uwagi])
VALUES (20, 6, 1, 3,'2022-09-15','2022-09-18','2022-09-28',0.10, 'brak');

INSERT INTO [zamowienia] ([id_zamowienia], [id_reprezentanta], [id_pracownik], [id_auta], [data_zamowienia], [data_wypozyczenia], [data_zwrotu], [rabat], [uwagi])
VALUES (21, 5, 3, 2,'2022-09-28','2022-09-30','2022-10-09',0.10, 'brak');

INSERT INTO [zamowienia] ([id_zamowienia], [id_reprezentanta], [id_pracownik], [id_auta], [data_zamowienia], [data_wypozyczenia], [data_zwrotu], [rabat], [uwagi])
VALUES (22, 1, 1, 3,'2022-10-03','2022-10-08','2022-10-28',0.20, 'brak');

INSERT INTO [zamowienia] ([id_zamowienia], [id_reprezentanta], [id_pracownik], [id_auta], [data_zamowienia], [data_wypozyczenia], [data_zwrotu], [rabat], [uwagi])
VALUES (23, 3, 3, 10,'2022-10-10','2022-10-15','2022-11-05',0.30, 'brak');

INSERT INTO [zamowienia] ([id_zamowienia], [id_reprezentanta], [id_pracownik], [id_auta], [data_zamowienia], [data_wypozyczenia], [data_zwrotu], [rabat], [uwagi])
VALUES (24, 4, 1, 9,'2022-10-15','2022-10-25','2022-11-20',0.30, 'brak');

INSERT INTO [zamowienia] ([id_zamowienia], [id_reprezentanta], [id_pracownik], [id_auta], [data_zamowienia], [data_wypozyczenia], [data_zwrotu], [rabat], [uwagi])
VALUES (25, 5, 2, 2,'2022-10-19','2022-10-22','2022-12-05',0.40, 'brak');

INSERT INTO [zamowienia] ([id_zamowienia], [id_reprezentanta], [id_pracownik], [id_auta], [data_zamowienia], [data_wypozyczenia], [data_zwrotu], [rabat], [uwagi])
VALUES (26, 7, 1, 5,'2022-10-24','2022-10-28','2022-11-28',0.40, 'brak');

INSERT INTO [zamowienia] ([id_zamowienia], [id_reprezentanta], [id_pracownik], [id_auta], [data_zamowienia], [data_wypozyczenia], [data_zwrotu], [rabat], [uwagi])
VALUES (27, 6, 1, 3,'2022-11-10','2022-11-13','2022-11-19',0.00, 'brak');

INSERT INTO [zamowienia] ([id_zamowienia], [id_reprezentanta], [id_pracownik], [id_auta], [data_zamowienia], [data_wypozyczenia], [data_zwrotu], [rabat], [uwagi])
VALUES (28, 3, 3, 7,'2022-11-15','2022-11-17','2022-11-23',0.00, 'brak');

INSERT INTO [zamowienia] ([id_zamowienia], [id_reprezentanta], [id_pracownik], [id_auta], [data_zamowienia], [data_wypozyczenia], [data_zwrotu], [rabat], [uwagi])
VALUES (29, 7, 1, 1,'2022-11-21','2022-11-25','2022-12-07',0.10, 'brak');

INSERT INTO [zamowienia] ([id_zamowienia], [id_reprezentanta], [id_pracownik], [id_auta], [data_zamowienia], [data_wypozyczenia], [data_zwrotu], [rabat], [uwagi])
VALUES (30, 5, 3, 2,'2022-12-10','2022-12-16','2022-12-20',0.00, 'brak');

INSERT INTO [zamowienia] ([id_zamowienia], [id_reprezentanta], [id_pracownik], [id_auta], [data_zamowienia], [data_wypozyczenia], [data_zwrotu], [rabat], [uwagi])
VALUES (31, 4, 2, 4,'2022-12-15','2022-12-18','2022-12-24',0.00, 'brak');

INSERT INTO [zamowienia] ([id_zamowienia], [id_reprezentanta], [id_pracownik], [id_auta], [data_zamowienia], [data_wypozyczenia], [data_zwrotu], [rabat], [uwagi])
VALUES (32, 1, 1, 5,'2023-01-10','2023-01-13','2023-01-19',0.00, 'brak');

INSERT INTO [zamowienia] ([id_zamowienia], [id_reprezentanta], [id_pracownik], [id_auta], [data_zamowienia], [data_wypozyczenia], [data_zwrotu], [rabat], [uwagi])
VALUES (33, 3, 3, 7,'2023-03-14','2023-03-16','2023-03-22',0.00, 'brak');

INSERT INTO [zamowienia] ([id_zamowienia], [id_reprezentanta], [id_pracownik], [id_auta], [data_zamowienia], [data_wypozyczenia], [data_zwrotu], [rabat], [uwagi])
VALUES (34, 5, 3, 6,'2023-04-18','2023-04-21','2023-04-27',0.00, 'brak');

INSERT INTO [zamowienia] ([id_zamowienia], [id_reprezentanta], [id_pracownik], [id_auta], [data_zamowienia], [data_wypozyczenia], [data_zwrotu], [rabat], [uwagi])
VALUES (35, 3, 2, 1,'2023-05-21','2023-05-24','2023-07-23',0.30, 'brak');

INSERT INTO [zamowienia] ([id_zamowienia], [id_reprezentanta], [id_pracownik], [id_auta], [data_zamowienia], [data_wypozyczenia], [data_zwrotu], [rabat], [uwagi])
VALUES (36, 1, 1, 5,'2023-06-01','2023-06-04','2023-06-16',0.10, 'brak');

INSERT INTO [zamowienia] ([id_zamowienia], [id_reprezentanta], [id_pracownik], [id_auta], [data_zamowienia], [data_wypozyczenia], [data_zwrotu], [rabat], [uwagi])
VALUES (37, 6, 1, 3,'2023-07-05','2023-07-08','2023-08-14',0.10, 'brak');


----

INSERT INTO [kierowcy] ([id_kierowcy], [id_reprezentanta], [pesel], [nr_prawa_jazdy], [nr_dowodu_os]) VALUES (1, 1, '95050511821', 'F1231234', 'ABC121223');

INSERT INTO [kierowcy] ([id_kierowcy], [id_reprezentanta], [pesel], [nr_prawa_jazdy], [nr_dowodu_os]) VALUES (2, 3, '99050611221', 'Z6558654', 'CXA564879');

INSERT INTO [kierowcy] ([id_kierowcy], [id_reprezentanta], [pesel], [nr_prawa_jazdy], [nr_dowodu_os]) VALUES (3, 4, '98050701231', 'W8895654', 'DRA121871');

INSERT INTO [kierowcy] ([id_kierowcy], [id_reprezentanta], [pesel], [nr_prawa_jazdy], [nr_dowodu_os]) VALUES (4, 5, '99052614221', 'H9878654', 'CRA564889');

INSERT INTO [kierowcy] ([id_kierowcy], [id_reprezentanta], [pesel], [nr_prawa_jazdy], [nr_dowodu_os]) VALUES (5, 6, '95010614551', 'L9866654', 'AWA522647');

INSERT INTO [kierowcy] ([id_kierowcy], [id_reprezentanta], [pesel], [nr_prawa_jazdy], [nr_dowodu_os]) VALUES (6, 7, '95101625321', 'M2255854', 'ZXA111487');

----

INSERT INTO [rola_reprezentanta] ([id_reprezentanta], [rola]) VALUES (1, 'Zamawiaj¹cy');

INSERT INTO [rola_reprezentanta] ([id_reprezentanta], [rola]) VALUES (2, 'Kierowca');

INSERT INTO [rola_reprezentanta] ([id_reprezentanta], [rola]) VALUES (3, 'Zamawiaj¹cy');

INSERT INTO [rola_reprezentanta] ([id_reprezentanta], [rola]) VALUES (3, 'Kierowca');

INSERT INTO [rola_reprezentanta] ([id_reprezentanta], [rola]) VALUES (4, 'Zamawiaj¹cy');

INSERT INTO [rola_reprezentanta] ([id_reprezentanta], [rola]) VALUES (4, 'Kierowca');

INSERT INTO [rola_reprezentanta] ([id_reprezentanta], [rola]) VALUES (5, 'Zamawiaj¹cy');

INSERT INTO [rola_reprezentanta] ([id_reprezentanta], [rola]) VALUES (5, 'Kierowca');

INSERT INTO [rola_reprezentanta] ([id_reprezentanta], [rola]) VALUES (6, 'Zamawiaj¹cy');

INSERT INTO [rola_reprezentanta] ([id_reprezentanta], [rola]) VALUES (6, 'Kierowca');

INSERT INTO [rola_reprezentanta] ([id_reprezentanta], [rola]) VALUES (7, 'Zamawiaj¹cy');

INSERT INTO [rola_reprezentanta] ([id_reprezentanta], [rola]) VALUES (7, 'Kierowca');

----

INSERT INTO [wydanie_auta] ([id_zamowienia], [data_wydania], [godzina_wydania], [id_kierowcy], [id_wydajacego_pojazd]) VALUES (1,'2022-05-18','12:00:00', 1, 1);

INSERT INTO [wydanie_auta] ([id_zamowienia], [data_wydania], [godzina_wydania], [id_kierowcy], [id_wydajacego_pojazd]) VALUES (2,'2022-05-16','11:00:00', 2, 2);

INSERT INTO [wydanie_auta] ([id_zamowienia], [data_wydania], [godzina_wydania], [id_kierowcy], [id_wydajacego_pojazd]) VALUES (3,'2022-05-20','10:30:00', 3, 2);

INSERT INTO [wydanie_auta] ([id_zamowienia], [data_wydania], [godzina_wydania], [id_kierowcy], [id_wydajacego_pojazd]) VALUES (4,'2022-05-28','10:00:00', 1, 3);

INSERT INTO [wydanie_auta] ([id_zamowienia], [data_wydania], [godzina_wydania], [id_kierowcy], [id_wydajacego_pojazd]) VALUES (5,'2022-05-29','09:00:00', 4, 1);

INSERT INTO [wydanie_auta] ([id_zamowienia], [data_wydania], [godzina_wydania], [id_kierowcy], [id_wydajacego_pojazd]) VALUES (6,'2022-06-08','08:30:00', 5, 2);

INSERT INTO [wydanie_auta] ([id_zamowienia], [data_wydania], [godzina_wydania], [id_kierowcy], [id_wydajacego_pojazd]) VALUES (7,'2022-06-18','09:00:00', 2, 1);

INSERT INTO [wydanie_auta] ([id_zamowienia], [data_wydania], [godzina_wydania], [id_kierowcy], [id_wydajacego_pojazd]) VALUES (8,'2022-06-26','09:30:00', 6, 3);

INSERT INTO [wydanie_auta] ([id_zamowienia], [data_wydania], [godzina_wydania], [id_kierowcy], [id_wydajacego_pojazd]) VALUES (9,'2022-06-29','10:00:00', 4, 3);

INSERT INTO [wydanie_auta] ([id_zamowienia], [data_wydania], [godzina_wydania], [id_kierowcy], [id_wydajacego_pojazd]) VALUES (10,'2022-07-05','09:30:00', 1, 2);

INSERT INTO [wydanie_auta] ([id_zamowienia], [data_wydania], [godzina_wydania], [id_kierowcy], [id_wydajacego_pojazd]) VALUES (11,'2022-07-15','08:00:00', 5, 2);

INSERT INTO [wydanie_auta] ([id_zamowienia], [data_wydania], [godzina_wydania], [id_kierowcy], [id_wydajacego_pojazd]) VALUES (12,'2022-07-17','11:00:00', 6, 3);

INSERT INTO [wydanie_auta] ([id_zamowienia], [data_wydania], [godzina_wydania], [id_kierowcy], [id_wydajacego_pojazd]) VALUES (13,'2022-07-26','12:00:00', 3, 3);

INSERT INTO [wydanie_auta] ([id_zamowienia], [data_wydania], [godzina_wydania], [id_kierowcy], [id_wydajacego_pojazd]) VALUES (14,'2022-07-30','16:00:00', 4, 3);

INSERT INTO [wydanie_auta] ([id_zamowienia], [data_wydania], [godzina_wydania], [id_kierowcy], [id_wydajacego_pojazd]) VALUES (15,'2022-08-14','09:00:00', 5, 3);

INSERT INTO [wydanie_auta] ([id_zamowienia], [data_wydania], [godzina_wydania], [id_kierowcy], [id_wydajacego_pojazd]) VALUES (16,'2022-08-15','09:00:00', 1, 1);

INSERT INTO [wydanie_auta] ([id_zamowienia], [data_wydania], [godzina_wydania], [id_kierowcy], [id_wydajacego_pojazd]) VALUES (17,'2022-08-24','09:30:00', 2, 2);

INSERT INTO [wydanie_auta] ([id_zamowienia], [data_wydania], [godzina_wydania], [id_kierowcy], [id_wydajacego_pojazd]) VALUES (18,'2022-08-29','10:00:00', 3, 2);

INSERT INTO [wydanie_auta] ([id_zamowienia], [data_wydania], [godzina_wydania], [id_kierowcy], [id_wydajacego_pojazd]) VALUES (19,'2022-09-11','09:30:00', 6, 1);

INSERT INTO [wydanie_auta] ([id_zamowienia], [data_wydania], [godzina_wydania], [id_kierowcy], [id_wydajacego_pojazd]) VALUES (20,'2022-09-18','12:30:00', 5, 1);

INSERT INTO [wydanie_auta] ([id_zamowienia], [data_wydania], [godzina_wydania], [id_kierowcy], [id_wydajacego_pojazd]) VALUES (21,'2022-09-30','08:30:00', 4, 3);

INSERT INTO [wydanie_auta] ([id_zamowienia], [data_wydania], [godzina_wydania], [id_kierowcy], [id_wydajacego_pojazd]) VALUES (22,'2022-10-08','09:00:00', 1, 3);

INSERT INTO [wydanie_auta] ([id_zamowienia], [data_wydania], [godzina_wydania], [id_kierowcy], [id_wydajacego_pojazd]) VALUES (23,'2022-10-15','09:00:00', 2, 1);

INSERT INTO [wydanie_auta] ([id_zamowienia], [data_wydania], [godzina_wydania], [id_kierowcy], [id_wydajacego_pojazd]) VALUES (24,'2022-10-25','09:30:00', 3, 2);

INSERT INTO [wydanie_auta] ([id_zamowienia], [data_wydania], [godzina_wydania], [id_kierowcy], [id_wydajacego_pojazd]) VALUES (25,'2022-10-22','12:00:00', 4, 1);

INSERT INTO [wydanie_auta] ([id_zamowienia], [data_wydania], [godzina_wydania], [id_kierowcy], [id_wydajacego_pojazd]) VALUES (26,'2022-10-28','15:00:00', 6, 3);

INSERT INTO [wydanie_auta] ([id_zamowienia], [data_wydania], [godzina_wydania], [id_kierowcy], [id_wydajacego_pojazd]) VALUES (27,'2022-11-13','11:00:00', 5, 3);

INSERT INTO [wydanie_auta] ([id_zamowienia], [data_wydania], [godzina_wydania], [id_kierowcy], [id_wydajacego_pojazd]) VALUES (28,'2022-11-17','12:00:00', 2, 1);

INSERT INTO [wydanie_auta] ([id_zamowienia], [data_wydania], [godzina_wydania], [id_kierowcy], [id_wydajacego_pojazd]) VALUES (29,'2022-11-25','16:00:00', 6, 1);

INSERT INTO [wydanie_auta] ([id_zamowienia], [data_wydania], [godzina_wydania], [id_kierowcy], [id_wydajacego_pojazd]) VALUES (30,'2022-12-16','09:00:00', 4, 3);

INSERT INTO [wydanie_auta] ([id_zamowienia], [data_wydania], [godzina_wydania], [id_kierowcy], [id_wydajacego_pojazd]) VALUES (31,'2022-12-18','09:00:00', 3, 3);

INSERT INTO [wydanie_auta] ([id_zamowienia], [data_wydania], [godzina_wydania], [id_kierowcy], [id_wydajacego_pojazd]) VALUES (32,'2023-01-13','09:30:00', 1, 1);

INSERT INTO [wydanie_auta] ([id_zamowienia], [data_wydania], [godzina_wydania], [id_kierowcy], [id_wydajacego_pojazd]) VALUES (33,'2023-03-16','10:00:00', 2, 3);

INSERT INTO [wydanie_auta] ([id_zamowienia], [data_wydania], [godzina_wydania], [id_kierowcy], [id_wydajacego_pojazd]) VALUES (34,'2023-04-21','09:30:00', 4, 3);

INSERT INTO [wydanie_auta] ([id_zamowienia], [data_wydania], [godzina_wydania], [id_kierowcy], [id_wydajacego_pojazd]) VALUES (35,'2023-05-24','12:30:00', 2, 3);

INSERT INTO [wydanie_auta] ([id_zamowienia], [data_wydania], [godzina_wydania], [id_kierowcy], [id_wydajacego_pojazd]) VALUES (36,'2023-06-04','16:00:00', 1, 1);

INSERT INTO [wydanie_auta] ([id_zamowienia], [data_wydania], [godzina_wydania], [id_kierowcy], [id_wydajacego_pojazd]) VALUES (37,'2023-07-08','09:00:00', 5, 1);

----

INSERT INTO [zwrot_auta] ([id_zamowienia], [data_zwrotu], [godzina_zwrotu], [id_kierowcy], [id_przyjmujacego_pojazd], [doplata], [uwagi])
VALUES (1,'2022-05-22','11:00:00', 1, 1,0.00, 'brak');

INSERT INTO [zwrot_auta] ([id_zamowienia], [data_zwrotu], [godzina_zwrotu], [id_kierowcy], [id_przyjmujacego_pojazd], [doplata], [uwagi])
VALUES (2,'2022-05-20','15:00:00', 2, 1,0.00, 'brak');

INSERT INTO [zwrot_auta] ([id_zamowienia], [data_zwrotu], [godzina_zwrotu], [id_kierowcy], [id_przyjmujacego_pojazd], [doplata], [uwagi])
VALUES (3,'2022-05-28','10:00:00', 3, 2,0.00, 'brak');

INSERT INTO [zwrot_auta] ([id_zamowienia], [data_zwrotu], [godzina_zwrotu], [id_kierowcy], [id_przyjmujacego_pojazd], [doplata], [uwagi])
VALUES (4,'2022-06-08','11:00:00', 1, 3,0.00, 'brak');

INSERT INTO [zwrot_auta] ([id_zamowienia], [data_zwrotu], [godzina_zwrotu], [id_kierowcy], [id_przyjmujacego_pojazd], [doplata], [uwagi])
VALUES (5,'2022-06-12','10:00:00', 4, 1,0.00, 'brak');

INSERT INTO [zwrot_auta] ([id_zamowienia], [data_zwrotu], [godzina_zwrotu], [id_kierowcy], [id_przyjmujacego_pojazd], [doplata], [uwagi])
VALUES (6,'2022-06-18','09:00:00', 5, 1,0.00, 'brak');

INSERT INTO [zwrot_auta] ([id_zamowienia], [data_zwrotu], [godzina_zwrotu], [id_kierowcy], [id_przyjmujacego_pojazd], [doplata], [uwagi])
VALUES (7,'2022-06-25','09:30:00', 2, 1,0.00, 'brak');

INSERT INTO [zwrot_auta] ([id_zamowienia], [data_zwrotu], [godzina_zwrotu], [id_kierowcy], [id_przyjmujacego_pojazd], [doplata], [uwagi])
VALUES (8,'2022-06-30','09:00:00', 6, 3,0.00, 'brak');

INSERT INTO [zwrot_auta] ([id_zamowienia], [data_zwrotu], [godzina_zwrotu], [id_kierowcy], [id_przyjmujacego_pojazd], [doplata], [uwagi])
VALUES (9,'2022-07-02','09:00:00', 4, 3,0.00, 'brak');

INSERT INTO [zwrot_auta] ([id_zamowienia], [data_zwrotu], [godzina_zwrotu], [id_kierowcy], [id_przyjmujacego_pojazd], [doplata], [uwagi])
VALUES (10,'2022-07-15','09:30:00', 1, 2,0.00, 'brak');

INSERT INTO [zwrot_auta] ([id_zamowienia], [data_zwrotu], [godzina_zwrotu], [id_kierowcy], [id_przyjmujacego_pojazd], [doplata], [uwagi])
VALUES (11,'2022-07-19','09:00:00', 5, 1,0.00, 'brak');

INSERT INTO [zwrot_auta] ([id_zamowienia], [data_zwrotu], [godzina_zwrotu], [id_kierowcy], [id_przyjmujacego_pojazd], [doplata], [uwagi])
VALUES (12,'2022-07-22','09:00:00', 6, 3,0.00, 'brak');

INSERT INTO [zwrot_auta] ([id_zamowienia], [data_zwrotu], [godzina_zwrotu], [id_kierowcy], [id_przyjmujacego_pojazd], [doplata], [uwagi])
VALUES (13,'2022-07-29','10:00:00', 3, 3,0.00, 'brak');

INSERT INTO [zwrot_auta] ([id_zamowienia], [data_zwrotu], [godzina_zwrotu], [id_kierowcy], [id_przyjmujacego_pojazd], [doplata], [uwagi])
VALUES (14,'2022-08-22','09:00:00', 4, 3,0.00, 'brak');

INSERT INTO [zwrot_auta] ([id_zamowienia], [data_zwrotu], [godzina_zwrotu], [id_kierowcy], [id_przyjmujacego_pojazd], [doplata], [uwagi])
VALUES (15,'2022-08-24','09:00:00', 5, 3,200.00, 'dop³ata za tankowanie');

INSERT INTO [zwrot_auta] ([id_zamowienia], [data_zwrotu], [godzina_zwrotu], [id_kierowcy], [id_przyjmujacego_pojazd], [doplata], [uwagi])
VALUES (16,'2022-08-29','10:00:00', 1, 1,0.00, 'brak');

INSERT INTO [zwrot_auta] ([id_zamowienia], [data_zwrotu], [godzina_zwrotu], [id_kierowcy], [id_przyjmujacego_pojazd], [doplata], [uwagi])
VALUES (17,'2022-09-14','09:00:00', 2, 3,0.00, 'brak');

INSERT INTO [zwrot_auta] ([id_zamowienia], [data_zwrotu], [godzina_zwrotu], [id_kierowcy], [id_przyjmujacego_pojazd], [doplata], [uwagi])
VALUES (18,'2022-09-20','12:00:00', 3, 2,0.00, 'brak');

INSERT INTO [zwrot_auta] ([id_zamowienia], [data_zwrotu], [godzina_zwrotu], [id_kierowcy], [id_przyjmujacego_pojazd], [doplata], [uwagi])
VALUES (19,'2022-09-18','09:00:00', 6, 1,0.00, 'brak');

INSERT INTO [zwrot_auta] ([id_zamowienia], [data_zwrotu], [godzina_zwrotu], [id_kierowcy], [id_przyjmujacego_pojazd], [doplata], [uwagi])
VALUES (20,'2022-09-28','10:00:00', 5, 1,200.00, 'dop³ata za tankowanie');

INSERT INTO [zwrot_auta] ([id_zamowienia], [data_zwrotu], [godzina_zwrotu], [id_kierowcy], [id_przyjmujacego_pojazd], [doplata], [uwagi])
VALUES (21,'2022-10-09','12:00:00', 4, 3,0.00, 'brak');

INSERT INTO [zwrot_auta] ([id_zamowienia], [data_zwrotu], [godzina_zwrotu], [id_kierowcy], [id_przyjmujacego_pojazd], [doplata], [uwagi])
VALUES (22,'2022-10-28','09:00:00', 1, 3,0.00, 'brak');

INSERT INTO [zwrot_auta] ([id_zamowienia], [data_zwrotu], [godzina_zwrotu], [id_kierowcy], [id_przyjmujacego_pojazd], [doplata], [uwagi])
VALUES (23,'2022-11-05','09:00:00', 2, 1,0.00, 'brak');

INSERT INTO [zwrot_auta] ([id_zamowienia], [data_zwrotu], [godzina_zwrotu], [id_kierowcy], [id_przyjmujacego_pojazd], [doplata], [uwagi])
VALUES (24,'2022-11-20','10:00:00', 3, 1,0.00, 'brak');

INSERT INTO [zwrot_auta] ([id_zamowienia], [data_zwrotu], [godzina_zwrotu], [id_kierowcy], [id_przyjmujacego_pojazd], [doplata], [uwagi])
VALUES (25,'2022-12-05','09:00:00', 4, 1,0.00, 'brak');

INSERT INTO [zwrot_auta] ([id_zamowienia], [data_zwrotu], [godzina_zwrotu], [id_kierowcy], [id_przyjmujacego_pojazd], [doplata], [uwagi])
VALUES (26,'2022-11-28','12:00:00', 6, 3,0.00, 'brak');

INSERT INTO [zwrot_auta] ([id_zamowienia], [data_zwrotu], [godzina_zwrotu], [id_kierowcy], [id_przyjmujacego_pojazd], [doplata], [uwagi])
VALUES (27,'2022-11-19','09:00:00', 5, 3,0.00, 'brak');

INSERT INTO [zwrot_auta] ([id_zamowienia], [data_zwrotu], [godzina_zwrotu], [id_kierowcy], [id_przyjmujacego_pojazd], [doplata], [uwagi])
VALUES (28,'2022-11-23','09:00:00', 2, 1,0.00, 'brak');

INSERT INTO [zwrot_auta] ([id_zamowienia], [data_zwrotu], [godzina_zwrotu], [id_kierowcy], [id_przyjmujacego_pojazd], [doplata], [uwagi])
VALUES (29,'2022-12-07','09:30:00', 6, 1,0.00, 'brak');

INSERT INTO [zwrot_auta] ([id_zamowienia], [data_zwrotu], [godzina_zwrotu], [id_kierowcy], [id_przyjmujacego_pojazd], [doplata], [uwagi])
VALUES (30,'2022-12-20','12:00:00', 4, 3,0.00, 'brak');

INSERT INTO [zwrot_auta] ([id_zamowienia], [data_zwrotu], [godzina_zwrotu], [id_kierowcy], [id_przyjmujacego_pojazd], [doplata], [uwagi])
VALUES (31,'2022-12-24','09:00:00', 3, 3,0.00, 'brak');

INSERT INTO [zwrot_auta] ([id_zamowienia], [data_zwrotu], [godzina_zwrotu], [id_kierowcy], [id_przyjmujacego_pojazd], [doplata], [uwagi])
VALUES (32,'2023-01-19','10:00:00', 1, 1,0.00, 'brak');

INSERT INTO [zwrot_auta] ([id_zamowienia], [data_zwrotu], [godzina_zwrotu], [id_kierowcy], [id_przyjmujacego_pojazd], [doplata], [uwagi])
VALUES (33,'2023-03-22','09:00:00', 2, 1,0.00, 'brak');

INSERT INTO [zwrot_auta] ([id_zamowienia], [data_zwrotu], [godzina_zwrotu], [id_kierowcy], [id_przyjmujacego_pojazd], [doplata], [uwagi])
VALUES (34,'2023-04-27','12:00:00', 4, 3,0.00, 'brak');

----

INSERT INTO [stan_auta_info] ([id_auta], [stan_auta], [data_nastepnego_przegladu]) VALUES (1, 1,'2023-05-12');

INSERT INTO [stan_auta_info] ([id_auta], [stan_auta], [data_nastepnego_przegladu]) VALUES (2, 1,'2023-04-10');

INSERT INTO [stan_auta_info] ([id_auta], [stan_auta], [data_nastepnego_przegladu]) VALUES (3, 1,'2023-12-10');

INSERT INTO [stan_auta_info] ([id_auta], [stan_auta], [data_nastepnego_przegladu]) VALUES (4, 1,'2023-10-10');

INSERT INTO [stan_auta_info] ([id_auta], [stan_auta], [data_nastepnego_przegladu]) VALUES (5, 1,'2023-11-10');

INSERT INTO [stan_auta_info] ([id_auta], [stan_auta], [data_nastepnego_przegladu]) VALUES (6, 1,'2023-12-05');

INSERT INTO [stan_auta_info] ([id_auta], [stan_auta], [data_nastepnego_przegladu]) VALUES (7, 1,'2023-04-10');

INSERT INTO [stan_auta_info] ([id_auta], [stan_auta], [data_nastepnego_przegladu]) VALUES (8, 1,'2023-05-10');

INSERT INTO [stan_auta_info] ([id_auta], [stan_auta], [data_nastepnego_przegladu]) VALUES (9, 1,'2023-07-15');

INSERT INTO [stan_auta_info] ([id_auta], [stan_auta], [data_nastepnego_przegladu]) VALUES (10, 1,'2023-08-10');

INSERT INTO [stan_auta_info] ([id_auta], [stan_auta], [data_nastepnego_przegladu]) VALUES (11, 1,'2023-09-03');