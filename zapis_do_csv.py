''' Program odbiera ścieżkę np. Styczeń/Poniedziałek/rano/ i obsługuje plik Dane.csv '''

import csv
from pathlib import Path
import random

def zapis_do_csv(katalog: Path):
    ''' Uzupełnia lub tworzy plik Dane.csv w przekazanym kalatogu. '''
    if not katalog.exists():
        print("Przekazany katalog", katalog, "nie istnieje!")
    else: 
        with open(katalog / "Dane.csv", "w", newline="") as Dane_csv:
            wczyt = csv.writer(Dane_csv, delimiter=';')   # ; zamiast ,
            # pierwszy wiersz
            wczyt.writerow(["Model", "Wynik", "Czas", ""])
            # drugi wiersz:
            wczyt.writerow([random.choice("ABC"), random.randint(0,1000), f"{random.randint(0,1000)}s", ""]) 

def odczyt_z_csv(katalog: Path):
    ''' Odczytuje z Dane.csv w przekazanym katalogu -- jeżeli Model A, to przekazuje
        Czas, a jeżeli Model to B lub C, to przekazuje 0'''
    if not katalog.exists() or not (katalog / "Dane.csv").exists():
        print("Nie istnieje, bądź przekazana ścieżka, bądź plik Dane.csv.")
        return None
    with open(katalog / "Dane.csv", newline="", encoding="utf-8") as Dane_csv:
        odczyt = csv.reader(Dane_csv, delimiter=";")
        next(odczyt) # nagłówek pomijam
        model, wynik, czas, pusto = [x.strip() for x in next(odczyt)] # .strip() czyści białe znaki z napisu            

    return (int)(czas[:-1]) if model == "A" else 0