import csv

with open('stage3_test.csv', 'r', encoding='utf8') as f:
    reader = csv.reader(f)
    with open('normal_price.csv', 'w', encoding='utf8') as g:
        writer = csv.writer(g)
        for row in reader:
            if (row[4] == "Price"):
                writer.writerow(row)
                continue
            if 10000 < float(row[4]) <= 50000:
                writer.writerow(row)
