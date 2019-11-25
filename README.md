# Continual Learning Literature

email me at massimo.p.caccia at gmail.com is you would like to collaborate

### [Papers](#papers)

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
* [Continual Generative Modeling](#continual-generative-modeling)
* [Relevants](#relevants) (non-continual learning papers that can help us e.g. Generalization, Biology, Meta-Learning, etc)
* [Unclassified](#unclassified) (yet!)


### [Papers classified in more details](#paper-classification)

{Family, Single-Head, Task Agnostic, Online, Supervised Learning, Generative Modeling, Reinforcement Learning}

### [Continual Learning codebases](#Continual-Learning-codebases)

list of interesting codebases for continual learning

#### Abreviations

Continual Learning (CL), Catastrophic Forgetting (CF), Generative Replay (GR), Continual Meta Learning (CML), Meta Continual Learning (MCL)


## Papers

### Classics

[Catastrophic interference in connectionist networks: The sequential learning problem](https://www.sciencedirect.com/science/article/pii/S0079742108605368) (1989) [[bib]](https://github.com/optimass/continual_learning_papers/blob/master/bibtex.bib#L398-L402)
```
Introduces CL and reveals the catastrophic forgetting problem
```

[Lifelong robot learning](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.71.3723&rep=rep1&type=pdf) (1995) [[bib]](https://github.com/optimass/continual_learning_papers/blob/master/bibtex.bib#L1-L8)
``` 
argues knowledge transfer is essential if robots are to learn control with moderate learning times
```


### Influencials

[Towards Robust Evaluations of Continual Learning](https://arxiv.org/abs/1805.09733) (2018) [[bib]](https://github.com/optimass/continual_learning_papers/blob/master/bibtex.bib#L10-L15) [[summary]](https://github.com/optimass/continual_learning_papers/blob/master/summaries/Towards_Robust_Evaluation_of_Continual_Learning.md) 
```
Proposes desideratas and reexamines the evaluation protocol
```

[Efficient Lifelong Learning with A-GEM](https://arxiv.org/abs/1812.00420) (2018) [[bib]](https://github.com/optimass/continual_learning_papers/blob/master/bibtex.bib#L17-L21)
```
More efficient GEM; Introduces online continual learning
```

[Elastic Weight Consolidation (EWC)](https://www.pnas.org/content/pnas/114/13/3521.full.pdf) (2017) [[bib]](https://github.com/optimass/continual_learning_papers/blob/master/bibtex.bib#L24-L30)
```
Introduces prior-focused methods
```

[Gradient Episodic Memory (GEM)](https://arxiv.org/abs/1706.08840) (2017) [[bib]](https://github.com/optimass/continual_learning_papers/blob/master/bibtex.bib#L32-L41)
```
a model that alliviates CF via constrained optimization
```


[Continual Learning with Deep Generative Replay (GR)](https://arxiv.org/abs/1705.08690) (2017) [[bib]](https://github.com/optimass/continual_learning_papers/blob/master/bibtex.bib#L43-L49)
```
Introduces generative replay
```

[An Empirical Investigation of Catastrophic Forgetting in Gradient-Based Neural Networks](https://arxiv.org/abs/1312.6211) (2013) [[bib]](https://github.com/optimass/continual_learning_papers/blob/master/bibtex.bib#L51-L64)
```
Investigates CF in neural networks
```

### Surveys

[Continual learning: A comparative study on how to defy forgetting in classification tasks](https://arxiv.org/abs/1909.08383) (2019) [[bib]](https://github.com/optimass/continual_learning_papers/blob/master/bibtex.bib#L66-L73)
```
Extensive empirical study of CL methods (in the multi-head setting)
```

[Continual Learning for Robotics](https://arxiv.org/abs/1907.00182) (2019) [[bib]](https://github.com/optimass/continual_learning_papers/blob/master/bibtex.bib#L75-L82)
```
Extensive review of CL methods and their applications in robotics and framework proposition for continual learning
```

[Continual Lifelong Learning with Neural Networks: A Review](https://arxiv.org/abs/1802.07569)  (2018) [[bib]](https://github.com/optimass/continual_learning_papers/blob/master/bibtex.bib#L84-L95)
```
A extensive review of CL
```

[Lifelong Machine Learning](https://www.cs.uic.edu/~liub/lifelong-machine-learning-draft.pdf) (2016)
```
Book on Continual Learning. Extensive review of older and newer algorithm; motivations and relation to other ML paradigms
```


### Prior-focused Methods

#### 2019

[Improving and Understanding Variational Continual Learning](https://arxiv.org/abs/1905.02099) (2019) [[bib]](https://github.com/optimass/continual_learning_papers/blob/master/bibtex.bib#L97-L103)
```
Improved results and interpretation of VCL.
```

[Uncertainty-guided Continual Learning with Bayesian Neural Networks](https://arxiv.org/abs/1906.02425) (2019) [[bib]](https://github.com/optimass/continual_learning_papers/blob/master/bibtex.bib#L105-L111)
```
Uses Bayes by Backprop for variational Continual Learning.
```

[Uncertainty-based Continual Learning with Adaptive Regularization](https://arxiv.org/pdf/1905.11614.pdf) (2019) [[bib]](https://github.com/optimass/continual_learning_papers/blob/master/bibtex.bib#L113-L122)
```
Introduces VCL with uncertainty measured for neurons instead of weights.
```

[Task Agnostic Continual Learning Using Online Variational Bayes](https://arxiv.org/pdf/1803.10123.pdf) (2018) [[bib]](https://github.com/optimass/continual_learning_papers/blob/master/bibtex.bib#L124-L131)
```
Introduces an optimizer for CL that relies on closed form updates of mu and sigma of BNN; introduce label trick for "class learning" (single-head)
```

#### 2018


[Overcoming Catastrophic Interference using Conceptor-Aided Backpropagation (CAB)](https://openreview.net/pdf?id=B1al7jg0b) (2018) [[bib]](https://github.com/optimass/continual_learning_papers/blob/master/bibtex.bib#L133-L139)
```
"Conceptor-Aided Backprop" (CAB): gradients are shielded by conceptors against degradation of previously learned tasks
```

[Overcoming catastrophic forgetting with hard attention to the task (HAT)](https://arxiv.org/abs/1801.01423) (2018) [[bib]](https://github.com/optimass/continual_learning_papers/blob/master/bibtex.bib#L141-L156)
```
Introducing a "hard attention" idea with binary masks 
```

[Riemannian Walk for Incremental Learning: Understanding Forgetting and Intransigence](https://arxiv.org/abs/1801.10112) (2018) [[bib]](https://github.com/optimass/continual_learning_papers/blob/master/bibtex.bib#L158-L163)
```
Formalizes the shortcomings of multi-head evaluation, as well as the importance of replay in single-head setup. Presenting an improved version of EWC. 
```

#### 2017

[Elastic Weight Consolidation (EWC)](https://www.pnas.org/content/pnas/114/13/3521.full.pdf) (2017) [[bib]](https://github.com/optimass/continual_learning_papers/blob/master/bibtex.bib#L24-L30)
```
 Introduces prior-focused methods
```

[Memory Aware Synapses: Learning what (not) to forget](https://arxiv.org/pdf/1711.09601.pdf) (2017) [[bib]](https://github.com/optimass/continual_learning_papers/blob/master/bibtex.bib#L165-L181)
```
Importance of parameter measured based on their contribution to change in the learned prediction function.
```

[Variational Continual Learning (VCL)](https://arxiv.org/abs/1710.10628) (2017) [[bib]](https://github.com/optimass/continual_learning_papers/blob/master/bibtex.bib#L183-L189)
```
Introduces the idea of using previous task's posterior as the new task's prior in a BNN.
```

[Synaptic Intelligence (SI)](https://arxiv.org/abs/1703.04200) (2017) [[bib]](https://github.com/optimass/continual_learning_papers/blob/master/bibtex.bib#L191-L205)
```
Importance of parameter measured based on their contribution to change in the loss. 
```

#### 2016

[Learning without Forgetting](https://arxiv.org/abs/1606.09282) (2016) [[bib]](https://github.com/optimass/continual_learning_papers/blob/master/bibtex.bib#L207-L2013)
```
Functional regularization through distillation (keeping the output of the updated network on the new data close to the output of the old network on the new data)
```

### Dynamic Architectures Methods

[Continual Learning Using Bayesian Neural Networks](https://arxiv.org/abs/1910.04112) (2019) [[bib]](https://github.com/optimass/continual_learning_papers/blob/master/bibtex.bib#L215-L222)
```
Learns a separate set of posterior distributions for each weight for each task (for a BNN), which are merged using EM updates from time to time (thus posteriors are GMMs)
```

[Incremental Learning Through Deep Adaptation](https://arxiv.org/pdf/1705.04228.pdf) (2018) [[bib]](https://github.com/optimass/continual_learning_papers/blob/master/bibtex.bib#L224-L230)
```
 
```

[Progressive neural networks](https://arxiv.org/abs/1606.04671) (2016) [[bib]](https://github.com/optimass/continual_learning_papers/blob/master/bibtex.bib#L232-L246)
```
Each task have a specific model connected to the previous ones
```

### Rehearsal Methods

#### 2019

[Online Learned Continual Compression with Stacked Quantization Module](https://arxiv.org/abs/1911.08019) (2019) [[code]](https://github.com/pclucas14/stacked-quantized-modules)
```
Uses stacks of VQ-VAE modules to progressively compress the data stream, enabling better rehearsal
```

[Orthogonal Gradient Descent for Continual Learning](https://arxiv.org/abs/1910.07104) (2019) [[bib]](https://github.com/optimass/continual_learning_papers/blob/master/bibtex.bib#L248-L255)
```
projecting the gradients from new tasks onto a subspace in which the neural network output on previous task does not change and the projected gradient is still in a useful direction for learning the new task
``` 

[Gradient based sample selection for online continual learning](https://arxiv.org/abs/1903.08671) (2019) [[bib]](https://github.com/optimass/continual_learning_papers/blob/master/bibtex.bib#L257-L266)
```
sample selection as a constraint reduction problem based on the constrained optimization view of continual learning
```

[Online Continual Learning with Maximaly Interfered Retrieval (MIR)](https://arxiv.org/abs/1903.08671) (2019) [[bib]](https://github.com/optimass/continual_learning_papers/blob/master/bibtex.bib#L268-L277) [[summary]](https://www.shortscience.org/paper?bibtexKey=journals/corr/1908.04742)
```
Controlled sampling of memories for replay to automatically rehearse on tasks currently undergoing the most forgetting
```

#### 2018

[Efficient Lifelong Learning with A-GEM](https://arxiv.org/abs/1812.00420) (2018) [[bib]](https://github.com/optimass/continual_learning_papers/blob/master/bibtex.bib#L17-L22)
```
More efficient GEM; Introduces online continual learning
```

[Generative replay with feedback connections as a general strategy for continual learning](https://arxiv.org/abs/1809.10635) (2018) [[bib]](https://github.com/optimass/continual_learning_papers/blob/master/bibtex.bib#L279-L285)
```
smarter GR
```

#### 2017

[Gradient Episodic Memory (GEM)](https://arxiv.org/abs/1706.08840) (2017)  [[bib]](https://github.com/optimass/continual_learning_papers/blob/master/bibtex.bib#L32-L41)
```
a model that alliviates CF via constrained optimization (doesn't increase loss on previous stored data)
```

[Continual Learning with Deep Generative Replay (GR)](https://arxiv.org/abs/1705.08690) (2017) [[bib]](https://github.com/optimass/continual_learning_papers/blob/master/bibtex.bib#L43-L49)
```
 Introduces generative replay
```


### Hybrid Methods

[Continual learning with hypernetworks](https://openreview.net/pdf?id=SJgwNerKvB) (2019) [[bib]] (https://github.com/optimass/continual_learning_papers/blob/master/bibtex.bib#L388-L396) 
```
Learning task-conditioned hypernetworks for continual learning as well as task embeddings; hypernetwors offers good model compression.
```


### Meta Continual Learning

[Meta-Learning Representations for Continual Learning (MRCL)](https://arxiv.org/abs/1905.12588) (2019) [[bib]](https://github.com/optimass/continual_learning_papers/blob/master/bibtex.bib#L287-L296)
```
Learns how to continually learn i.e. learns how to do online updates without forgetting.
```

[Learning to Learn without Forgetting by Maximizing Transfer and Minimizing Interference (MER)](https://arxiv.org/abs/1810.11910) (2018) [[bib]](https://github.com/optimass/continual_learning_papers/blob/master/bibtex.bib#L268-L277)
```
Learns how to update the model such that weight sharing maximises transfer and minimizes interference, via REPTILE
```

### Continual Meta Learning

[Learning from the Past: Continual Meta-Learning with Bayesian Graph Neural Networks](https://arxiv.org/pdf/1911.04695.pdf) (2019) [[bib]](https://github.com/optimass/continual_learning_papers/blob/master/bibtex.bib#L298-L305)
```

```

[Task Agnostic Continual Learning via Meta Learning](https://arxiv.org/abs/1906.05201) (2019) [[bib]](https://github.com/optimass/continual_learning_papers/blob/master/bibtex.bib#L124-L131)
```
Introduces What and How framework; enables Task Agnostic CL with meta learned task inference
```

[Online Meta-Learning](https://arxiv.org/abs/1902.08438) (2019) [[bib]](https://github.com/optimass/continual_learning_papers/blob/master/bibtex.bib#L307-L321) [[summary]](https://github.com/optimass/continual_learning_papers/blob/master/summaries/Online_Meta-learning.md)
```
defines Online Meta-learning; propsoses Follow the Meta Leader (FTML) (~ Online MAML) 
```

[Reconciling meta-learning and continual learning with online mixtures of tasks](https://arxiv.org/abs/1812.06080) (2018) [[bib]](https://github.com/optimass/continual_learning_papers/blob/master/bibtex.bib#L323-L332)
```
Meta-learns a tasks structure; continual adaptation via non-parametric prior
```


[Deep Online Learning via Meta-Learning: Continual Adaptation for Model-Based RL](https://arxiv.org/abs/1812.07671) (2018) [[bib]](https://github.com/optimass/continual_learning_papers/blob/master/bibtex.bib#L334-L341)
```
Formulates an online learning procedure that uses SGD to update model parameters, and an EM with a Chinese restaurant process prior to develop and maintain a mixture of models to handle non-stationary task distribution
```


[//]: ### (Lifelong Reinforcement Learning)


### Continual Generative Modeling

[Continual Unsupervised Representation Learning](https://arxiv.org/pdf/1910.14481.pdf) (2019) [[bib]](https://github.com/optimass/continual_learning_papers/blob/master/bibtex.bib#L343-L350)
```
Introduces unsupervised continual learning (no task label and no task boundaries)
```

[Generative Models from the perspective of Continual Learning](https://arxiv.org/abs/1812.09111) (2018) [[bib]](https://github.com/optimass/continual_learning_papers/blob/master/bibtex.bib#L352-L363)
```
Extensive evaluation of CL methods for generative modeling
```

[Lifelong Generative Modeling](https://arxiv.org/abs/1705.09847) (2017) [[bib]](https://github.com/optimass/continual_learning_papers/blob/master/bibtex.bib#L-L)
```
first to focus on continual generative modeling (DGR's focus was still on continual supervised learning)
```

### Relevants 

#### 2019 

[Reccurent Independant Mechanisms](https://arxiv.org/pdf/1909.10893.pdf) [[bib]](https://github.com/optimass/continual_learning_papers/blob/master/bibtex.bib#L-L)
```

```

[A Meta-Transfer Objective for Learning to Disentangle Causal Mechanisms](https://arxiv.org/abs/1901.10912) [[bib]](https://github.com/optimass/continual_learning_papers/blob/master/bibtex.bib#L365-L370)
```
propose to meta-learn causal structures based on how fast a learner adapts to new distributions arising from sparse distributional changes, e.g. due to interventions, actions of agents and other sources of non-stationarities
```

[Modular Meta-learning](https://arxiv.org/abs/1806.10166) [[bib]](https://github.com/optimass/continual_learning_papers/blob/master/bibtex.bib#L372-L377)
```
Trains different modular (neural nets) structures on a set of related tasks and generalize to new tasks by composing the learned modules in new ways
```


#### 2018

[An Empirical Study of Example Forgetting during Deep Neural Network Learning](https://arxiv.org/abs/1812.05159) [[bib]](https://github.com/optimass/continual_learning_papers/blob/master/bibtex.bib#L379-L386)
```
(i) certain examples are forgotten with high frequency, and some not at all; (ii) (un)forgettable examples generalize across neural architectures; and (iii) based on forgetting dynamics, a significant fraction of examples can be omitted from the training data set while still maintaining state-of-the-art generalization performance
```

[Meta-Learning Update Rules for Unsupervised Representation Learning](https://arxiv.org/abs/1804.00222)
```

```


### (Unclassified)




## Paper Classification

family = {prior, rehearsal, dynamic, MCL, CML, hybrid}


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

## Continual Learning codebases


[Continual Learning Data Former](https://github.com/TLESORT/Continual_Learning_Data_Former)
```
 A pytorch compatible data loader to create and use sequence of tasks for Continual Learning 
```

[Online Learned Continual Compression with Stacked Quantization Module](https://github.com/pclucas14/stacked-quantized-modules)
\
```
Reproduce paper; useful of online compression
```

[Gradient Episodic Memory for Continual Learning](https://github.com/facebookresearch/GradientEpisodicMemory)
```
Reproduce paper. Nice repo because baselines and GEM are seamlessly interchangable
```

[Generative Models from the perspective of Continual Learning](https://github.com/TLESORT/Generative_Continual_Learning)
```
Complete repo for experiments in Generative Continual Learning
```

[Online Continual Learning with Maximally Interfered Retrieval](https://github.com/optimass/Maximally_Interfered_Retrieval)
```
Reproduce paper
```

[Learning to Learn without Forgetting by Maximizing Transfer and Minimizing Interference (MER)](https://github.com/mattriemer/mer)
```
Reproduce paper
```

