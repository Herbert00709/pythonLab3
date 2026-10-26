import argparse
import paths as Paths
import pathlib
import zapis_do_csv

parser = argparse.ArgumentParser()
parser.add_argument(
    '-m', '--miesiace', nargs='+', help='lista miausiecy', required=True
)
parser.add_argument(
    '-d', '--dni_tygodnia', nargs='+', help='lista zakresów dni tygodnia', required=True
)
parser.add_argument(
    '-p', '--pory_dnia', nargs='+', help='lista purrr dni, domyslnie rano'
)
coRobic = parser.add_mutually_exclusive_group(required=True)
coRobic.add_argument(
    '-t', '--tworzenie', action='store_true', help='tworzenie plików, wyłączny z odczytem'
)
coRobic.add_argument(
    '-o', '--odczyt', action='store_true', help='odczyt plików, wyłączny z tworzeniem'
)
format = parser.add_mutually_exclusive_group(required=True)
format.add_argument(
    '-c', '--csv', action='store_true', help='operacje na plikach typu csv, wyłączne z json'
)
format.add_argument(
    '-j', '--json', action='store_true', help='operacje na plikach typu json, wyłączne z csv'
)

args = parser.parse_args()

if args.csv:
    paths = Paths.create_path(args.miesiace, args.dni_tygodnia, args.pory_dnia)

    if args.tworzenie:
        for path in paths:
            path.mkdir(parents=True, exist_ok=True)
            zapis_do_csv.zapis_do_csv(path)
    else: # args.odczyt
        sum = 0
        for path in paths:
            sum += zapis_do_csv.odczyt_z_csv(path)
            
        print(f"Suma czasów modeli A: {sum}")
        
else: # args.json
    print("json obecnie nie jest wspierany.")
