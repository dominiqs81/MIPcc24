#!/bin/bash
#
# MIPcc24 presolve script example
#
# presolve.sh expects three arguments:
# 1) path to original instance in gzipped MPS format (INPUT)
# 2) path to presolved instance in gzipped MPS format (OUTPUT)
# 3) path to private presolved data (OUTPUT)

python3 DoNothingPresolve.py $1 $2 $3
