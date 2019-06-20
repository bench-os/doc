import matplotlib.pyplot as plt
import csv 
import sys

values = {}

with open(sys.argv[1], 'r') as f:
    for line in f:
        v = float(line)
        if v not in values:
            values[v] = 1
        else:
            values[v] = values[v] + 1

xmax = max(values.keys())
xmin = min(values.keys())

size = (xmax - xmin) / (len(values.keys()))
if size == 0:
    size = .05


plt.bar(values.keys(),values.values(), width=size, edgecolor='purple', color='purple', alpha=0.3)

plt.xlabel('Time (usec)')
plt.ylabel('Hits (log)')
plt.yscale("log")
plt.grid(True, which='both', axis='both', linewidth=0.2)


plt.xlim([xmin-size, xmax+size])

#plt.show()
plt.savefig(sys.argv[2])
