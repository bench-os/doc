import csv 
import sys

with open(sys.argv[1], 'r') as f:
    data = csv.reader(f, delimiter=',')
    next(data) # Skip header
    for row in data:
        for _ in range(int(row[1])):
            print(float(row[0])*10**6)

