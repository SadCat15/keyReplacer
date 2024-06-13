from csv import reader, writer
from random import randint

dostawcy = []
magazynw = []
dostawcy_keys = []
nrKlienta = []
dostawcy_file = "Dostawcy.csv"
magazynw_file = "Magazynw.csv"


def read_files():
    with open(dostawcy_file, newline="\n") as csv:
        csvreader = reader(csv, delimiter=';')
        for row in csvreader:
            dostawcy.append(row)
            dostawcy_keys.append(row[0])

    with open(magazynw_file, newline="\n") as csv:
        csvreader = reader(csv, delimiter=';')
        for row in csvreader:
            magazynw.append(row)
            nrKlienta.append(row[-1])


def replace():
    for i in range(len(nrKlienta)):
        if nrKlienta[i] not in dostawcy_keys:
            nrKlienta[i] = dostawcy_keys[randint(0, len(dostawcy_keys) - 1)]


def correct_data():
    for i in range(len(magazynw)):
        if i == 0:
            continue
        if magazynw[i][-1] != nrKlienta[i]:
            magazynw[i][-1] = nrKlienta[i]
    print("Poprawiono klucze niezgodne na losowe klucze")


def save_to_file():
    with open(magazynw_file, mode='w', newline='\n') as file:
        csvwriter = writer(file, delimiter=';')
        for row in magazynw:
            csvwriter.writerow(row)
    print(f"zapisano do pliku: {magazynw_file}")


def main():
    read_files()
    replace()
    correct_data()
    save_to_file()


if __name__ == "__main__":
    main()
