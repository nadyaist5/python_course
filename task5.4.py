import csv
import collections
from collections import OrderedDict

d = {}
with open('stage3_test.csv', 'r', encoding='utf8') as f:
    reader = csv.DictReader(f, delimiter=',')
    for row in reader:
        d[row["Id"]] = float(row["Price"])

    ord_dict = OrderedDict(sorted(d.items(), key=lambda t: t[1]))
    ord_dict_rev = OrderedDict(sorted(d.items(), reverse=True, key=lambda t: t[1]))

print(ord_dict)
print(ord_dict_rev)

