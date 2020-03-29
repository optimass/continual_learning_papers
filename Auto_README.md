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
- [**Catastrophic Interference in Connectionist Networks: The Sequential Learning Problem**](https://www.sciencedirect.com/science/article/pii/S0079742108605368) , (1989) by *Michael McCloskey and Neal J. Cohen* [[bib]](../bibtex.bib#L552-L558) 
``` 
Introduces CL and reveals the catastrophic forgetting problem
``` 

## Surveys
- [**Continual learning: A comparative study on how to defy forgetting in classification tasks**](https://arxiv.org/abs/1909.08383) , (2019) by *Matthias De Lange, Rahaf Aljundi, Marc Masana, Sarah Parisot, Xu Jia, Ales Leonardis, Gregory Slabaugh and Tinne Tuytelaars* [[bib]](../bibtex.bib#L86-L95) 
``` 
Extensive empirical study of CL methods (in the multi-head setting)
``` 
- [**Continual lifelong learning with neural networks: A review**](http://www.sciencedirect.com/science/article/pii/S0893608019300231) , (2019) by *German I. Parisi, Ronald Kemker, Jose L. Part, Christopher Kanan and Stefan Wermter* [[bib]](../bibtex.bib#L98-L109) 
``` 
An extensive review of CL
``` 
- [**Three scenarios for continual learning**](https://arxiv.org/abs/1904.07734) , (2019) by *van de Ven, Gido M and Tolias, Andreas S* [[bib]](../bibtex.bib#L578-L585) 
``` 
An extensive review of CL methods in three different scenarios (task-, domain-, and class-incremental learning)
``` 
- [**Born to learn: The inspiration, progress, and future of evolved plastic artificial neural networks**](http://www.sciencedirect.com/science/article/pii/S0893608018302120) , (2018) by *Andrea Soltoggio, Kenneth O. Stanley and Sebastian Risi* [[bib]](../bibtex.bib#L729-L740) 
``` 
 
``` 
- [**Continual learning for robotics: Definition, framework, learning strategies, opportunities and challenges**](http://www.sciencedirect.com/science/article/pii/S1566253519307377) , (2020) by *Timothée Lesort, Vincenzo Lomonaco, Andrei Stoian, Davide Maltoni, David Filliat and Natalia Díaz-Rodríguez* [[bib]](../bibtex.bib#L865-L877) 
``` 
Extensive review of CL methods and their applications in robotics and framework proposition for continual learning
``` 

## Influentials
- [**Towards Robust Evaluations of Continual Learning**](https://arxiv.org/abs/1805.09733) , (2018) by *Farquhar, Sebastian and Gal, Yarin* [[bib]](../bibtex.bib#L13-L20) 
``` 
Proposes desideratas and reexamines the evaluation protocol
``` 
- [**Efficient Lifelong Learning with {A-GEM}**](https://arxiv.org/abs/1812.00420) , (2019) by *Chaudhry, Arslan, Ranzato, Marc’Aurelio, Rohrbach, Marcus and Elhoseiny, Mohamed* [[bib]](../bibtex.bib#L23-L30) 
``` 
More efficient GEM; Introduces online continual learning
``` 
- [**Overcoming catastrophic forgetting in neural networks**](https://www.pnas.org/content/pnas/114/13/3521.full.pdf) , (2017) by *Kirkpatrick, James, Pascanu, Razvan, Rabinowitz, Neil, Veness, Joel, Desjardins, Guillaume, Rusu, Andrei A, Milan, Kieran, Quan, John, Ramalho, Tiago, Grabska-Barwinska, Agnieszka and others* [[bib]](../bibtex.bib#L33-L41) 
``` 
Introduces prior-focused methods (Elastic Weight Consolidation)
``` 
- [**Gradient Episodic Memory for Continual Learning**](http://papers.nips.cc/paper/7225-gradient-episodic-memory-for-continual-learning.pdf) , (2017) by *Lopez-Paz, David and Ranzato, Marc-Aurelio* [[bib]](../bibtex.bib#L45-L55) 
``` 
A model that alliviates CF via constrained optimization
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
- [**Overcoming catastrophic forgetting in neural networks**](https://www.pnas.org/content/pnas/114/13/3521.full.pdf) , (2017) by *Kirkpatrick, James, Pascanu, Razvan, Rabinowitz, Neil, Veness, Joel, Desjardins, Guillaume, Rusu, Andrei A, Milan, Kieran, Quan, John, Ramalho, Tiago, Grabska-Barwinska, Agnieszka and others* [[bib]](../bibtex.bib#L33-L41) 
``` 
Introduces prior-focused methods (Elastic Weight Consolidation)
``` 
- [**Improving and Understanding Variational Continual Learning**](https://arxiv.org/abs/1905.02099) , (2019) by *Siddharth Swaroop, Cuong V. Nguyen, Thang D. Bui and Richard E. Turner* [[bib]](../bibtex.bib#L122-L130) 
- [**Uncertainty-guided Continual Learning with Bayesian Neural Networks**](https://arxiv.org/abs/1906.02425) , (2019) by *Sayna Ebrahimi, Mohamed Elhoseiny, Trevor Darrell and Marcus Rohrbach* [[bib]](../bibtex.bib#L142-L150) 
``` 
Uses Bayes by Backprop for variational Continual Learning.
``` 
- [**Uncertainty-based Continual Learning with Adaptive Regularization**](http://papers.nips.cc/paper/8690-uncertainty-based-continual-learning-with-adaptive-regularization.pdf) , (2019) by *Ahn, Hongjoon, Cha, Sungmin, Lee, Donggyu and Moon, Taesup* [[bib]](../bibtex.bib#L153-L163) 
``` 
Introduces VCL with uncertainty measured for neurons instead of weights.
``` 
- [**Task Agnostic Continual Learning Using Online Variational Bayes**](https://arxiv.org/pdf/1803.10123.pdf) , (2018) by *Chen Zeno, Itay Golan, Elad Hoffer and Daniel Soudry* [[bib]](../bibtex.bib#L166-L175) 
``` 
Introduces an optimizer for CL that relies on closed form updates of mu and sigma of BNN; introduce label trick for class learning (single-head)
``` 
- [**Overcoming Catastrophic Interference using Conceptor-Aided Backpropagation**](https://openreview.net/forum?id=B1al7jg0b) , (2018) by *Xu He and Herbert Jaeger* [[bib]](../bibtex.bib#L225-L232) 
``` 
Conceptor-Aided Backprop (CAB): gradients are shielded by conceptors against degradation of previously learned tasks
``` 
- [**Overcoming Catastrophic Forgetting with Hard Attention to the Task**](http://proceedings.mlr.press/v80/serra18a.html) , (2018) by *Serra, Joan, Suris, Didac, Miron, Marius and Karatzoglou, Alexandros* [[bib]](../bibtex.bib#L244-L260) 
``` 
Introducing a hard attention idea with binary masks
``` 
- [**Riemannian Walk for Incremental Learning: Understanding Forgetting and Intransigence**](https://arxiv.org/abs/1801.10112) , (2018) by *Chaudhry, Arslan, Dokania, Puneet K, Ajanthan, Thalaiyasingam and Torr, Philip HS* [[bib]](../bibtex.bib#L263-L270) 
``` 
Formalizes the shortcomings of multi-head evaluation, as well as the importance of replay in single-head setup. Presenting an improved version of EWC.
``` 
- [**Memory Aware Synapses: Learning what (not) to forget**](http://arxiv.org/abs/1711.09601) , (2017) by *Rahaf Aljundi, Francesca Babiloni, Mohamed Elhoseiny, Marcus Rohrbach and Tinne Tuytelaars* [[bib]](../bibtex.bib#L273-L286) 
``` 
Importance of parameter measured based on their contribution to change in the learned prediction function
``` 
- [**Variational Continual Learning**](https://arxiv.org/abs/1710.10628) , (2018) by *Cuong V. Nguyen, Yingzhen Li, Thang D. Bui and Richard E. Turner* [[bib]](../bibtex.bib#L289-L296) 
``` 
Introduces the idea of using previous task's posterior as the new task's prior in a BNN.
``` 
- [**Continual Learning Through Synaptic Intelligence**](http://proceedings.mlr.press/v70/zenke17a.html) , (2017) by *Zenke, Friedeman, Poole, Ben and Ganguli, Surya * [[bib]](../bibtex.bib#L299-L314) 
``` 
Synaptic Intelligence (SI). Importance of parameter measured based on their contribution to change in the loss. 
``` 
- [**Continual Learning with Bayesian Neural Networks for Non-Stationary Data**](https://openreview.net/forum?id=SJlsFpVtDB) , (2020) by *Richard Kurle, Botond Cseke, Alexej Klushyn, Patrick van der Smagt and Stephan Günnemann* [[bib]](../bibtex.bib#L442-L449) 
``` 
continual learning for non-stationary data using Bayesian neural networks and memory-based online variational Bayes
``` 
- [**Progress \& compress: A scalable framework for continual learning**](https://arxiv.org/abs/1805.06370) , (2018) by *Schwarz, Jonathan, Luketina, Jelena, Czarnecki, Wojciech M, Grabska-Barwinska, Agnieszka, Teh, Yee Whye, Pascanu, Razvan and Hadsell, Raia* [[bib]](../bibtex.bib#L680-L687) 
``` 
A new P\&C architecture; online EWC for keeping the knowledge about the previous task, knowledge for keeping the knowledge about the current task (Multi-head setting, RL)
``` 
- [**Functional Regularisation for Continual Learning with Gaussian Processes**](https://arxiv.org/abs/1901.11356) , (2019) by *Titsias, Michalis K, Schwarz, Jonathan, Matthews, Alexander G de G, Pascanu, Razvan and Teh, Yee Whye* [[bib]](../bibtex.bib#L895-L902) 
``` 
functional regularisation for Continual Learning: avoids forgetting a previous task by constructing and memorising an approximate posterior belief over the underlying task-specific function
``` 

## Distillation Methods
- [**Learning without forgetting**](https://arxiv.org/abs/1606.09282) , (2017) by *Li, Zhizhong and Hoiem, Derek* [[bib]](../bibtex.bib#L317-L325) 
``` 
Functional regularization through distillation (keeping the output of the updated network on the new data close to the output of the old network on the new data)
``` 
- [**Overcoming Catastrophic Forgetting With Unlabeled Data in the Wild**](https://arxiv.org/abs/1903.12648) , (2019) by *Lee, Kibok, Lee, Kimin, Shin, Jinwoo and Lee, Honglak* [[bib]](../bibtex.bib#L588-L596) 
``` 
Introducing global distillation loss and balanced finetuning; leveraging unlabeled data in the open world setting (Single-head setting)
``` 
- [**Large scale incremental learning**](https://arxiv.org/abs/1905.13260) , (2019) by *Wu, Yue, Chen, Yinpeng, Wang, Lijuan, Ye, Yuancheng, Liu, Zicheng, Guo, Yandong and Fu, Yun* [[bib]](../bibtex.bib#L599-L607) 
``` 
Introducing bias parameters to the last fully connected layer to resolve the data imbalance issue (Single-head setting)
``` 
- [**Lifelong learning via progressive distillation and retrospection**](https://arxiv.org/abs/1905.13260) , (2018) by *Hou, Saihui, Pan, Xinyu, Change Loy, Chen, Wang, Zilei and Lin, Dahua* [[bib]](../bibtex.bib#L610-L618) 
``` 
Introducing an expert of the current task in the knowledge distillation method (Multi-head setting)
``` 
- [**End-to-end incremental learning**](https://arxiv.org/abs/1807.09536) , (2018) by *Castro, Francisco M, Marin-Jimenez, Manuel J, Guil, Nicolas, Schmid, Cordelia and Alahari, Karteek* [[bib]](../bibtex.bib#L621-L629) 
``` 
Finetuning the last fully connected layer with a balanced dataset to resolve the data imbalance issue (Single-head setting)
``` 
- [**icarl: Incremental classifier and representation learning**](https://arxiv.org/abs/1611.07725) , (2017) by *Rebuffi, Sylvestre-Alvise, Kolesnikov, Alexander, Sperl, Georg and Lampert, Christoph H* [[bib]](../bibtex.bib#L632-L640) 
``` 
Binary cross-entropy loss for representation learning & exemplar memory (or coreset) for replay (Single-head setting)
``` 

## Rehearsal Methods
- [**Efficient Lifelong Learning with {A-GEM}**](https://arxiv.org/abs/1812.00420) , (2019) by *Chaudhry, Arslan, Ranzato, Marc’Aurelio, Rohrbach, Marcus and Elhoseiny, Mohamed* [[bib]](../bibtex.bib#L23-L30) 
``` 
More efficient GEM; Introduces online continual learning
``` 
- [**Gradient Episodic Memory for Continual Learning**](http://papers.nips.cc/paper/7225-gradient-episodic-memory-for-continual-learning.pdf) , (2017) by *Lopez-Paz, David and Ranzato, Marc-Aurelio* [[bib]](../bibtex.bib#L45-L55) 
``` 
A model that alliviates CF via constrained optimization
``` 
- **Orthogonal Gradient Descent for Continual Learning**, (2019) by *Mehrdad Farajtabar, Navid Azizan, Alex Mott and Ang Li* [[bib]](../bibtex.bib#L364-L372) 
- [**Gradient based sample selection for online continual learning**](http://papers.nips.cc/paper/9354-gradient-based-sample-selection-for-online-continual-learning.pdf) , (2019) by *Aljundi, Rahaf, Lin, Min, Goujaud, Baptiste and Bengio, Yoshua* [[bib]](../bibtex.bib#L374-L384) 
- **Online Learned Continual Compression with Adaptative Quantization Module**, (2019) by *Caccia, Lucas, Belilovsky, Eugene, Caccia, Massimo and Pineau, Joelle* [[bib]](../bibtex.bib#L400-L406) 
``` 
Uses stacks of VQ-VAE modules to progressively compress the data stream, enabling better rehearsal
``` 
- [**icarl: Incremental classifier and representation learning**](https://arxiv.org/abs/1611.07725) , (2017) by *Rebuffi, Sylvestre-Alvise, Kolesnikov, Alexander, Sperl, Georg and Lampert, Christoph H* [[bib]](../bibtex.bib#L632-L640) 
``` 
Binary cross-entropy loss for representation learning & exemplar memory (or coreset) for replay (Single-head setting)
``` 
- **Experience replay for continual learning**, (2019) by *Rolnick, David, Ahuja, Arun, Schwarz, Jonathan, Lillicrap, Timothy and Wayne, Gregory* [[bib]](../bibtex.bib#L993-L1000) 

## Generative Replay Methods
- [**Continual learning with deep generative replay**](https://arxiv.org/abs/1705.08690) , (2017) by *Shin, Hanul, Lee, Jung Kwon, Kim, Jaehong and Kim, Jiwon* [[bib]](../bibtex.bib#L59-L67) 
``` 
Introduces generative replay
``` 
- [**{Generative Models from the perspective of Continual Learning}**](https://hal.archives-ouvertes.fr/hal-01951954) , (2019) by *Lesort, Timoth{\'e}e, Caselles-Dupr{\'e}, Hugo, Garcia-Ortiz, Michael, Goudou, Jean-Fran{\c c}ois and Filliat, David* [[bib]](../bibtex.bib#L501-L513) 
- **Marginal replay vs conditional replay for continual learning**, (2019) by *Lesort, Timoth{\'e}e, Gepperth, Alexander, Stoian, Andrei and Filliat, David* [[bib]](../bibtex.bib#L945-L953) 

## Dynamic Architectures or Routing Methods
- **A Neural Dirichlet Process Mixture Model for Task-Free Continual Learning**, (2020) by *Lee, Soochan, Ha, Junsoo, Zhang, Dongsu and Kim, Gunhee* [[bib]](../bibtex.bib#L133-L139) 
- **Continual Learning with Adaptive Weights (CLAW)**, (2019) by *Adel, Tameem, Zhao, Han and Turner, Richard E* [[bib]](../bibtex.bib#L178-L184) 
- [**{ORACLE:} Order Robust Adaptive Continual LEarning**](http://arxiv.org/abs/1902.09432) , (2019) by *Jaehong Yoon and
Saehoon Kim and
Eunho Yang and
Sung Ju Hwang* [[bib]](../bibtex.bib#L186-L202) 
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
- **Compacting, Picking and Growing for Unforgetting Continual Learning**, (2019) by *Hung, Ching-Yi, Tu, Cheng-Hao, Wu, Cheng-En, Chen, Chien-Hung, Chan, Yi-Ming and Chen, Chu-Song* [[bib]](../bibtex.bib#L112-L119) 
- [**Continual learning with hypernetworks**](https://openreview.net/forum?id=SJgwNerKvB) , (2020) by *Anonymous* [[bib]](../bibtex.bib#L542-L550) 

## Meta Continual Learning
- [**Meta-Learning Representations for Continual Learning**](http://papers.nips.cc/paper/8458-meta-learning-representations-for-continual-learning.pdf) , (2019) by *Javed, Khurram and White, Martha* [[bib]](../bibtex.bib#L419-L429) 
- **Learning from the Past: Continual Meta-Learning via Bayesian Graph Modeling**, (2019) by *Yadan Luo, Zi Huang, Zheng Zhang, Ziwei Wang, Mahsa Baktashmotlagh and Yang Yang* [[bib]](../bibtex.bib#L431-L439) 
- [**Online Meta-Learning**](http://proceedings.mlr.press/v97/finn19a.html) , (2019) by *Finn, Chelsea, Rajeswaran, Aravind, Kakade, Sham and Levine, Sergey* [[bib]](../bibtex.bib#L452-L467) 
- [**Reconciling meta-learning and continual learning with online mixtures of tasks**](http://papers.nips.cc/paper/9112-reconciling-meta-learning-and-continual-learning-with-online-mixtures-of-tasks.pdf) , (2019) by *Jerfel, Ghassen, Grant, Erin, Griffiths, Tom and Heller, Katherine A* [[bib]](../bibtex.bib#L469-L479) 
- [**Deep Online Learning Via Meta-Learning: Continual Adaptation for Model-Based {RL}**](https://openreview.net/forum?id=HyxAfnA5tm) , (2019) by *Anusha Nagabandi, Chelsea Finn and Sergey Levine* [[bib]](../bibtex.bib#L482-L489) 
- **Task Agnostic Continual Learning via Meta Learning**, (2019) by *Xu He, Jakub Sygnowski, Alexandre Galashov, Andrei A. Rusu, Yee Whye Teh and Razvan Pascanu* [[bib]](../bibtex.bib#L561-L568) 
- **Learning to Continually Learn**, (2020) by *Beaulieu, Shawn, Frati, Lapo, Miconi, Thomas, Lehman, Joel, Stanley, Kenneth O, Clune, Jeff and Cheney, Nick* [[bib]](../bibtex.bib#L968-L974) 
- **Meta-learnt priors slow down catastrophic forgetting in neural networks**, (2019) by *Spigler, Giacomo* [[bib]](../bibtex.bib#L976-L982) 
- **Learning to learn without forgetting by maximizing transfer and minimizing interference**, (2018) by *Riemer, Matthew, Cases, Ignacio, Ajemian, Robert, Liu, Miao, Rish, Irina, Tu, Yuhai and Tesauro, Gerald* [[bib]](../bibtex.bib#L985-L991) 

## Lifelong Reinforcement Learning
- [**Continual learning for robotics: Definition, framework, learning strategies, opportunities and challenges**](http://www.sciencedirect.com/science/article/pii/S1566253519307377) , (2020) by *Timothée Lesort, Vincenzo Lomonaco, Andrei Stoian, Davide Maltoni, David Filliat and Natalia Díaz-Rodríguez* [[bib]](../bibtex.bib#L865-L877) 
``` 
Extensive review of CL methods and their applications in robotics and framework proposition for continual learning
``` 
- **Experience replay for continual learning**, (2019) by *Rolnick, David, Ahuja, Arun, Schwarz, Jonathan, Lillicrap, Timothy and Wayne, Gregory* [[bib]](../bibtex.bib#L993-L1000) 

## Continual Generative Modeling
- [**Continual learning with deep generative replay**](https://arxiv.org/abs/1705.08690) , (2017) by *Shin, Hanul, Lee, Jung Kwon, Kim, Jaehong and Kim, Jiwon* [[bib]](../bibtex.bib#L59-L67) 
``` 
Introduces generative replay
``` 
- **Continual Unsupervised Representation Learning**, (2019) by *Dushyant Rao, Francesco Visin, Andrei A. Rusu, Yee Whye Teh, Razvan Pascanu and Raia Hadsell* [[bib]](../bibtex.bib#L491-L499) 
- [**{Generative Models from the perspective of Continual Learning}**](https://hal.archives-ouvertes.fr/hal-01951954) , (2019) by *Lesort, Timoth{\'e}e, Caselles-Dupr{\'e}, Hugo, Garcia-Ortiz, Michael, Goudou, Jean-Fran{\c c}ois and Filliat, David* [[bib]](../bibtex.bib#L501-L513) 
- **Lifelong Generative Modeling**, (2017) by *Ramapuram, Jason, Gregorova, Magda and Kalousis, Alexandros* [[bib]](../bibtex.bib#L515-L521) 
- **Marginal replay vs conditional replay for continual learning**, (2019) by *Lesort, Timoth{\'e}e, Gepperth, Alexander, Stoian, Andrei and Filliat, David* [[bib]](../bibtex.bib#L945-L953) 
