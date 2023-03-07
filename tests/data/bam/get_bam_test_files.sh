#!/bin/bash

# https://aldy.readthedocs.io/en/latest/readme.html#sample-datasets

curl http://cb.csail.mit.edu/cb/aldy/data/NA10856.bam --output ./tests/data/bam/NA10856.bam
samtools index ./tests/data/bam/NA10856.bam