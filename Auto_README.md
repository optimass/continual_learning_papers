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
- **Lifelong robot learning**, (1995) [[bib]](../bibtex_me.bib#L1-L9)  by *Thrun, Sebastian and Mitchell, Tom M*
``` 
Argues knowledge transfer is essential if robots are to learn control with moderate learning times
``` 
- **Catastrophic Interference in Connectionist Networks: The Sequential Learning Problem**, (1989) [[bib]](../bibtex_me.bib#L526-L531)  by *Michael McCloskey and Neal J. Cohen*
``` 
Introduces CL and reveals the catastrophic forgetting problem
``` 

## Surveys
- **Continual learning: A comparative study on how to defy forgetting in classification tasks**, (2019) [[bib]](../bibtex_me.bib#L82-L90)  by *Matthias De Lange, Rahaf Aljundi, Marc Masana, Sarah Parisot, Xu Jia, Ales Leonardis, Gregory Slabaugh and Tinne Tuytelaars*
``` 
Extensive empirical study of CL methods (in the multi-head setting)
``` 
- **Continual lifelong learning with neural networks: A review**, (2019) [[paper]](http://www.sciencedirect.com/science/article/pii/S0893608019300231)  [[bib]](../bibtex_me.bib#L93-L104)  by *German I. Parisi, Ronald Kemker, Jose L. Part, Christopher Kanan and Stefan Wermter*
``` 
An extensive review of CL
``` 
- **Three scenarios for continual learning**, (2019) [[bib]](../bibtex_me.bib#L551-L557)  by *van de Ven, Gido M and Tolias, Andreas S*
``` 
An extensive review of CL methods in three different scenarios (task-, domain-, and class-incremental learning)
``` 
- **Born to learn: The inspiration, progress, and future of evolved plastic artificial neural networks**, (2018) [[paper]](http://www.sciencedirect.com/science/article/pii/S0893608018302120)  [[bib]](../bibtex_me.bib#L688-L700)  by *Andrea Soltoggio, Kenneth O. Stanley and Sebastian Risi*
- **Continual learning for robotics: Definition, framework, learning strategies, opportunities and challenges**, (2020) [[paper]](http://www.sciencedirect.com/science/article/pii/S1566253519307377)  [[bib]](../bibtex_me.bib#L823-L835)  by *Timothée Lesort, Vincenzo Lomonaco, Andrei Stoian, Davide Maltoni, David Filliat and Natalia Díaz-Rodríguez*
``` 
Extensive review of CL methods and their applications in robotics and framework proposition for continual learning
``` 

## Influentials
- **Towards Robust Evaluations of Continual Learning**, (2018) [[bib]](../bibtex_me.bib#L12-L18)  by *Farquhar, Sebastian and Gal, Yarin*
``` 
Proposes desideratas and reexamines the evaluation protocol
``` 
- **Efficient Lifelong Learning with {A-GEM}**, (2019) [[paper]](https://arxiv.org/abs/1812.00420)  [[bib]](../bibtex_me.bib#L21-L28)  by *Chaudhry, Arslan, Ranzato, Marc’Aurelio, Rohrbach, Marcus and Elhoseiny, Mohamed*
``` 
More efficient GEM; Introduces online continual learning
``` 
- **Overcoming catastrophic forgetting in neural networks**, (2017) [[bib]](../bibtex_me.bib#L31-L38)  by *Kirkpatrick, James, Pascanu, Razvan, Rabinowitz, Neil, Veness, Joel, Desjardins, Guillaume, Rusu, Andrei A, Milan, Kieran, Quan, John, Ramalho, Tiago, Grabska-Barwinska, Agnieszka and others*
``` 
Introduces prior-focused methods
``` 
- **Gradient Episodic Memory for Continual Learning**, (2017) [[paper]](http://papers.nips.cc/paper/7225-gradient-episodic-memory-for-continual-learning.pdf)  [[bib]](../bibtex_me.bib#L42-L52)  by *Lopez-Paz, David and Ranzato, Marc-Aurelio*
``` 
A model that alliviates CF via constrained optimization
``` 
- **Continual learning with deep generative replay**, (2017) [[bib]](../bibtex_me.bib#L56-L63)  by *Shin, Hanul, Lee, Jung Kwon, Kim, Jaehong and Kim, Jiwon*
``` 
Introduces generative replay
``` 
- **{An Empirical Investigation of Catastrophic Forgetting in Gradient-Based Neural Networks}**, (2013) [[bib]](../bibtex_me.bib#L66-L79)  by *{Goodfellow}, I.~J., {Mirza}, M., {Xiao}, D., {Courville}, A. and 
{Bengio}, Y.*
``` 
Investigates CF in neural networks
``` 

## Regularization Methods
- **Efficient Lifelong Learning with {A-GEM}**, (2019) [[paper]](https://arxiv.org/abs/1812.00420)  [[bib]](../bibtex_me.bib#L21-L28)  by *Chaudhry, Arslan, Ranzato, Marc’Aurelio, Rohrbach, Marcus and Elhoseiny, Mohamed*
``` 
More efficient GEM; Introduces online continual learning
``` 
- **Overcoming catastrophic forgetting in neural networks**, (2017) [[bib]](../bibtex_me.bib#L31-L38)  by *Kirkpatrick, James, Pascanu, Razvan, Rabinowitz, Neil, Veness, Joel, Desjardins, Guillaume, Rusu, Andrei A, Milan, Kieran, Quan, John, Ramalho, Tiago, Grabska-Barwinska, Agnieszka and others*
``` 
Introduces prior-focused methods
``` 
- **Gradient Episodic Memory for Continual Learning**, (2017) [[paper]](http://papers.nips.cc/paper/7225-gradient-episodic-memory-for-continual-learning.pdf)  [[bib]](../bibtex_me.bib#L42-L52)  by *Lopez-Paz, David and Ranzato, Marc-Aurelio*
``` 
A model that alliviates CF via constrained optimization
``` 
- **Improving and Understanding Variational Continual Learning**, (2019) [[bib]](../bibtex_me.bib#L117-L124)  by *Siddharth Swaroop, Cuong V. Nguyen, Thang D. Bui and Richard E. Turner*
- **Uncertainty-guided Continual Learning with Bayesian Neural Networks**, (2019) [[bib]](../bibtex_me.bib#L135-L142)  by *Sayna Ebrahimi, Mohamed Elhoseiny, Trevor Darrell and Marcus Rohrbach*
- **Uncertainty-based Continual Learning with Adaptive Regularization**, (2019) [[paper]](http://papers.nips.cc/paper/8690-uncertainty-based-continual-learning-with-adaptive-regularization.pdf)  [[bib]](../bibtex_me.bib#L144-L154)  by *Ahn, Hongjoon, Cha, Sungmin, Lee, Donggyu and Moon, Taesup*
- **Task Agnostic Continual Learning Using Online Variational Bayes**, (2018) [[bib]](../bibtex_me.bib#L156-L164)  by *Chen Zeno, Itay Golan, Elad Hoffer and Daniel Soudry*
- **Overcoming Catastrophic Interference using Conceptor-Aided Backpropagation**, (2018) [[paper]](https://openreview.net/forum?id=B1al7jg0b)  [[bib]](../bibtex_me.bib#L213-L220)  by *Xu He and Herbert Jaeger*
- **Overcoming Catastrophic Forgetting with Hard Attention to the Task**, (2018) [[paper]](http://proceedings.mlr.press/v80/serra18a.html)  [[bib]](../bibtex_me.bib#L230-L246)  by *Serra, Joan, Suris, Didac, Miron, Marius and Karatzoglou, Alexandros*
- **Riemannian Walk for Incremental Learning: Understanding Forgetting and Intransigence**, (2018) [[bib]](../bibtex_me.bib#L248-L254)  by *Chaudhry, Arslan, Dokania, Puneet K, Ajanthan, Thalaiyasingam and Torr, Philip HS*
- **Memory Aware Synapses: Learning what (not) to forget**, (2017) [[paper]](http://arxiv.org/abs/1711.09601)  [[bib]](../bibtex_me.bib#L256-L269)  by *Rahaf Aljundi, Francesca Babiloni, Mohamed Elhoseiny, Marcus Rohrbach and Tinne Tuytelaars*
- **Variational Continual Learning**, (2018) [[paper]](https://openreview.net/forum?id=BkQqq0gRb)  [[bib]](../bibtex_me.bib#L271-L278)  by *Cuong V. Nguyen, Yingzhen Li, Thang D. Bui and Richard E. Turner*
- **Continual Learning Through Synaptic Intelligence**, (2017) [[paper]](http://proceedings.mlr.press/v70/zenke17a.html)  [[bib]](../bibtex_me.bib#L280-L295)  by *{Zenke}, Friedeman, {Poole}, Ben and {Ganguli}, Surya *
``` 
Synaptic Intelligence (SI). Importance of parameter measured based on their contribution to change in the loss. 
``` 
- **Continual Learning with Bayesian Neural Networks for Non-Stationary Data**, (2020) [[paper]](https://openreview.net/forum?id=SJlsFpVtDB)  [[bib]](../bibtex_me.bib#L417-L424)  by *Richard Kurle, Botond Cseke, Alexej Klushyn, Patrick van der Smagt and Stephan Günnemann*
- **Progress \& compress: A scalable framework for continual learning**, (2018) [[bib]](../bibtex_me.bib#L641-L647)  by *Schwarz, Jonathan, Luketina, Jelena, Czarnecki, Wojciech M, Grabska-Barwinska, Agnieszka, Teh, Yee Whye, Pascanu, Razvan and Hadsell, Raia*
- **Functional Regularisation for Continual Learning with Gaussian Processes**, (2019) [[bib]](../bibtex_me.bib#L853-L859)  by *Titsias, Michalis K, Schwarz, Jonathan, Matthews, Alexander G de G, Pascanu, Razvan and Teh, Yee Whye*

## Distillation Methods
- **Learning without forgetting**, (2017) [[bib]](../bibtex_me.bib#L298-L305)  by *Li, Zhizhong and Hoiem, Derek*
- **Overcoming Catastrophic Forgetting With Unlabeled Data in the Wild**, (2019) [[bib]](../bibtex_me.bib#L560-L567)  by *Lee, Kibok, Lee, Kimin, Shin, Jinwoo and Lee, Honglak*
- **Large scale incremental learning**, (2019) [[bib]](../bibtex_me.bib#L569-L576)  by *Wu, Yue, Chen, Yinpeng, Wang, Lijuan, Ye, Yuancheng, Liu, Zicheng, Guo, Yandong and Fu, Yun*
- **Lifelong learning via progressive distillation and retrospection**, (2018) [[bib]](../bibtex_me.bib#L578-L585)  by *Hou, Saihui, Pan, Xinyu, Change Loy, Chen, Wang, Zilei and Lin, Dahua*
- **End-to-end incremental learning**, (2018) [[bib]](../bibtex_me.bib#L587-L594)  by *Castro, Francisco M, Mar{\'\i}n-Jim{\'e}nez, Manuel J, Guil, Nicol{\'a}s, Schmid, Cordelia and Alahari, Karteek*
- **icarl: Incremental classifier and representation learning**, (2017) [[bib]](../bibtex_me.bib#L596-L603)  by *Rebuffi, Sylvestre-Alvise, Kolesnikov, Alexander, Sperl, Georg and Lampert, Christoph H*

## Rehearsal Methods
- **Efficient Lifelong Learning with {A-GEM}**, (2019) [[paper]](https://arxiv.org/abs/1812.00420)  [[bib]](../bibtex_me.bib#L21-L28)  by *Chaudhry, Arslan, Ranzato, Marc’Aurelio, Rohrbach, Marcus and Elhoseiny, Mohamed*
``` 
More efficient GEM; Introduces online continual learning
``` 
- **Gradient Episodic Memory for Continual Learning**, (2017) [[paper]](http://papers.nips.cc/paper/7225-gradient-episodic-memory-for-continual-learning.pdf)  [[bib]](../bibtex_me.bib#L42-L52)  by *Lopez-Paz, David and Ranzato, Marc-Aurelio*
``` 
A model that alliviates CF via constrained optimization
``` 
- **Orthogonal Gradient Descent for Continual Learning**, (2019) [[bib]](../bibtex_me.bib#L342-L350)  by *Mehrdad Farajtabar, Navid Azizan, Alex Mott and Ang Li*
- **Gradient based sample selection for online continual learning**, (2019) [[paper]](http://papers.nips.cc/paper/9354-gradient-based-sample-selection-for-online-continual-learning.pdf)  [[bib]](../bibtex_me.bib#L352-L362)  by *Aljundi, Rahaf, Lin, Min, Goujaud, Baptiste and Bengio, Yoshua*
- **Online Learned Continual Compression with Stacked Quantization Module**, (2019) [[bib]](../bibtex_me.bib#L376-L382)  by *Caccia, Lucas, Belilovsky, Eugene, Caccia, Massimo and Pineau, Joelle*
- **icarl: Incremental classifier and representation learning**, (2017) [[bib]](../bibtex_me.bib#L596-L603)  by *Rebuffi, Sylvestre-Alvise, Kolesnikov, Alexander, Sperl, Georg and Lampert, Christoph H*
- **Experience replay for continual learning**, (2019) [[bib]](../bibtex_me.bib#L950-L957)  by *Rolnick, David, Ahuja, Arun, Schwarz, Jonathan, Lillicrap, Timothy and Wayne, Gregory*

## Generative Replay Methods
- **Continual learning with deep generative replay**, (2017) [[bib]](../bibtex_me.bib#L56-L63)  by *Shin, Hanul, Lee, Jung Kwon, Kim, Jaehong and Kim, Jiwon*
``` 
Introduces generative replay
``` 
- **{Generative Models from the perspective of Continual Learning}**, (2019) [[paper]](https://hal.archives-ouvertes.fr/hal-01951954)  [[bib]](../bibtex_me.bib#L475-L487)  by *Lesort, Timoth{\'e}e, Caselles-Dupr{\'e}, Hugo, Garcia-Ortiz, Michael, Goudou, Jean-Fran{\c c}ois and Filliat, David*
- **Marginal replay vs conditional replay for continual learning**, (2019) [[bib]](../bibtex_me.bib#L902-L910)  by *Lesort, Timoth{\'e}e, Gepperth, Alexander, Stoian, Andrei and Filliat, David*

## Dynamic Architectures or Routing Methods
- **A Neural Dirichlet Process Mixture Model for Task-Free Continual Learning**, (2020) [[bib]](../bibtex_me.bib#L126-L132)  by *Lee, Soochan, Ha, Junsoo, Zhang, Dongsu and Kim, Gunhee*
- **Continual Learning with Adaptive Weights (CLAW)**, (2019) [[bib]](../bibtex_me.bib#L166-L172)  by *Adel, Tameem, Zhao, Han and Turner, Richard E*
- **{ORACLE:} Order Robust Adaptive Continual LEarning**, (2019) [[paper]](http://arxiv.org/abs/1902.09432)  [[bib]](../bibtex_me.bib#L174-L190)  by *Jaehong Yoon and
Saehoon Kim and
Eunho Yang and
Sung Ju Hwang*
- **Random Path Selection for Incremental Learning**, (2019) [[paper]](http://arxiv.org/abs/1906.01120)  [[bib]](../bibtex_me.bib#L192-L209)  by *Jathushan Rajasegaran and
Munawar Hayat and
Salman H. Khan and
Fahad Shahbaz Khan and
Ling Shao*
- **Incremental Learning through Deep Adaptation**, (2018) [[paper]](https://openreview.net/forum?id=ryj0790hb)  [[bib]](../bibtex_me.bib#L318-L324)  by *Amir Rosenfeld and John K. Tsotsos*
- **{Progressive Neural Networks}**, (2016) [[bib]](../bibtex_me.bib#L326-L340)  by *{Rusu}, A.~A., {Rabinowitz}, N.~C., {Desjardins}, G., 
{Soyer}, H., {Kirkpatrick}, J., {Kavukcuoglu}, K., 
{Pascanu}, R. and {Hadsell}, R.*

## Hybrid Methods
- **Compacting, Picking and Growing for Unforgetting Continual Learning**, (2019) [[bib]](../bibtex_me.bib#L107-L114)  by *Hung, Ching-Yi, Tu, Cheng-Hao, Wu, Cheng-En, Chen, Chien-Hung, Chan, Yi-Ming and Chen, Chu-Song*
- **Continual learning with hypernetworks**, (2020) [[paper]](https://openreview.net/forum?id=SJgwNerKvB)  [[bib]](../bibtex_me.bib#L516-L524)  by *Anonymous*

## Meta Continual Learning
- **Meta-Learning Representations for Continual Learning**, (2019) [[paper]](http://papers.nips.cc/paper/8458-meta-learning-representations-for-continual-learning.pdf)  [[bib]](../bibtex_me.bib#L394-L404)  by *Javed, Khurram and White, Martha*
- **Learning from the Past: Continual Meta-Learning via Bayesian Graph Modeling**, (2019) [[bib]](../bibtex_me.bib#L406-L414)  by *Yadan Luo, Zi Huang, Zheng Zhang, Ziwei Wang, Mahsa Baktashmotlagh and Yang Yang*
- **Online Meta-Learning**, (2019) [[paper]](http://proceedings.mlr.press/v97/finn19a.html)  [[bib]](../bibtex_me.bib#L426-L441)  by *Finn, Chelsea, Rajeswaran, Aravind, Kakade, Sham and Levine, Sergey*
- **Reconciling meta-learning and continual learning with online mixtures of tasks**, (2019) [[paper]](http://papers.nips.cc/paper/9112-reconciling-meta-learning-and-continual-learning-with-online-mixtures-of-tasks.pdf)  [[bib]](../bibtex_me.bib#L443-L453)  by *Jerfel, Ghassen, Grant, Erin, Griffiths, Tom and Heller, Katherine A*
- **Deep Online Learning Via Meta-Learning: Continual Adaptation for Model-Based {RL}**, (2019) [[paper]](https://openreview.net/forum?id=HyxAfnA5tm)  [[bib]](../bibtex_me.bib#L456-L463)  by *Anusha Nagabandi, Chelsea Finn and Sergey Levine*
- **Task Agnostic Continual Learning via Meta Learning**, (2019) [[bib]](../bibtex_me.bib#L534-L541)  by *Xu He, Jakub Sygnowski, Alexandre Galashov, Andrei A. Rusu, Yee Whye Teh and Razvan Pascanu*
- **Learning to Continually Learn**, (2020) [[bib]](../bibtex_me.bib#L925-L931)  by *Beaulieu, Shawn, Frati, Lapo, Miconi, Thomas, Lehman, Joel, Stanley, Kenneth O, Clune, Jeff and Cheney, Nick*
- **Meta-learnt priors slow down catastrophic forgetting in neural networks**, (2019) [[bib]](../bibtex_me.bib#L933-L939)  by *Spigler, Giacomo*
- **Learning to learn without forgetting by maximizing transfer and minimizing interference**, (2018) [[bib]](../bibtex_me.bib#L942-L948)  by *Riemer, Matthew, Cases, Ignacio, Ajemian, Robert, Liu, Miao, Rish, Irina, Tu, Yuhai and Tesauro, Gerald*

## Lifelong Reinforcement Learning
- **Continual learning for robotics: Definition, framework, learning strategies, opportunities and challenges**, (2020) [[paper]](http://www.sciencedirect.com/science/article/pii/S1566253519307377)  [[bib]](../bibtex_me.bib#L823-L835)  by *Timothée Lesort, Vincenzo Lomonaco, Andrei Stoian, Davide Maltoni, David Filliat and Natalia Díaz-Rodríguez*
``` 
Extensive review of CL methods and their applications in robotics and framework proposition for continual learning
``` 
- **Experience replay for continual learning**, (2019) [[bib]](../bibtex_me.bib#L950-L957)  by *Rolnick, David, Ahuja, Arun, Schwarz, Jonathan, Lillicrap, Timothy and Wayne, Gregory*

## Continual Generative Modeling
- **Continual learning with deep generative replay**, (2017) [[bib]](../bibtex_me.bib#L56-L63)  by *Shin, Hanul, Lee, Jung Kwon, Kim, Jaehong and Kim, Jiwon*
``` 
Introduces generative replay
``` 
- **Continual Unsupervised Representation Learning**, (2019) [[bib]](../bibtex_me.bib#L465-L473)  by *Dushyant Rao, Francesco Visin, Andrei A. Rusu, Yee Whye Teh, Razvan Pascanu and Raia Hadsell*
- **{Generative Models from the perspective of Continual Learning}**, (2019) [[paper]](https://hal.archives-ouvertes.fr/hal-01951954)  [[bib]](../bibtex_me.bib#L475-L487)  by *Lesort, Timoth{\'e}e, Caselles-Dupr{\'e}, Hugo, Garcia-Ortiz, Michael, Goudou, Jean-Fran{\c c}ois and Filliat, David*
- **Lifelong Generative Modeling**, (2017) [[bib]](../bibtex_me.bib#L489-L495)  by *Ramapuram, Jason, Gregorova, Magda and Kalousis, Alexandros*
- **Marginal replay vs conditional replay for continual learning**, (2019) [[bib]](../bibtex_me.bib#L902-L910)  by *Lesort, Timoth{\'e}e, Gepperth, Alexander, Stoian, Andrei and Filliat, David*
