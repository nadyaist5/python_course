import csv

data = []
with open('stage3_test.csv', 'r', encoding='utf8') as f:
    reader = csv.reader(f)
    for row in reader:
        if (row[4] == "Price"):
            data.append(row)
            continue
        if (float(row[4]) > 10000) and (float(row[4]) <= 50000):
            data.append(row)
            print(row[4])

with open('normal_price.csv', 'w', encoding='utf8') as f:
    writer = csv.writer(f)
    for row in data:
        writer.writerow(row)