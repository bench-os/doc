import matplotlib.pyplot as plt
import sys

values = {}
values_ = []
with open(sys.argv[1], 'r') as f:
    for line in f:
        if sys.argv[2] == 'riot':
            v = float(line)
        else:
            v = (int(line) / 32768) * 10**6
        values_.append(v)
        if v not in values:
            values[v] = 1
        else:
            values[v] = values[v] + 1

xmax = max(values.keys())
xmin = min(values.keys())
size = max((xmax - xmin) / 10, .1)

mean = sum(values_)/len(values_)

print("Mean: {}".format(mean))
print("Min: {}".format(xmin))
print("Max: {}".format(xmax))



plt.bar(values.keys(), values.values(), width=size)
plt.xlabel('Time (usec)')
plt.ylabel('Hits (log)')
plt.yscale("log")
plt.grid(True, which='both', axis='both', linewidth=0.2)
plt.xlim([xmin-1, xmax+1])

plt.savefig(sys.argv[1].split('.')[0]+'-plot.png')
