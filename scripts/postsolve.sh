#!/bin/bash
#
# MIPcc24 postsolve script example
#
# postsolve.sh expects five arguments:
# 1) path to original instance in gzipped MPS format (INPUT)
# 2) path to presolved instance in gzipped MPS format (INPUT)
# 3) path to private presolved data (INPUT)
# 4) path to presolved solution in SCIP format (INPUT)
# 5) path to postsolved solution in SCIP format (OUTPUT)

python3 DoNothingPostsolve.py $1 $2 $3 $4 $5
