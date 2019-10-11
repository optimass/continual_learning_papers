# Continual Learning Reading Group

## Schedule

Monday 1:30PM, Room H06 (6650 St-Urbain)

## Categories

* [Classics](#classics) (papers before Deep Learning area. Motivates and sets the stage for Continual Learning)
* [Influencials](#influentials) (well cited papers. More general contributions like proposing new desideratas, frameworks, evaluations, etc)
* [Rookies](#rookies) (new papers. e.g. NeurIPS 2019, ICLR 2020 submissions)
* [Prior-Focused Methods](#prior-focused-methods)
* [Dynamic Architectures](#dynamic-architectures)
* [Rehearsal Methods](#rehearsal-methods)
* [Meta Continual Learning](#meta-continual-learning) (learning to continually learn)
* [Continual Meta Learning](#continual-meta-learning) (continually learning to learn)
* [Lifelong Reinforcement Learning](#lifelong-reinforcement-learning)
* [Relevants](#relevants) (non-continual learning papers that can help us. Generalization, Biology, Psychology, Meta-Learning, etc)

#### Abreviations

Continual Learning (CL), Catastrophic Forgetting (CF), Generative Replay (GR)


## Papers

#### Classics

Title | Year | tl;dr
--- | --- | ---
[Lifelong robot learning](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.71.3723&rep=rep1&type=pdf) | 1995 | argues that knowledge transfer is essential if robots are to learn control with moderate learning times in complex scenarios

#### Influencials

Title | Year | tl;dr
--- | --- | ---
[An Empirical Investigation of Catastrophic Forgetting in Gradient-Based Neural Networks](https://arxiv.org/abs/1312.6211) | 2013 | Investigates CF in neural networks
[Elastic Weight Consolidation (EWC)](https://www.pnas.org/content/pnas/114/13/3521.full.pdf) | 2017 | Introduces prior-focused methods
[Gradient Episodic Memory (GEM)](https://arxiv.org/abs/1706.08840) | 2017 | a model that alliviates CF via constrained optimization
[Efficient Lifelong Learning with A-GEM](https://arxiv.org/abs/1812.00420) | 2018 | More efficient GEM; Introduces online continual learning
[Continual Learning with Deep Generative Replay (GR)](https://arxiv.org/abs/1705.08690) | 2017 | Introduces generative replay
[Continual Lifelong Learning with Neural Networks: A Review](https://arxiv.org/abs/1802.07569) | 2018 | A extensive review of CL
[Towards Robust Evaluations of Continual Learning](https://arxiv.org/abs/1805.09733) | 2018 | Proposes desideratas and reexamines the evaluation protocol

#### Rookies

Title | Year | tl;dr
--- | --- | ---

#### Prior-focused Methods

Title | Year | tl;dr
--- | --- | ---
[Elastic Weight Consolidation (EWC)](https://www.pnas.org/content/pnas/114/13/3521.full.pdf) | 2017 | Introduces prior-focused methods


#### Dynamic Architectures

Title | Year | tl;dr
--- | --- | ---
[Progressive neural networks](https://arxiv.org/abs/1606.04671) | 2016 |

#### Rehearsal Methods

Title | Year | tl;dr
--- | --- | ---
[Gradient Episodic Memory (GEM)](https://arxiv.org/abs/1706.08840) | 2017 | a model that alliviates CF via constrained optimization (doesn't increase loss on previous stored data)
[Efficient Lifelong Learning with A-GEM](https://arxiv.org/abs/1812.00420) | 2018 | More efficient GEM; Introduces online continual learning
[Continual Learning with Deep Generative Replay (GR)](https://arxiv.org/abs/1705.08690) | 2017 | Introduces generative replay
[Gradient based sample selection for online continual learning](https://arxiv.org/abs/1903.08671) | 2019 | sample selection as a constraint reduction problem based on the constrained optimization view of continual learning
[Generative replay with feedback connections as a general strategy for continual learning](https://arxiv.org/abs/1809.10635) | 2018 | smarter GR
[Generative Models from the perspective of Continual Learning](https://arxiv.org/abs/1812.09111) | 2018 | Extensive evaluation of CL methods for generative modeling

#### Meta Continual Learning

Title | Year | tl;dr
--- | --- | ---

#### Continual Meta Learning

Title | Year | tl;dr
--- | --- | ---
[Task Agnostic Continual Learning via Meta Learning](https://arxiv.org/abs/1906.05201) | 2019 | Introduces What and How framework; enables Task Agnostic CL with meta learned task inference
[Reconciling meta-learning and continual learning with online mixtures of tasks](https://arxiv.org/abs/1812.06080) | 2019 | Meta-learns a tasks structure; continual adaptation via non-parametric prior



#### Lifelong Reinforcement Learning

Title | Year | tl;dr
--- | --- | ---

#### Relevants 

Title | Year | tl;dr
--- | --- | ---


## Paper Classification

family = {prior, rehearsal, dynamic}


Title | Family | Single-Head | Task Agnostic | Online | Supervised | Generative | RL
---   | ---    | ---         | ---           | ---    | ---        | ---        | ---
[Elastic Weight Consolidation (EWC)](https://www.pnas.org/content/pnas/114/13/3521.full.pdf) | Prior | | | | :heavy_check_mark: | | :heavy_check_mark: 
[Continual Learning with Deep Generative Replay (GR)](https://arxiv.org/abs/1705.08690) | Rehearsal | | | | :heavy_check_mark: | :heavy_check_mark: || 
[Gradient based sample selection for online continual learning](https://arxiv.org/abs/1903.08671) | Rehearsal |  :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |  |  | 
[Generative replay with feedback connections as a general strategy for continual learning](https://arxiv.org/abs/1809.10635) | Rehearsal | :heavy_check_mark: | | | :heavy_check_mark: | :heavy_check_mark: | | 
