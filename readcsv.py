import csv
import checkfile
holl_dict = {}
with open('/Users/dengshiqi/Desktop/test/csv/2021-1-21-1.csv','r') as f:
    reader = csv.reader(f)
    for row in reader:
        key = row[1]
        holl_dict[key] = row[2:]