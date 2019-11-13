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
1. ![](https://latex.codecogs.com/gif.latex?%5Ctext%7BAt%20round%20t%2C%20the%20agent%20chooses%20a%20model%20defined%20by%20%7D%20w_t)
2. ![](https://latex.codecogs.com/gif.latex?%5Ctext%7BThe%20world%20simultaneously%20chooses%20task%20defined%20by%20%7D%20%24f_t%24)
3. ![](https://latex.codecogs.com/gif.latex?%5Csmall%20%5Ctext%7BThe%20agent%20obtains%20access%20to%20%7D%20U_t%20%5Ctext%7B%2C%20and%20uses%20it%20to%20update%20parameters%20as%20%7D%20%5Ctilde%20w_t%20%3D%20U_t%28w_t%29)
4. ![](https://latex.codecogs.com/gif.latex?%5Csmall%20%5Ctext%7BThe%20agent%20incurs%20loss%20%7D%20f_t%28%5Ctilde%20w_t%20%29%20%5Ctext%7B.%20Advance%20to%20round%20t%20&plus;%201%7D)

the goal for the agent is to minimize regrets over rounds.
Achieving sublinear regrets means you're improving and converging to upper bound (joint training on all tasks)


## Algorithm and Analysis:

Follow the meta-leader (FTML): 
![](https://i.imgur.com/qWb9g8Q.png)

FTML’s regret is sublinear (under some assumption)
