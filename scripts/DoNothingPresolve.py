# Python script that implement an empty presolve reduction

import os
import sys
from datetime import datetime
import time
import shutil

if len(sys.argv) < 3:
    print("Usage: python3", os.path.basename(__file__),
          "/path/to/instance.mps.gz /path/to/presolved.mps.gz",
          "/path/to/postsolvedata")
    exit()

# Parse arguments
input_file = sys.argv[1]
output_file = sys.argv[2]
presolve_data_file = sys.argv[3]

# Mandatory log header
print("[INSTANCE]", os.path.basename(input_file))
print("[START]", datetime.now().isoformat())

# Do nothing
time.sleep(1)

# Mandatory log footer
print("[END]", datetime.now().isoformat())

# Create output file
# (we do not create a postsolve data file as the reduction does not need it)
shutil.copyfile(input_file, output_file)
