# [Towards Robust Evaluations of Continual Learning](https://arxiv.org/abs/1805.09733)

## Sebastian Farquhar, Yarin Gal

### Introduction / Contributions

* propose fundamental desiderata for future evaluations, which can be applied regardless of dataset
* analyse the shortcomings of existing widely used evaluations in continual learning
* show empirically that existing evaluations are biased towards prior-focused approaches
* propose new experimental designs which mitigate the issues of existing ones.

### Proposed Desiderata for Continual Learning Evaluations

* A: cross-task resemblances
* B: Shared output head
* C: No test-time assumed task labels
* D: No unconstrained retraining on old tasks
* E: More than two tasks

Other desiderata:

* Unclear task demarcation
* Continuous tasks
* Overlapping task
* Long task sequences
* Time/compute/memory constraints
* Strict privacy guarantees

### Critical Analysis of Existing Evaluations

* don't use permuted MNIST (decause desideratum A)

### Empirical Analysis of Existing Evaluations


* whenever you remove a desideratum (A, B, C, D, E) introduces blindspots in the eval protocol
* Variational Generative Replay (VGR)'s uncertainty spikes when the task switchs (so it can be used for task boundary detection)
* There is a trade-off between time/compute and accuracy


### Some Notes

* seems like it will be hard for prior-focused methods to be a standalone CL strategy
* How could we evaluate time/compute/memory without overloading the evaluation protocol? (AUC maybe)
* How about hyper-parameter search time? should that be taken into consideration?



