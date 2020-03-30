# Continual Learning Literature 
## Outline 
- [Classics](https://github.com/TLESORT/continual_learning_papers#Classics)
- [Surveys](https://github.com/TLESORT/continual_learning_papers#Surveys)
- [Influentials](https://github.com/TLESORT/continual_learning_papers#Influentials)
- [Regularization Methods](https://github.com/TLESORT/continual_learning_papers#Regularization-Methods)
- [Distillation Methods](https://github.com/TLESORT/continual_learning_papers#Distillation-Methods)
- [Rehearsal Methods](https://github.com/TLESORT/continual_learning_papers#Rehearsal-Methods)
- [Generative Replay Methods](https://github.com/TLESORT/continual_learning_papers#Generative-Replay-Methods)
- [Dynamic Architectures or Routing Methods](https://github.com/TLESORT/continual_learning_papers#Dynamic-Architectures-or-Routing-Methods)
- [Hybrid Methods](https://github.com/TLESORT/continual_learning_papers#Hybrid-Methods)
- [Meta Continual Learning](https://github.com/TLESORT/continual_learning_papers#Meta-Continual-Learning)
- [Lifelong Reinforcement Learning](https://github.com/TLESORT/continual_learning_papers#Lifelong-Reinforcement-Learning)
- [Continual Generative Modeling](https://github.com/TLESORT/continual_learning_papers#Continual-Generative-Modeling)

## Classics
- [**Lifelong robot learning**](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.71.3723&rep=rep1&type=pdf) , (1995) by *Thrun, Sebastian and Mitchell, Tom M* [[bib]](../bibtex.bib#L1-L10) 
``` 
Argues knowledge transfer is essential if robots are to learn control with moderate learning times
``` 
- [**Catastrophic Interference in Connectionist Networks: The Sequential Learning Problem**](https://www.sciencedirect.com/science/article/pii/S0079742108605368) , (1989) by *Michael McCloskey and Neal J. Cohen* [[bib]](../bibtex.bib#L553-L559) 
``` 
Introduces CL and reveals the catastrophic forgetting problem
``` 

## Surveys
- [**Continual learning for robotics: Definition, framework, learning strategies, opportunities and challenges**](http://www.sciencedirect.com/science/article/pii/S1566253519307377) , (2020) by *Timothée Lesort, Vincenzo Lomonaco, Andrei Stoian, Davide Maltoni, David Filliat and Natalia Díaz-Rodríguez* [[bib]](../bibtex.bib#L866-L878) 
``` 
Extensive review of CL methods and their applications in robotics and framework proposition for continual learning
``` 
- [**Three scenarios for continual learning**](https://arxiv.org/abs/1904.07734) , (2019) by *van de Ven, Gido M and Tolias, Andreas S* [[bib]](../bibtex.bib#L579-L586) 
``` 
An extensive review of CL methods in three different scenarios (task-, domain-, and class-incremental learning)
``` 
- [**Born to learn: The inspiration, progress, and future of evolved plastic artificial neural networks**](http://www.sciencedirect.com/science/article/pii/S0893608018302120) , (2018) by *Andrea Soltoggio, Kenneth O. Stanley and Sebastian Risi* [[bib]](../bibtex.bib#L730-L741) 
``` 
 
``` 

## Influentials
- [**Efficient Lifelong Learning with {A-GEM}**](https://arxiv.org/abs/1812.00420) , (2019) by *Chaudhry, Arslan, Ranzato, Marc’Aurelio, Rohrbach, Marcus and Elhoseiny, Mohamed* [[bib]](../bibtex.bib#L23-L30) 
``` 
More efficient GEM; Introduces online continual learning
``` 
- [**Towards Robust Evaluations of Continual Learning**](https://arxiv.org/abs/1805.09733) , (2018) by *Farquhar, Sebastian and Gal, Yarin* [[bib]](../bibtex.bib#L13-L20) 
``` 
Proposes desideratas and reexamines the evaluation protocol
``` 
- [**Continual learning with deep generative replay**](https://arxiv.org/abs/1705.08690) , (2017) by *Shin, Hanul, Lee, Jung Kwon, Kim, Jaehong and Kim, Jiwon* [[bib]](../bibtex.bib#L59-L67) 
``` 
Introduces generative replay
``` 
- [**An Empirical Investigation of Catastrophic Forgetting in Gradient-Based Neural Networks**](https://arxiv.org/abs/1705.08690) , (2013) by *Goodfellow, I.~J., Mirza, M., Xiao, D., Courville, A. and Bengio, Y.* [[bib]](../bibtex.bib#L70-L83) 
``` 
Investigates CF in neural networks
``` 

## Regularization Methods
- [**Continual Learning with Bayesian Neural Networks for Non-Stationary Data**](https://openreview.net/forum?id=SJlsFpVtDB) , (2020) by *Richard Kurle, Botond Cseke, Alexej Klushyn, Patrick van der Smagt and Stephan Günnemann* [[bib]](../bibtex.bib#L443-L450) 
``` 
continual learning for non-stationary data using Bayesian neural networks and memory-based online variational Bayes
``` 
- [**Functional Regularisation for Continual Learning with Gaussian Processes**](https://arxiv.org/abs/1901.11356) , (2019) by *Titsias, Michalis K, Schwarz, Jonathan, Matthews, Alexander G de G, Pascanu, Razvan and Teh, Yee Whye* [[bib]](../bibtex.bib#L896-L903) 
``` 
functional regularisation for Continual Learning: avoids forgetting a previous task by constructing and memorising an approximate posterior belief over the underlying task-specific function
``` 
- [**Progress \& compress: A scalable framework for continual learning**](https://arxiv.org/abs/1805.06370) , (2018) by *Schwarz, Jonathan, Luketina, Jelena, Czarnecki, Wojciech M, Grabska-Barwinska, Agnieszka, Teh, Yee Whye, Pascanu, Razvan and Hadsell, Raia* [[bib]](../bibtex.bib#L681-L688) 
``` 
A new P\&C architecture; online EWC for keeping the knowledge about the previous task, knowledge for keeping the knowledge about the current task (Multi-head setting, RL)
``` 
- [**Continual Learning Through Synaptic Intelligence**](http://proceedings.mlr.press/v70/zenke17a.html) , (2017) by *Zenke, Friedeman, Poole, Ben and Ganguli, Surya * [[bib]](../bibtex.bib#L299-L314) 
``` 
Synaptic Intelligence (SI). Importance of parameter measured based on their contribution to change in the loss. 
``` 

## Distillation Methods
- [**Large scale incremental learning**](https://arxiv.org/abs/1905.13260) , (2019) by *Wu, Yue, Chen, Yinpeng, Wang, Lijuan, Ye, Yuancheng, Liu, Zicheng, Guo, Yandong and Fu, Yun* [[bib]](../bibtex.bib#L600-L608) 
``` 
Introducing bias parameters to the last fully connected layer to resolve the data imbalance issue (Single-head setting)
``` 
- [**End-to-end incremental learning**](https://arxiv.org/abs/1807.09536) , (2018) by *Castro, Francisco M, Marin-Jimenez, Manuel J, Guil, Nicolas, Schmid, Cordelia and Alahari, Karteek* [[bib]](../bibtex.bib#L622-L630) 
``` 
Finetuning the last fully connected layer with a balanced dataset to resolve the data imbalance issue (Single-head setting)
``` 
- [**icarl: Incremental classifier and representation learning**](https://arxiv.org/abs/1611.07725) , (2017) by *Rebuffi, Sylvestre-Alvise, Kolesnikov, Alexander, Sperl, Georg and Lampert, Christoph H* [[bib]](../bibtex.bib#L633-L641) 
``` 
Binary cross-entropy loss for representation learning & exemplar memory (or coreset) for replay (Single-head setting)
``` 

## Rehearsal Methods
- **Experience replay for continual learning**, (2019) by *Rolnick, David, Ahuja, Arun, Schwarz, Jonathan, Lillicrap, Timothy and Wayne, Gregory* [[bib]](../bibtex.bib#L994-L1001) 
- [**icarl: Incremental classifier and representation learning**](https://arxiv.org/abs/1611.07725) , (2017) by *Rebuffi, Sylvestre-Alvise, Kolesnikov, Alexander, Sperl, Georg and Lampert, Christoph H* [[bib]](../bibtex.bib#L633-L641) 
``` 
Binary cross-entropy loss for representation learning & exemplar memory (or coreset) for replay (Single-head setting)
``` 

## Generative Replay Methods
- **Marginal replay vs conditional replay for continual learning**, (2019) by *Lesort, Timoth{\'e}e, Gepperth, Alexander, Stoian, Andrei and Filliat, David* [[bib]](../bibtex.bib#L946-L954) 
- [**Continual learning with deep generative replay**](https://arxiv.org/abs/1705.08690) , (2017) by *Shin, Hanul, Lee, Jung Kwon, Kim, Jaehong and Kim, Jiwon* [[bib]](../bibtex.bib#L59-L67) 
``` 
Introduces generative replay
``` 

## Dynamic Architectures or Routing Methods
- **A Neural Dirichlet Process Mixture Model for Task-Free Continual Learning**, (2020) by *Lee, Soochan, Ha, Junsoo, Zhang, Dongsu and Kim, Gunhee* [[bib]](../bibtex.bib#L133-L139) 
- [**Random Path Selection for Incremental Learning**](http://arxiv.org/abs/1906.01120) , (2019) by *Jathushan Rajasegaran and
Munawar Hayat and
Salman H. Khan and
Fahad Shahbaz Khan and
Ling Shao* [[bib]](../bibtex.bib#L204-L221) 
- [**Incremental Learning through Deep Adaptation**](https://openreview.net/forum?id=ryj0790hb) , (2018) by *Amir Rosenfeld and John K. Tsotsos* [[bib]](../bibtex.bib#L340-L346) 
- **{Progressive Neural Networks}**, (2016) by *{Rusu}, A.~A., {Rabinowitz}, N.~C., {Desjardins}, G., 
{Soyer}, H., {Kirkpatrick}, J., {Kavukcuoglu}, K., 
{Pascanu}, R. and {Hadsell}, R.* [[bib]](../bibtex.bib#L348-L362) 

## Hybrid Methods
- [**Continual learning with hypernetworks**](https://openreview.net/forum?id=SJgwNerKvB) , (2020) by *Anonymous* [[bib]](../bibtex.bib#L543-L551) 
- **Compacting, Picking and Growing for Unforgetting Continual Learning**, (2019) by *Hung, Ching-Yi, Tu, Cheng-Hao, Wu, Cheng-En, Chen, Chien-Hung, Chan, Yi-Ming and Chen, Chu-Song* [[bib]](../bibtex.bib#L112-L119) 

## Meta Continual Learning
- **Learning to Continually Learn**, (2020) by *Beaulieu, Shawn, Frati, Lapo, Miconi, Thomas, Lehman, Joel, Stanley, Kenneth O, Clune, Jeff and Cheney, Nick* [[bib]](../bibtex.bib#L969-L975) 
- **Meta-learnt priors slow down catastrophic forgetting in neural networks**, (2019) by *Spigler, Giacomo* [[bib]](../bibtex.bib#L977-L983) 
- **Learning to learn without forgetting by maximizing transfer and minimizing interference**, (2018) by *Riemer, Matthew, Cases, Ignacio, Ajemian, Robert, Liu, Miao, Rish, Irina, Tu, Yuhai and Tesauro, Gerald* [[bib]](../bibtex.bib#L986-L992) 

## Lifelong Reinforcement Learning
- [**Continual learning for robotics: Definition, framework, learning strategies, opportunities and challenges**](http://www.sciencedirect.com/science/article/pii/S1566253519307377) , (2020) by *Timothée Lesort, Vincenzo Lomonaco, Andrei Stoian, Davide Maltoni, David Filliat and Natalia Díaz-Rodríguez* [[bib]](../bibtex.bib#L866-L878) 
``` 
Extensive review of CL methods and their applications in robotics and framework proposition for continual learning
``` 
- **Experience replay for continual learning**, (2019) by *Rolnick, David, Ahuja, Arun, Schwarz, Jonathan, Lillicrap, Timothy and Wayne, Gregory* [[bib]](../bibtex.bib#L994-L1001) 

## Continual Generative Modeling
- **Marginal replay vs conditional replay for continual learning**, (2019) by *Lesort, Timoth{\'e}e, Gepperth, Alexander, Stoian, Andrei and Filliat, David* [[bib]](../bibtex.bib#L946-L954) 
- **Lifelong Generative Modeling**, (2017) by *Ramapuram, Jason, Gregorova, Magda and Kalousis, Alexandros* [[bib]](../bibtex.bib#L516-L522) 
