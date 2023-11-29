MIPcc24: The MIP Workshop 2024 Computational Competition
========================================================

About
-----

The computational development of optimization tools is a key component within the MIP community and has proven to be a challenging task. It requires great knowledge of the well-established methods, technical implementation abilities, as well as creativity to push the boundaries with novel solutions. In 2022, the annual [Mixed Integer Programming Workshop](https://www.mixedinteger.org/) established a computational competition in order to encourage and provide recognition to the development of novel practical techniques within MIP technology. This year, the competition will focus on MIP presolve.

The Challenge Topic: MIP Presolve
---------------------------------

Presolve is a key component in modern MIP solvers. According to the computational survey [Mixed Integer Programming: Analyzing 12 Years of Progress](https://link.springer.com/chapter/10.1007/978-3-642-38189-8_18), disabling presolve gives the largest overall slowdown in the commercial solver IBM CPLEX 12.5.

At the same time, with the exception of the recent survey [Presolve Reductions in Mixed Integer Programming](https://pubsonline.informs.org/doi/abs/10.1287/ijoc.2018.0857), the literature on presolve reductions is scarse, and there is a wide variability in presolve effectiveness on the same model with different solvers. The purpose of the competition is to fill this gap.

Participants must provide:

* a **presolve code** implementing one (or more) presolve reductions,
* a **postsolve code** able to map a feasible solution of the presolved space back to the original space, and
* a **written report** describing their methodology and results.

Finalists will be provided travel support to present their methods at the [21th anniversary MIP Workshop 2024](https://www.mixedinteger.org/2024/) held in June 2024. High-quality submissions will be invited to an expedited review process in [Mathematical Programming Computation](https://www.springer.com/journal/12532).

Timeline
--------

* July 2023: Publication of topic, rules and competition testset
* **November 30th, 2023**: Registration deadline for participation
* **January 31st, 2024**: Submission deadline for report and code (**Anytime on Earth**)
* March 31st, 2024: Notification of results
* June, 2024: Presentations of the finalists at the MIP Workshop

Awards
------

* The jury will select up to three finalists to present their work at the MIP workshop 2024. The final winner will be announced at the MIP Workshop 2024.
* One representative of each finalist will receive travel support to MIP and free registration.
* The performance of non-finalist submissions will not be published.
* High-quality submissions will receive an expedited review process in [Mathematical Programming Computation](https://www.springer.com/journal/12532).
* The jury may present an award to recognize outstanding student submissions. For these submissions, senior supervisors may be part of the team, but the implementation work must have been fully conducted by students. Students should not have received their first PhD degree on March 1st, 2024.

Organizing committee
--------------------

* [Domenico Salvagnin](https://www.dei.unipd.it/~salvagni/), DEI, University of Padova (Chair)
* [Suresh Bolusani](https://coral.ise.lehigh.edu/bsuresh/), Zuse Institute Berlin
* [Pierre Bonami](https://scholar.google.com/citations?user=JP1tBRAAAAAJ&hl=en), Gurobi
* [Claudia D'Ambrosio](https://www.lix.polytechnique.fr/~dambrosio/), CNRS & Ecole Polytechnique (LIX)
* [Gregor Hendel](https://www.zib.de/hendel/), FICO
* [Joseph Paat](https://sites.google.com/site/josephspaat/), University of British Columbia, Sauder School of Business
* [Krunal Patel](https://www.krooonal.com/about/), Polytechnique Montreal

Rules and Evaluation Procedure
------------------------------

### Rules for Participation

* Participants must not be an organizer of the competition nor a family member of a competition organizer.
* Otherwise, there is no restriction on participation.
* **In particular, student participation is encouraged.**
* Participants can be a single entrant or a team; there is no restriction on the size of teams.
* Should participants be related to organizers of the competition, the rest of the committee will decide whether a conflict of interest is at hand. Affected organizers will not be part of the jury for the final evaluation.

### Technical Rules

* Participants may use any existing software (including closed-source solvers), but cannot use the presolver of an optimization solver in the reduction itself. Solving optimization problems (e.g., LPs and MIPs) is allowed though.
* The source code may be written in any programming language.
* For the final evaluation, participants will need to compile and run their code on a Linux server, accessible via SSH.
* The submissions must run sequentially (1 CPU thread), use no more than 16 GB of RAM, and respect a time limit of 10 minutes (excluding I/O) for each instance in the testset, plus 1 minute for postsolve.

In case participants have any doubts about the implementation of specific rules, they should not hesitate to contact the organizers.

### Submission Requirements

### Registration

* All participants must register with the full list of team members by sending an e-mail [here](mailto:dominiqs@gmail.com) by November 30th, 2023.
* After this deadline, all teams will receive access to a server for testing installation of their software.
* Teams of multiple participants must nominate a single contact person to handle the submission of report and code.

### Report

All participants must submit a written report of **10 pages maximum** plus references, in Springer LNCS format. Submissions will be accepted until **January 31st, 2024 (AoE)**.

The report must include the following information:

* A description of the methods developed and implemented, including any necessary citations to the literature and software used.
* Computational results on the competition testset.
* For each instance in the testset, the results should include at least the following metrics: `presolved size` and `time`.
* Further analysis of the computational results is welcome.

If the computational work was performed by students only, the participants should include a letter of attestation indicating this.

### Code

Each code submission is in two parts: presolve and postsolve.

The presolve part should be executable via a shell script named `presolve.sh` (provided by the participants) which receives arguments on the command line as follows:

1. The first argument is the path in the filesystem to the instance to read, in (gzipped) MPS format.
2. The second argument is the path in the filesystem where the method should write (again in gzipped MPS format) the presolved model.
3. The third argument is the path in the filesystem where the method should write (in arbitrary format) the necessary information for postsolve.

The presolve step will thus be executed as

`sh presolve.sh /path/to/instance.mps.gz /path/to/presolved.mps.gz /path/to/postsolvedata`

with a hard time limit of 20 minutes. Files are specified as absolute paths.

The log output must contain at least the following information in this order:

```
[INSTANCE] instance_name.mps.gz
[START] 2023-10-26T15:25:10.852
[END] 2023-10-26T15:26:17.171
```

* The `[START]` and `[END]` times must be given in the same format as that of the `date -Iseconds` command.
* `[INSTANCE]` must be the file name of the current instance being solved (without the complete path).

The user is allowed (and encouraged) to start the clock after reading the instance to presolve and stopping it before writing the presolved model to file, so that I/O does not play a role in the timing. Note that while the hard time limit on the process is 20 minutes, the actual time limit for the presolve reduction itself (i.e., `[END] - [START]`) is 10 minutes.

The postsolve part should also be executable via a shell script, named `postsolve.sh` and again provided by the participants, which receives arguments on the command line as follows:

1. The first argument is the path in the filesystem to the original instance, in (gzipped) MPS format.
2. The second argument is the path in the filesystem to the presolved instance, in (gzipped) MPS format.
3. The third argument is the path in the filesystem to the private postsolve data.
4. The fourth argument is the path in the filesystem to the solution file computed by SCIP on the presolved instance (more details below on the format).
5. The fifth argument is the path in the filesystem where to write the postsolved solution (in the same format as the previous argument).

The postsolve step will thus be executed as

`sh postsolve.sh /path/to/instance.mps.gz /path/to/presolved.mps.gz /path/to/postsolvedata /path/to/presolved_solution.sol /path/to/postsolved_solution.sol`

with a hard time limit of 5 minutes. Files are specified as absolute paths.

Again, the log output must contain at least the following information in this order:

```
[INSTANCE] instance_name.mps.gz
[START] 2023-10-26T15:25:10.852
[END] 2023-10-26T15:26:17.171
```

* The `[START]` and `[END]` times must be given in the same format as that of the `date -Iseconds` command.
* `[INSTANCE]` must be the file name of the current instance being solved (without the complete path).

The user is allowed (and encouraged) to start the clock after reading the files and stopping it before writing the the output, so that I/O does not play a role in the timing. Note that while the hard time limit on the process is 5 minutes, the actual time limit for the postsolve itself (i.e., `[END] - [START]`) is 1 minute.

As for the solution file format, it will be the one already used by the MIPLIB solution checker:

* Each line contains a variable name and the associated value as `<variable name> white space <variable value>`.
* Additional lines can be added as comments starting with `#`.
* If any variable is absent from the solution file, its value will be interpreted as 0.0.

### Final Evaluation Criteria

The evaluation will be performed by an expert jury of researchers with experience in computational optimization. They will judge both paper and code submission on two criteria:

1. **Novelty and scope**: How innovative is the approach and how generally applicable?
2. **Computational excellence**: How does the approach rank in terms of the performance score defined below.

The spirit of this competition is to encourage the development of new methods that work in practice. The jury will be free to disqualify submissions that provide no contribution beyond repurposing existing software.

### Performance Scoring

For a given method, each instance in the competition testset will be processed as follows:

1. The presolve step (`presolve.sh`) is executed. Let's say the presolve reduction takes, excluding I/O, T seconds.
2. SCIP is run with default settings on the presolved model obtained in step 1, with a time limit of 3600-T seconds.
3. If the instance is not infeasible and SCIP computes a feasible primal solution, postsolve (`postsolve.sh`) will be executed on it to get a feasible solution in the original space.

After the code has run, a verification step will be performed, checking that:

* the postsolved primal solution (if any) is feasible w.r.t. the original model. A primal solution will be considered feasible if the absolute violation of every constraint is at most 10^{−5} and if all integer variables are at most 10^{−4} away from the nearest integer value.
* the primal and dual bounds computed by SCIP on the presolved instance are compatible with the best known bounds on the instance. Note that this implies that, in the reduction, scaling the objective or arbitrarily changing the objective offset is not allowed.

If the verification checks succeed, the final score of a method on a given instance will be given by T plus the PDI measure reported by SCIP in step 2. In case of invalid bounds/solution, the score will be set to 3600.

Finally, scores will be averaged over all the instances in the testset via the shifted geometric mean, with a shift of 10 (the lower the better).

As for testsets, all submissions will be initially run on the MIPLIB 2017 instances listed in the file `first_round.test`. Then, potential winners will be run on the full MIPLIB 2017 benchmark set.

## FAQ

Q: Can I implement my reduction on top of [Papilo](https://github.com/scipopt/papilo/)?

In general, implementing the reduction on top of a presolving framework (closed or open-source) is forbidden by the competition rules, for the following reasons:
1. it would make it difficult to evaluate whether the improvement comes from just running presolve twice (once in the reduction, and once by SCIP itself in the final run) or with different parameters, or from the new reduction itself;
2. it would bias the competition towards participants that are already familiar with a presolving framework.

However, we understand that using a framework could provide some convenience features and speed up development.
So, after some discussion with the Papilo maintainers, we agreed that participants are allowed to use Papilo provided that:
1. all other reductions are disabled;
2. parallel execution is disabled.

You can use the dedicated branch [Papilo/MIPCOMP24](https://github.com/scipopt/papilo/tree/MIPCOMP24) or, if you prefer to do those changes manually:
* Disable all presolvers by starting with an empty function `addDefaultPresolvers()` in `Presolve.hpp`
* Use only the sequential mode of PaPILO by using the parameter setting: `presolve.threads = 1`
* Disable linearly dependent equations by parameter setting: `presolve.detectlindep = 0`

