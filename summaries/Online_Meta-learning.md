# [Online Meta-Learning](https://arxiv.org/pdf/1902.08438.pdf)
## Chelsea Finn, Aravind Rajeswaran, Sham Kakade, Sergey Levine
  
### Introduction

Two distinct research paradigms have studied how prior tasks or experiences can be used by an agent to inform future learning.

* Meta Learning:  past experience is used to acquire a prior over model parameters or a learning procedure, and typically studies a setting where a set of meta-training tasks are made available together upfront
* Online learning : a sequential setting where tasks are revealed one after another, but aims to attain zero-shot generalization without any task-specific adaptation.

We argue that neither setting is ideal for studying continual lifelong learning. Meta-learning deals with learning to learn, but neglects the sequential and non-stationary aspects of the problem. Online learning offers an appealing theoretical framework, but does not generally consider how past experience can accelerate adaptation to a new task.

### Online Learning

Online learning focuses on regret minimization. Most standard notion of regret is to compare to the cumulative loss of the best fixed model in hindsight:

  

  
  
### Title of another important section
  
* important point
* another important point
  
  
### Some notes


* this paper made me think about that
* also, makes me question this
