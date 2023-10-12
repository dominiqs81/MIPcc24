# Python script that implements the final evaluation
#
# NOTE: We check the postsolved solution (if any) for feasibility
#       and the postsolve log for postsolve time.

import os
import sys
from dateutil import parser
import pyscipopt

if len(sys.argv) < 3:
    print("Usage: python3", os.path.basename(__file__),
          "/path/to/instance.mps.gz /path/to/solution.sol postsolve_logfile")
    exit()

POSTSOLVE_TIMELIMIT = 60.0

# Parse arguments
input_file = sys.argv[1]
solution_file = sys.argv[2]
postsolve_logfile = sys.argv[3]

instance_name = os.path.basename(input_file)

# Parse postsolve log file
with open(postsolve_logfile) as f:
    log_lines = f.read().splitlines()

start_line = list(filter(lambda l: "[START]" in l, log_lines))[0]
start_time = parser.parse(start_line.split(' ')[-1])
end_line = list(filter(lambda l: "[END]" in l, log_lines))[0]
end_time = parser.parse(end_line.split(' ')[-1])

scores = {}
time_difference = end_time - start_time
postsolve_time = time_difference.total_seconds()
timeout_value = POSTSOLVE_TIMELIMIT + 5.0
if postsolve_time > timeout_value:
    print(f"Warning: overtime for instance {instance_name}: {postsolve_time} > {timeout_value}")

scores["PostsolveTime"] = postsolve_time
scores["PostsolveValid"] = True

# Verify solution with SCIP
model = pyscipopt.Model("Verify Solution")
model.setIntParam("display/verblevel", 0)
model.readProblem(input_file)
sol = model.readSolFile(solution_file)
model.setRealParam("numerics/feastol", 1e-5)
model.setRealParam("numerics/epsilon", 1e-4)

if not model.checkSol(sol):
    print(f"Warning: produced solution for {instance_name} is infeasible")
    scores["PostsolveValid"] = False

# Print results
print("Instance:", instance_name)
print("PostsolveTime:", scores["PostsolveTime"])
print("PostsolveValid:", scores["PostsolveValid"])
