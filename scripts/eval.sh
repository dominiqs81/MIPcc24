#!/usr/bin/env bash

# Script to evaluate a MIPcc24 competition presolve reduction
# on a set of models
#
# Usage:
#
# sh eval.sh list_of_models.test /path/to/data/dir /path/to/output_dir

benchmark_instances=$1
data_dir=$2
output_dir=$3

# Make sure output directory exists
mkdir -p $output_dir

# Presolve loop
while read instance
do
    echo "Presolving $instance"
    input_file="$data_dir/$instance.mps.gz"
    presolved_path="$output_dir/presolved_$instance.mps.gz"
    presolver_data_path="$output_dir/data_$instance"
    presolve_logfile="$output_dir/$instance.presolve.log"
    sh presolve.sh $input_file $presolved_path $presolver_data_path > $presolve_logfile
done < $benchmark_instances


# Solve loop
while read instance
do
    echo "Solving $instance"
    input_file="$data_dir/$instance.mps.gz"
    presolved_path="$output_dir/presolved_$instance.mps.gz"
    presolved_sol_path="$output_dir/presolved_$instance.sol"
    presolver_data_path="$output_dir/data_$instance"
    presolve_logfile="$output_dir/$instance.presolve.log"
    solve_logfile="$output_dir/$instance.solve.log"
    python3 solve.py $presolved_path $presolved_sol_path $presolve_logfile > $solve_logfile
done < $benchmark_instances


# Postsolve loop
while read instance
do
    input_file="$data_dir/$instance.mps.gz"
    presolved_path="$output_dir/presolved_$instance.mps.gz"
    presolved_sol_path="$output_dir/presolved_$instance.sol"
    postsolved_sol_path="$output_dir/$instance.sol"
    presolver_data_path="$output_dir/data_$instance"
    solve_logfile="$output_dir/$instance.solve.log"
    postsolve_logfile="$output_dir/$instance.postsolve.log"
    feasible=$(grep "Feasible" $solve_logfile | cut -d ' '  -f2)
    if [[ $feasible == "True" ]]
    then
        echo "Postsolving $instance"
        sh postsolve.sh $input_file $presolved_path $presolver_data_path $presolved_sol_path $postsolved_sol_path > $postsolve_logfile
        python3 eval.py $input_file $postsolved_sol_path $postsolve_logfile >> $solve_logfile
    fi
done < $benchmark_instances
