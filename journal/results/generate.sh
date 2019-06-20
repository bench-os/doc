#!/bin/sh

for i in riot contiki; do
    for j in remote z1; do
        python3 compare.py reference-value/$i/$j/data.txt extension-framework/$i/$j/data.txt devices-framework/$i/$j/data.txt comparisons/comparison-all-$i-$j.pdf
        for x in extension-framework devices-framework; do
            python3 compare.py reference-value/$i/$j/data.txt $x/$i/$j/data.txt comparisons/comparison-$x-$i-$j.pdf
        done
    done
done

for x in extension-framework reference-value devices-framework; do
    for i in riot contiki; do
        for j in remote z1; do
            python3 data.py $x/$i/$j/data.txt comparisons/$x-$i-$j.pdf
        done
    done
done

for j in remote z1; do
    python3 offset.py reference-value/contiki/$j/data.txt reference-value/riot/$j/data.txt comparisons/offset-$j.pdf
done

cp comparisons/*.pdf ~/codes/bench-os/thesis/assets/.
