import csv


def save_CSV(file, names, list):
    with open(file, mode="w", encoding='utf-8-sig') as wFile:
        fileWriter = csv.DictWriter(wFile, lineterminator="\r", fieldnames=names)
        fileWriter.writeheader()
        fileWriter.writerows(list)
        fileWriter.writerow({f"{names[0]}": "PC4", f"{names[1]}": "10.125.43.20;E4-A7-A0-5C-A2-AA"})
        fileWriter.writerow({f"{names[0]}": "PC5", f"{names[1]}": "10.125.43.19;E4-A7-A0-5C-A2-K7"})


def get_csv_data(file) -> (list, list):
    with open(file, encoding='utf-8-sig') as rFile:
        fileReader = csv.DictReader(rFile)
        return list(fileReader.fieldnames), [row for row in fileReader]


if __name__ == "__main__":
    fieldnames, row1 = get_csv_data("Zadanie1.csv")
    save_CSV("new_Zadanie1.csv", fieldnames, row1)

