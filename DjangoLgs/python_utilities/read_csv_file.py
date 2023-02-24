import csv

# Per una complteta descrizione Reading and writng file in Python: Reading and Writing CSV Files in Python
# https://realpython.com/python-csv/

## List of String Elemnts
""" with open('data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
            line_count += 1
    print(f'Processed {line_count} lines.') """
    
## Reading CSV Files Into a Dictionary

with open('data.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        print(f'\t{row["AUDITOR"]} works in the {row["SITO"]} department, and was born in Rome.')
        line_count += 1
    print(f'Processed {line_count} lines.')