values = []

with open('data.txt', 'r') as f:
    for row in f:
        values.append(int(row))

for v in values:
    v = (v/32768) * 10 ** 6
    print(v)
