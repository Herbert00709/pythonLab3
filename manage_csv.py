''' Program odbiera ścieżkę np. Styczeń/Poniedziałek/rano/ i obsługuje plik Dane.csv '''

import csv
from pathlib import Path
import random

def write_to_csv(directory: Path, filename: str = "Dane.csv") -> None:
    ''' Uzupełnia lub tworzy plik Dane.csv w przekazanym kalatogu. '''
    if not directory.exists():
        raise ValueError("Przekazany directory", directory, "nie istnieje!")
    else: 
        with open(directory / filename, "w", newline="") as Dane_csv:
            wczyt = csv.writer(Dane_csv, delimiter=';')   # ; zamiast ,
            # first line:
            wczyt.writerow(["Model", "Wynik", "Czas", ""])
            # second line:
            wczyt.writerow([random.choice("ABC"), random.randint(0,1000), f"{random.randint(0,1000)}s", ""]) 

def read_from_csv(directory: Path, filename: str = "Dane.csv") -> int | None:
    ''' Odczytuje z Dane.csv w przekazanym directory -- jeżeli Model A, to przekazuje
        Czas, a jeżeli Model to B lub C, to przekazuje 0'''
    if not directory.exists() or not (directory / filename).exists():
        raise ValueError("Nie istnieje, bądź przekazana ścieżka, bądź plik", filename)
        return None
    with open(directory / filename, newline="", encoding="utf-8") as Dane_csv:
        odczyt = csv.reader(Dane_csv, delimiter=";")
        next(odczyt) # passing the header
        model, wynik, czas, pusto = [x.strip() for x in next(odczyt)] # .strip() removes whitespaces

    return (int)(czas[:-1]) if model == "A" else 0
