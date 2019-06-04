import matplotlib.pyplot as plt
import csv 
import sys

x = []
y = []

with open(sys.argv[1], 'r') as f:
    data = csv.reader(f, delimiter=',')
    next(data) # Skip header
    for row in data:
        x.append(float(row[0])*10**6) # Time
        y.append(float(row[1])) # Hits

xfirst = list(map(lambda i: i > 0, y)).index(True)
xlast = len(y) - list(map(lambda i: i > 0, reversed(y))).index(True)

xmin = x[xfirst]
xmax = x[xlast]
size = (xmax - xmin)/10

plt.bar(x,y, width=size)
plt.xlabel('Time (usec)')
plt.ylabel('Hits (log)')
plt.yscale("log")
plt.grid(True, which='both', axis='both', linewidth=0.2)
plt.xlim(left=x[xfirst-1], right=x[xlast+1])

#plt.show()
plt.savefig(sys.argv[1].split('.')[0]+'-plot.png')
