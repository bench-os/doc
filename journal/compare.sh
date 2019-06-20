#!/bin/sh

for i in riot contiki; do
    for j in z1 remote; do
        python3 compare.py reference-value/$i/$j/data.txt devices-framework/$i/$j/data.txt
