# Python script that implement an empty postsolve step

import os
import sys
from datetime import datetime
import time
import shutil

if len(sys.argv) < 5:
    print("Usage: python3", os.path.basename(__file__),
          "/path/to/instance.mps.gz /path/to/presolved.mps.gz",
          "/path/to/postsolvedata /path/to/presolved_solution.sol",
          "/path/to/postsolved_solution.sol")
    exit()

# Parse arguments
input_file = sys.argv[1]
presolved_input_file = sys.argv[2]
presolve_data_file = sys.argv[3]
presolved_sol_file = sys.argv[4]
postsolve_sol_file = sys.argv[5]

# Time limit for postsolve.
time_limit = 60

# Mandatory log header
print("[INSTANCE]", os.path.basename(input_file))
print("[START]", datetime.now().isoformat())

# Do nothing
time.sleep(1)

# Mandatory log footer
print("[END]", datetime.now().isoformat())

# Create output file
shutil.copyfile(presolved_sol_file, postsolve_sol_file)
