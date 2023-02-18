import csv

with open('stage3_test.csv', 'r', encoding='utf8') as f:
    reader = csv.DictReader(f, delimiter=',')
    with open('task3.csv', 'w', encoding='utf8') as g:
        fieldnames = ["Id", "Title", "Price"]
        writer = csv.DictWriter(g, fieldnames=fieldnames)
        writer.writeheader()
        for row in reader:
            del(row['Images'], row['Description'])
            writer.writerow(row)
