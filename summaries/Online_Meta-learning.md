# [Online Meta-Learning](https://arxiv.org/pdf/1902.08438.pdf)
## Chelsea Finn, Aravind Rajeswaran, Sham Kakade, Sergey Levine
  
## Introduction

Two distinct research paradigms have studied how prior tasks or experiences can be used by an agent to inform future learning.

* Meta Learning:  past experience is used to acquire a prior over model parameters or a learning procedure, and typically studies a setting where a set of meta-training tasks are made available together upfront
* Online learning : a sequential setting where tasks are revealed one after another, but aims to attain zero-shot generalization without any task-specific adaptation.

We argue that neither setting is ideal for studying continual lifelong learning. Meta-learning deals with learning to learn, but neglects the sequential and non-stationary aspects of the problem. Online learning offers an appealing theoretical framework, but does not generally consider how past experience can accelerate adaptation to a new task.

## Online Learning

Online learning focuses on regret minimization. Most standard notion of regret is to compare to the cumulative loss of the best fixed model in hindsight:
![](https://i.imgur.com/pbZG4kK.png)
One way minimize regret is with Follow the Leader (FTL):
![](https://i.imgur.com/NCs73vG.png)

## Online Meta-learning Setting:

let $U_t$ be the update procedure for task $t$
e.g. in MAML:
![](https://i.imgur.com/Q4I4HkD.png)

<img src="https://latex.codecogs.com/gif.latex?O_t=\text { Onset event at time bin } t " />

The overall protocol for the setting is as follows:
1. At round t, the agent chooses a model defined by $w_t$
2. The world simultaneously chooses task defined by $f_t$ 
3. The agent obtains access to the update procedure $U_t$, and uses it to update parameters as $\tilde w_t = U_t(w_t)$
4. The agent incurs loss $f_t(\tilde w_t )$. Advance to round t + 1.

the goal for the agent is to minimize regrets over rounds.
Achieving sublinear regrets means you're improving and converging to upper bound (joint training on all tasks)


## Algorithm and Analysis:

Follow the meta-leader (FTML): 
![](https://i.imgur.com/qWb9g8Q.png)

FTML’s regret is sublinear (under some assumption)
