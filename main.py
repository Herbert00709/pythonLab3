import argparse

parser = argparse.ArgumentParser()
parser.add_argument(
    '-m', '--miesiace', nargs='+', help='TODO lista miesiecy', required=True
)
parser.add_argument(
    '-d', '--dni_tygodnia', nargs='+', help='TODO lista zakresów dni tygodnia', required=True
)
parser.add_argument(
    '-p', '--pory_dnia', nargs='+', help='TODO lista pór dni, domyslnie rano'
)
coRobic = parser.add_mutually_exclusive_group(required=True)
coRobic.add_argument(
    '-t', '--tworzenie', action='store_true'
)
coRobic.add_argument(
    '-o', '--odczyt', action='store_true'
)
format = parser.add_mutually_exclusive_group(required=True)
format.add_argument(
    '-c', '--csv', action='store_true'
)
format.add_argument(
    '-j', '--json', action='store_true'
)

args = parser.parse_args()

print(args);


# parser.add_argument('-l','--list', nargs='+', help='<Required> Set flag', required=True)
# # Use like:
# # python arg.py -l 1234 2345 3456 4567

# python3 main.py -m styczen luty -d pn-wt pt -p r w -t -c