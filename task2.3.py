import csv

data = []
with open('stage3_test.csv', 'r', encoding='utf8') as f:
    reader = csv.DictReader(f, delimiter=',')
    for row in reader:
        del(row['Images'], row['Description'])
        data.append(row)

with open('task3.csv', 'w', encoding='utf8') as f:
    fieldnames = ["Id","Title","Price"]
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for row in data:
        writer.writerow(row)

