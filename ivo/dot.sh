#! /bin/bash

for f in "dump/*.dot"; do
    dot -Tpng -O $f
done
