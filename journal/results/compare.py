import matplotlib.pyplot as plt
import sys

values1 = {}

with open(sys.argv[1], 'r') as f:
    for line in f:
        v = float(line)
        if v not in values1:
            values1[v] = 1
        else:
            values1[v] = values1[v] + 1

xmax1 = max(values1.keys())
xmin1 = min(values1.keys())


values2 = {}

with open(sys.argv[2], 'r') as f:
    for line in f:
        v = float(line)
        if v not in values2:
            values2[v] = 1
        else:
            values2[v] = values2[v] + 1

xmax2 = max(values2.keys())
xmin2 = min(values2.keys())

xmax = max(xmax1, xmax2)
xmin = min(xmin1, xmin2)

if len(sys.argv) > 4:
    values3 = {}

    with open(sys.argv[3], 'r') as f:
        for line in f:
            v = float(line)
            if v not in values3:
                values3[v] = 1
            else:
                values3[v] = values3[v] + 1

    xmax3 = max(values3.keys())
    xmin3 = min(values3.keys())

    xmax = max(xmax, xmax3)
    xmin = min(xmin, xmin3)



size = (xmax - xmin) / (len(values1.keys()) + len(values2.keys()))

plt.bar(values1.keys(), values1.values(), width=size, edgecolor='purple', color='purple', alpha=0.8)
plt.bar(values2.keys(), values2.values(), width=size, edgecolor='orange', color='orange', alpha=0.3)

if len(sys.argv) > 4: 
    plt.bar(values3.keys(), values3.values(), width=size, edgecolor='green', color='green', alpha=0.5)

plt.xlabel('Time (usec)')
plt.ylabel('Hits (log)')
plt.yscale("log")
plt.grid(True, which='both', axis='both', linewidth=0.2)

if len(sys.argv) > 4:
    plt.legend(['Reference values', 'Extension approach values', 'Devices approach values'])
else:
    plt.legend(['Reference values', 'Framework values'])

plt.xlim([xmin-size, xmax+size])

#plt.show()

if len(sys.argv) > 4:
    plt.savefig(sys.argv[4])
else:
    plt.savefig(sys.argv[3])
