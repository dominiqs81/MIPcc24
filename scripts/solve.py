# Python script that implements the solution step with SCIP
#
# NOTE: we take as input argument also the presolve log file
#       and we use it to compute the remaining time limit

import os
import sys
from dateutil import parser
import pyscipopt

if len(sys.argv) < 3:
    print("Usage: python3", os.path.basename(__file__),
          "/path/to/presolved.mps.gz /path/to/presolved_solution.sol presolve_logfile")
    exit()

PRESOLVE_TIMELIMIT = 600.0
SOLVE_TIMELIMIT = 3600.0

# Parse arguments
input_file = sys.argv[1]
output_file = sys.argv[2]
presolve_logfile = sys.argv[3]

# Parse presolve log file
with open(presolve_logfile) as f:
    log_lines = f.read().splitlines()

instance_line = list(filter(lambda l: "[INSTANCE]" in l, log_lines))[0]
instance_name = instance_line.split(' ')[-1]
start_line = list(filter(lambda l: "[START]" in l, log_lines))[0]
start_time = parser.parse(start_line.split(' ')[-1])
end_line = list(filter(lambda l: "[END]" in l, log_lines))[0]
end_time = parser.parse(end_line.split(' ')[-1])

# Compute remaining time
scores = {}
time_difference = end_time - start_time
presolve_time = time_difference.total_seconds()
timeout_value = PRESOLVE_TIMELIMIT + 5.0

if presolve_time > timeout_value:
    print(f"### Warning: overtime for instance {instance_name}: {presolve_time} > {timeout_value}")

scores["TotalScore"] = SOLVE_TIMELIMIT
scores["PDI"] = SOLVE_TIMELIMIT
scores["PresolveTime"] = presolve_time

time_limit = SOLVE_TIMELIMIT - presolve_time
print(f"### Solving {instance_name} with time limit = {time_limit}")

# Solve model with SCIP
model = pyscipopt.Model("Presolved Model")
model.setIntParam("display/verblevel", 0)
model.readProblem(input_file)
model.setRealParam("limits/time", time_limit)
model.setRealParam("numerics/feastol", 1e-5)
model.setRealParam("numerics/epsilon", 1e-4)
model.optimize()

# Parse PDI from statistics
stats_file = "stats.txt"
model.writeStatistics(stats_file)
with open(stats_file) as f:
    stats_lines = f.read().splitlines()
os.remove(stats_file)

if model.getStatus() == 'infeasible':
    # No PDI for infeasible models: use time instead
    totaltime_line = list(filter(lambda l: "Total Time" in l, stats_lines))[0]
    scores["PDI"] = float(totaltime_line.split()[3])
else:
    pdi_line = list(filter(lambda l: "primal-dual" in l, stats_lines))[0]
    # SCIP computes the primal-dual integral with a gap in [0,100]
    # and not in [0,1] as we would expect...hence we have to divide by 100!
    scores["PDI"] = float(pdi_line.split()[2]) / 100.0

scores["TotalScore"] = scores["PresolveTime"] + scores["PDI"]

# Print solution
if model.getNSols() > 0:
    scores["Feasible"] = True
    with open(output_file, 'w') as f:
        vars = model.getVars(transformed=False)
        for v in vars:
            solval = model.getVal(v)
            if abs(solval) > 1e-10:
                f.write(v.name + "    " + str(solval) + "\n")
else:
    scores["Feasible"] = False

# Print results
print("Instance:", instance_name)
print("PresolveTime:", scores["PresolveTime"])
print("PDI:", scores["PDI"])
print("Feasible:", scores["Feasible"])
print("TotalScore:", scores["TotalScore"])
