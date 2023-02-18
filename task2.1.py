import csv

with open('stage3_test.csv', 'r', encoding='utf8') as f:
    reader = csv.DictReader(f, delimiter=',')
    with open('3images.csv', 'w', encoding='utf8') as g:
        writer = csv.DictWriter(g, fieldnames=reader.fieldnames)
        writer.writeheader()

        for row in reader:
            if (len(row['Images'].split(',')) > 3):
                writer.writerow(row)
