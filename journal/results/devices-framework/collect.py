"""
This script retrieves the context switching time between two tasks.
"""
import matplotlib.pyplot as plt
import sys
from PSL import sciencelab

I = sciencelab.connect()

values = {}
values_ = []

error_rate = 0.00

samples_size = 1000 * (1 + error_rate*2)

while len(values_) < samples_size:
    interval_time = I.MeasureInterval('ID1', 'ID1', 'falling', 'rising')

    if interval_time > 0:
        v = interval_time*10**6
        values_.append(v)

for _ in range(int(len(values_) * error_rate)):
    values_.remove(max(values_))
    values_.remove(min(values_))

for v in values_:
    print(v)
