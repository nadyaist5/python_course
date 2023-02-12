import csv

data = []
with open('stage3_test.csv', 'r', encoding='utf8') as f:
    reader = csv.DictReader(f, delimiter=',')
    for row in reader:
        if (len(row['Images'].split(',')) > 3):
            data.append(row)
            print(row['Images'])

with open('3images.csv', 'w', encoding='utf8') as f:
    fieldnames = ["Id","Images","Title","Description","Price"]
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for row in data:
        writer.writerow(row)