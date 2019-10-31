# Continual Learning Reading Group

## Schedule

Monday 1:30PM, Room H06 (6650 St-Urbain)

## Categories

* [Classics](#classics) (papers before Deep Learning era. Motivates and sets the stage for Continual Learning)
* [Influencials](#influencials) (well cited papers. More general contributions like proposing new frameworks, evaluations, etc)
* [Surveys](#surveys)
* [Prior-Focused Methods](#prior-focused-methods)
* [Dynamic Architectures Methods](#dynamic-architectures-methods)
* [Rehearsal Methods](#rehearsal-methods)
* [Hybrid Methods](#hybrid-methods)
* [Meta Continual Learning](#meta-continual-learning) (learning to continually learn)
* [Continual Meta Learning](#continual-meta-learning) (continually learning to learn)
* [Lifelong Reinforcement Learning](#lifelong-reinforcement-learning)
* [Relevants](#relevants) (non-continual learning papers that can help us e.g. Generalization, Biology, Meta-Learning, etc)
* [Unclassified](#unclassified) (yet!)

#### Abreviations

Continual Learning (CL), Catastrophic Forgetting (CF), Generative Replay (GR), Continual Meta Learning (CML)


## Papers

### Classics


[Lifelong robot learning](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.71.3723&rep=rep1&type=pdf) (1995)
``` 
argues knowledge transfer is essential if robots are to learn control with moderate learning times
```

### Influencials


[An Empirical Investigation of Catastrophic Forgetting in Gradient-Based Neural Networks](https://arxiv.org/abs/1312.6211) (2013) 
```
Investigates CF in neural networks
```

[Elastic Weight Consolidation (EWC)](https://www.pnas.org/content/pnas/114/13/3521.full.pdf) (2017)
```
Introduces prior-focused methods
```

[Gradient Episodic Memory (GEM)](https://arxiv.org/abs/1706.08840) (2017) 
```
a model that alliviates CF via constrained optimization
```

[Efficient Lifelong Learning with A-GEM](https://arxiv.org/abs/1812.00420) (2018) 
```
More efficient GEM; Introduces online continual learning
```

[Continual Learning with Deep Generative Replay (GR)](https://arxiv.org/abs/1705.08690) (2017)
```
Introduces generative replay
```

[Towards Robust Evaluations of Continual Learning](https://arxiv.org/abs/1805.09733) (2018) [[summary]](https://github.com/optimass/continual_learning_papers/blob/master/summaries/Towards_Robust_Evaluation_of_Continual_Learning.md)
```
Proposes desideratas and reexamines the evaluation protocol
```


### Surveys


[Continual Lifelong Learning with Neural Networks: A Review](https://arxiv.org/abs/1802.07569)  (2018) 
```
A extensive review of CL
```


### Prior-focused Methods


[Elastic Weight Consolidation (EWC)](https://www.pnas.org/content/pnas/114/13/3521.full.pdf) (2017) 
```
 Introduces prior-focused methods
```

[Synaptic Intelligence (SI)](https://arxiv.org/abs/1703.04200) (2017)
```
Importance of parameter measured based on their contribution to change in the loss. 
```

[Riemannian Walk for Incremental Learning: Understanding Forgetting and Intransigence](https://arxiv.org/abs/1801.10112) (2018)
```
Formalizes the shortcomings of multi-head evaluation, as well as the importance of replay in single-head setup. Presenting an improved version of EWC. 
```

[Memory Aware Synapses: Learning what (not) to forget](https://arxiv.org/pdf/1711.09601.pdf) (2018)
```
Importance of parameter measured based on their contribution to change in the learned prediction function.
```

[Learning without Forgetting](https://arxiv.org/abs/1606.09282) (2016)
```
Functional regularization through distillation (keeping the output of the updated network on the new data close to the output of the old network on the new data)
```

[Overcoming catastrophic forgetting with hard attention to the task (HAT)](https://arxiv.org/abs/1801.01423) (2018)
```
Introducing a "hard attention" idea with binary masks |
```

[Piggyback: Adapting a Single Network to Multiple Tasks by Learning to Mask Weights](https://arxiv.org/abs/1801.06519) (2018)
```
Hard masking of a fixed pretrained network. |
```

[Variational Continual Learning (VCL)](https://arxiv.org/abs/1710.10628) (2017)
```
Introduces the idea of using previous task's posterior as the new task's prior in a BNN.
```

[Improving and Understanding Variational Continual Learning](https://arxiv.org/abs/1905.02099) (2019)
```
Improved results and interpretation of VCL.
```

[Uncertainty-guided Continual Learning with Bayesian Neural Networks](https://arxiv.org/abs/1906.02425) (2019) 
```
Uses Bayes by Backprop for variational Continual Learning.
```

[Uncertainty-based Continual Learning with Adaptive Regularization](https://arxiv.org/pdf/1905.11614.pdf) (2019) 
```
Introduces VCL with uncertainty measured for neurons instead of weights.
```

[Task Agnostic Continual Learning Using Online Variational Bayes](https://arxiv.org/pdf/1803.10123.pdf) (2019)
```
Introduces an optimizer for CL that relies on closed form updates of mu and sigma of BNN; introduce label trick for "class learning" (single-head)
```


### Dynamic Architectures Methods

[Progressive neural networks](https://arxiv.org/abs/1606.04671) (2016)

[Incremental Learning Through Deep Adaptation](https://arxiv.org/pdf/1705.04228.pdf) (2018)

[Continual Learning Using Bayesian Neural Networks](https://arxiv.org/abs/1910.04112) (2019)
```
Learns a separate set of posterior distributions for each weight for each task (for a BNN), which are merged using EM updates from time to time (thus posteriors are GMMs)
```


### Rehearsal Methods

[Gradient Episodic Memory (GEM)](https://arxiv.org/abs/1706.08840) (2017) 
```
a model that alliviates CF via constrained optimization (doesn't increase loss on previous stored data)
```

[Efficient Lifelong Learning with A-GEM](https://arxiv.org/abs/1812.00420) (2018)
```
More efficient GEM; Introduces online continual learning
```

[Continual Learning with Deep Generative Replay (GR)](https://arxiv.org/abs/1705.08690) (2017)
```
 Introduces generative replay
```

[Generative replay with feedback connections as a general strategy for continual learning](https://arxiv.org/abs/1809.10635) (2018)
```
smarter GR
```

[Generative Models from the perspective of Continual Learning](https://arxiv.org/abs/1812.09111) (2018)
```
Extensive evaluation of CL methods for generative modeling
```

[Gradient based sample selection for online continual learning](https://arxiv.org/abs/1903.08671) (2019)
```
sample selection as a constraint reduction problem based on the constrained optimization view of continual learning
```

[Online Continual Learning with Maximaly Interfered Retrieval](https://arxiv.org/abs/1903.08671) (2019)
```
Controlled sampling of memories for replay: retrieving the samples which are most interfered
```


### Hybrid Methods


### Meta Continual Learning

[Meta-Learning Representations for Continual Learning (MRCL)](https://arxiv.org/abs/1905.12588) (2019)
```
Learns how to continually learn i.e. learns how to do online updates without forgetting.
```

### Continual Meta Learning

[Task Agnostic Continual Learning via Meta Learning](https://arxiv.org/abs/1906.05201) (2019)
```
Introduces What and How framework; enables Task Agnostic CL with meta learned task inference
```

[Reconciling meta-learning and continual learning with online mixtures of tasks](https://arxiv.org/abs/1812.06080) (2019)
```
Meta-learns a tasks structure; continual adaptation via non-parametric prior
```


### Lifelong Reinforcement Learning


### Relevants 

### Unclassified



## Paper Classification

family = {prior, rehearsal, dynamic, meta, hybrid}


Title                                                                                                                               | Family     | Single-Head        | Task Agnostic      | Online             | Supervised         | Generative         | RL
---                                                                                                                                 | ---        | ---                | ---                | ---                | ---                | ---                | ---
[Elastic Weight Consolidation (EWC)](https://www.pnas.org/content/pnas/114/13/3521.full.pdf)                                        | Prior      |                    |                    |                    | :heavy_check_mark: |                    | :heavy_check_mark:
[Continual Learning with Deep Generative Replay (GR)](https://arxiv.org/abs/1705.08690)                                             | Rehearsal  |                    |                    |                    | :heavy_check_mark: | :heavy_check_mark: |
[Gradient based sample selection for online continual learning](https://arxiv.org/abs/1903.08671)                                   | Rehearsal  | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |                    |
[Generative replay with feedback connections as a general strategy for continual learning](https://arxiv.org/abs/1809.10635)        | Rehearsal  | :heavy_check_mark: |                    |                    | :heavy_check_mark: | :heavy_check_mark: |
[Task Agnostic Continual Learning via Meta Learning](https://arxiv.org/abs/1906.05201)                                              | Meta       | :heavy_check_mark: | :heavy_check_mark: |                    | :heavy_check_mark: |                    |
[Reconciling meta-learning and continual learning with online mixtures of tasks](https://arxiv.org/abs/1812.06080)                  | Meta       | :heavy_check_mark: | :heavy_check_mark: |                    | :heavy_check_mark: |                    |
[Task Agnostic Continual Learning Using Online Variational Bayes](https://arxiv.org/pdf/1803.10123.pdf)                             | Meta       | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |                    |
[Meta-Learning Representations for Continual Learning (MRCL)](https://arxiv.org/abs/1905.12588)                                     | Meta       | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |                    |
