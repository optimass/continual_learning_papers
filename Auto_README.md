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
- **Lifelong robot learning**, (1995) by *Thrun, Sebastian and Mitchell, Tom M* [[bib]](../bibtex.bib#L1-L9) 
``` 
Argues knowledge transfer is essential if robots are to learn control with moderate learning times
``` 
- **Catastrophic Interference in Connectionist Networks: The Sequential Learning Problem**, (1989) by *Michael McCloskey and Neal J. Cohen* [[bib]](../bibtex.bib#L526-L531) 
``` 
Introduces CL and reveals the catastrophic forgetting problem
``` 

## Surveys
- **Continual learning: A comparative study on how to defy forgetting in classification tasks**, (2019) by *Matthias De Lange, Rahaf Aljundi, Marc Masana, Sarah Parisot, Xu Jia, Ales Leonardis, Gregory Slabaugh and Tinne Tuytelaars* [[bib]](../bibtex.bib#L82-L90) 
``` 
Extensive empirical study of CL methods (in the multi-head setting)
``` 
- [**Continual lifelong learning with neural networks: A review**](http://www.sciencedirect.com/science/article/pii/S0893608019300231) , (2019) by *German I. Parisi, Ronald Kemker, Jose L. Part, Christopher Kanan and Stefan Wermter* [[bib]](../bibtex.bib#L93-L104) 
``` 
An extensive review of CL
``` 
- **Three scenarios for continual learning**, (2019) by *van de Ven, Gido M and Tolias, Andreas S* [[bib]](../bibtex.bib#L551-L557) 
``` 
An extensive review of CL methods in three different scenarios (task-, domain-, and class-incremental learning)
``` 
- [**Born to learn: The inspiration, progress, and future of evolved plastic artificial neural networks**](http://www.sciencedirect.com/science/article/pii/S0893608018302120) , (2018) by *Andrea Soltoggio, Kenneth O. Stanley and Sebastian Risi* [[bib]](../bibtex.bib#L688-L700) 
- [**Continual learning for robotics: Definition, framework, learning strategies, opportunities and challenges**](http://www.sciencedirect.com/science/article/pii/S1566253519307377) , (2020) by *Timothée Lesort, Vincenzo Lomonaco, Andrei Stoian, Davide Maltoni, David Filliat and Natalia Díaz-Rodríguez* [[bib]](../bibtex.bib#L823-L835) 
``` 
Extensive review of CL methods and their applications in robotics and framework proposition for continual learning
``` 

## Influentials
- **Towards Robust Evaluations of Continual Learning**, (2018) by *Farquhar, Sebastian and Gal, Yarin* [[bib]](../bibtex.bib#L12-L18) 
``` 
Proposes desideratas and reexamines the evaluation protocol
``` 
- [**Efficient Lifelong Learning with {A-GEM}**](https://arxiv.org/abs/1812.00420) , (2019) by *Chaudhry, Arslan, Ranzato, Marc’Aurelio, Rohrbach, Marcus and Elhoseiny, Mohamed* [[bib]](../bibtex.bib#L21-L28) 
``` 
More efficient GEM; Introduces online continual learning
``` 
- **Overcoming catastrophic forgetting in neural networks**, (2017) by *Kirkpatrick, James, Pascanu, Razvan, Rabinowitz, Neil, Veness, Joel, Desjardins, Guillaume, Rusu, Andrei A, Milan, Kieran, Quan, John, Ramalho, Tiago, Grabska-Barwinska, Agnieszka and others* [[bib]](../bibtex.bib#L31-L38) 
``` 
Introduces prior-focused methods
``` 
- [**Gradient Episodic Memory for Continual Learning**](http://papers.nips.cc/paper/7225-gradient-episodic-memory-for-continual-learning.pdf) , (2017) by *Lopez-Paz, David and Ranzato, Marc-Aurelio* [[bib]](../bibtex.bib#L42-L52) 
``` 
A model that alliviates CF via constrained optimization
``` 
- **Continual learning with deep generative replay**, (2017) by *Shin, Hanul, Lee, Jung Kwon, Kim, Jaehong and Kim, Jiwon* [[bib]](../bibtex.bib#L56-L63) 
``` 
Introduces generative replay
``` 
- **{An Empirical Investigation of Catastrophic Forgetting in Gradient-Based Neural Networks}**, (2013) by *{Goodfellow}, I.~J., {Mirza}, M., {Xiao}, D., {Courville}, A. and 
{Bengio}, Y.* [[bib]](../bibtex.bib#L66-L79) 
``` 
Investigates CF in neural networks
``` 

## Regularization Methods
- [**Efficient Lifelong Learning with {A-GEM}**](https://arxiv.org/abs/1812.00420) , (2019) by *Chaudhry, Arslan, Ranzato, Marc’Aurelio, Rohrbach, Marcus and Elhoseiny, Mohamed* [[bib]](../bibtex.bib#L21-L28) 
``` 
More efficient GEM; Introduces online continual learning
``` 
- **Overcoming catastrophic forgetting in neural networks**, (2017) by *Kirkpatrick, James, Pascanu, Razvan, Rabinowitz, Neil, Veness, Joel, Desjardins, Guillaume, Rusu, Andrei A, Milan, Kieran, Quan, John, Ramalho, Tiago, Grabska-Barwinska, Agnieszka and others* [[bib]](../bibtex.bib#L31-L38) 
``` 
Introduces prior-focused methods
``` 
- [**Gradient Episodic Memory for Continual Learning**](http://papers.nips.cc/paper/7225-gradient-episodic-memory-for-continual-learning.pdf) , (2017) by *Lopez-Paz, David and Ranzato, Marc-Aurelio* [[bib]](../bibtex.bib#L42-L52) 
``` 
A model that alliviates CF via constrained optimization
``` 
- **Improving and Understanding Variational Continual Learning**, (2019) by *Siddharth Swaroop, Cuong V. Nguyen, Thang D. Bui and Richard E. Turner* [[bib]](../bibtex.bib#L117-L124) 
- **Uncertainty-guided Continual Learning with Bayesian Neural Networks**, (2019) by *Sayna Ebrahimi, Mohamed Elhoseiny, Trevor Darrell and Marcus Rohrbach* [[bib]](../bibtex.bib#L135-L142) 
- [**Uncertainty-based Continual Learning with Adaptive Regularization**](http://papers.nips.cc/paper/8690-uncertainty-based-continual-learning-with-adaptive-regularization.pdf) , (2019) by *Ahn, Hongjoon, Cha, Sungmin, Lee, Donggyu and Moon, Taesup* [[bib]](../bibtex.bib#L144-L154) 
- **Task Agnostic Continual Learning Using Online Variational Bayes**, (2018) by *Chen Zeno, Itay Golan, Elad Hoffer and Daniel Soudry* [[bib]](../bibtex.bib#L156-L164) 
- [**Overcoming Catastrophic Interference using Conceptor-Aided Backpropagation**](https://openreview.net/forum?id=B1al7jg0b) , (2018) by *Xu He and Herbert Jaeger* [[bib]](../bibtex.bib#L213-L220) 
- [**Overcoming Catastrophic Forgetting with Hard Attention to the Task**](http://proceedings.mlr.press/v80/serra18a.html) , (2018) by *Serra, Joan, Suris, Didac, Miron, Marius and Karatzoglou, Alexandros* [[bib]](../bibtex.bib#L230-L246) 
- **Riemannian Walk for Incremental Learning: Understanding Forgetting and Intransigence**, (2018) by *Chaudhry, Arslan, Dokania, Puneet K, Ajanthan, Thalaiyasingam and Torr, Philip HS* [[bib]](../bibtex.bib#L248-L254) 
- [**Memory Aware Synapses: Learning what (not) to forget**](http://arxiv.org/abs/1711.09601) , (2017) by *Rahaf Aljundi, Francesca Babiloni, Mohamed Elhoseiny, Marcus Rohrbach and Tinne Tuytelaars* [[bib]](../bibtex.bib#L256-L269) 
- [**Variational Continual Learning**](https://openreview.net/forum?id=BkQqq0gRb) , (2018) by *Cuong V. Nguyen, Yingzhen Li, Thang D. Bui and Richard E. Turner* [[bib]](../bibtex.bib#L271-L278) 
- [**Continual Learning Through Synaptic Intelligence**](http://proceedings.mlr.press/v70/zenke17a.html) , (2017) by *{Zenke}, Friedeman, {Poole}, Ben and {Ganguli}, Surya * [[bib]](../bibtex.bib#L280-L295) 
``` 
Synaptic Intelligence (SI). Importance of parameter measured based on their contribution to change in the loss. 
``` 
- [**Continual Learning with Bayesian Neural Networks for Non-Stationary Data**](https://openreview.net/forum?id=SJlsFpVtDB) , (2020) by *Richard Kurle, Botond Cseke, Alexej Klushyn, Patrick van der Smagt and Stephan Günnemann* [[bib]](../bibtex.bib#L417-L424) 
- **Progress \& compress: A scalable framework for continual learning**, (2018) by *Schwarz, Jonathan, Luketina, Jelena, Czarnecki, Wojciech M, Grabska-Barwinska, Agnieszka, Teh, Yee Whye, Pascanu, Razvan and Hadsell, Raia* [[bib]](../bibtex.bib#L641-L647) 
- **Functional Regularisation for Continual Learning with Gaussian Processes**, (2019) by *Titsias, Michalis K, Schwarz, Jonathan, Matthews, Alexander G de G, Pascanu, Razvan and Teh, Yee Whye* [[bib]](../bibtex.bib#L853-L859) 

## Distillation Methods
- **Learning without forgetting**, (2017) by *Li, Zhizhong and Hoiem, Derek* [[bib]](../bibtex.bib#L298-L305) 
- **Overcoming Catastrophic Forgetting With Unlabeled Data in the Wild**, (2019) by *Lee, Kibok, Lee, Kimin, Shin, Jinwoo and Lee, Honglak* [[bib]](../bibtex.bib#L560-L567) 
- **Large scale incremental learning**, (2019) by *Wu, Yue, Chen, Yinpeng, Wang, Lijuan, Ye, Yuancheng, Liu, Zicheng, Guo, Yandong and Fu, Yun* [[bib]](../bibtex.bib#L569-L576) 
- **Lifelong learning via progressive distillation and retrospection**, (2018) by *Hou, Saihui, Pan, Xinyu, Change Loy, Chen, Wang, Zilei and Lin, Dahua* [[bib]](../bibtex.bib#L578-L585) 
- **End-to-end incremental learning**, (2018) by *Castro, Francisco M, Mar{\'\i}n-Jim{\'e}nez, Manuel J, Guil, Nicol{\'a}s, Schmid, Cordelia and Alahari, Karteek* [[bib]](../bibtex.bib#L587-L594) 
- **icarl: Incremental classifier and representation learning**, (2017) by *Rebuffi, Sylvestre-Alvise, Kolesnikov, Alexander, Sperl, Georg and Lampert, Christoph H* [[bib]](../bibtex.bib#L596-L603) 

## Rehearsal Methods
- [**Efficient Lifelong Learning with {A-GEM}**](https://arxiv.org/abs/1812.00420) , (2019) by *Chaudhry, Arslan, Ranzato, Marc’Aurelio, Rohrbach, Marcus and Elhoseiny, Mohamed* [[bib]](../bibtex.bib#L21-L28) 
``` 
More efficient GEM; Introduces online continual learning
``` 
- [**Gradient Episodic Memory for Continual Learning**](http://papers.nips.cc/paper/7225-gradient-episodic-memory-for-continual-learning.pdf) , (2017) by *Lopez-Paz, David and Ranzato, Marc-Aurelio* [[bib]](../bibtex.bib#L42-L52) 
``` 
A model that alliviates CF via constrained optimization
``` 
- **Orthogonal Gradient Descent for Continual Learning**, (2019) by *Mehrdad Farajtabar, Navid Azizan, Alex Mott and Ang Li* [[bib]](../bibtex.bib#L342-L350) 
- [**Gradient based sample selection for online continual learning**](http://papers.nips.cc/paper/9354-gradient-based-sample-selection-for-online-continual-learning.pdf) , (2019) by *Aljundi, Rahaf, Lin, Min, Goujaud, Baptiste and Bengio, Yoshua* [[bib]](../bibtex.bib#L352-L362) 
- **Online Learned Continual Compression with Stacked Quantization Module**, (2019) by *Caccia, Lucas, Belilovsky, Eugene, Caccia, Massimo and Pineau, Joelle* [[bib]](../bibtex.bib#L376-L382) 
- **icarl: Incremental classifier and representation learning**, (2017) by *Rebuffi, Sylvestre-Alvise, Kolesnikov, Alexander, Sperl, Georg and Lampert, Christoph H* [[bib]](../bibtex.bib#L596-L603) 
- **Experience replay for continual learning**, (2019) by *Rolnick, David, Ahuja, Arun, Schwarz, Jonathan, Lillicrap, Timothy and Wayne, Gregory* [[bib]](../bibtex.bib#L950-L957) 

## Generative Replay Methods
- **Continual learning with deep generative replay**, (2017) by *Shin, Hanul, Lee, Jung Kwon, Kim, Jaehong and Kim, Jiwon* [[bib]](../bibtex.bib#L56-L63) 
``` 
Introduces generative replay
``` 
- [**{Generative Models from the perspective of Continual Learning}**](https://hal.archives-ouvertes.fr/hal-01951954) , (2019) by *Lesort, Timoth{\'e}e, Caselles-Dupr{\'e}, Hugo, Garcia-Ortiz, Michael, Goudou, Jean-Fran{\c c}ois and Filliat, David* [[bib]](../bibtex.bib#L475-L487) 
- **Marginal replay vs conditional replay for continual learning**, (2019) by *Lesort, Timoth{\'e}e, Gepperth, Alexander, Stoian, Andrei and Filliat, David* [[bib]](../bibtex.bib#L902-L910) 

## Dynamic Architectures or Routing Methods
- **A Neural Dirichlet Process Mixture Model for Task-Free Continual Learning**, (2020) by *Lee, Soochan, Ha, Junsoo, Zhang, Dongsu and Kim, Gunhee* [[bib]](../bibtex.bib#L126-L132) 
- **Continual Learning with Adaptive Weights (CLAW)**, (2019) by *Adel, Tameem, Zhao, Han and Turner, Richard E* [[bib]](../bibtex.bib#L166-L172) 
- [**{ORACLE:} Order Robust Adaptive Continual LEarning**](http://arxiv.org/abs/1902.09432) , (2019) by *Jaehong Yoon and
Saehoon Kim and
Eunho Yang and
Sung Ju Hwang* [[bib]](../bibtex.bib#L174-L190) 
- [**Random Path Selection for Incremental Learning**](http://arxiv.org/abs/1906.01120) , (2019) by *Jathushan Rajasegaran and
Munawar Hayat and
Salman H. Khan and
Fahad Shahbaz Khan and
Ling Shao* [[bib]](../bibtex.bib#L192-L209) 
- [**Incremental Learning through Deep Adaptation**](https://openreview.net/forum?id=ryj0790hb) , (2018) by *Amir Rosenfeld and John K. Tsotsos* [[bib]](../bibtex.bib#L318-L324) 
- **{Progressive Neural Networks}**, (2016) by *{Rusu}, A.~A., {Rabinowitz}, N.~C., {Desjardins}, G., 
{Soyer}, H., {Kirkpatrick}, J., {Kavukcuoglu}, K., 
{Pascanu}, R. and {Hadsell}, R.* [[bib]](../bibtex.bib#L326-L340) 

## Hybrid Methods
- **Compacting, Picking and Growing for Unforgetting Continual Learning**, (2019) by *Hung, Ching-Yi, Tu, Cheng-Hao, Wu, Cheng-En, Chen, Chien-Hung, Chan, Yi-Ming and Chen, Chu-Song* [[bib]](../bibtex.bib#L107-L114) 
- [**Continual learning with hypernetworks**](https://openreview.net/forum?id=SJgwNerKvB) , (2020) by *Anonymous* [[bib]](../bibtex.bib#L516-L524) 

## Meta Continual Learning
- [**Meta-Learning Representations for Continual Learning**](http://papers.nips.cc/paper/8458-meta-learning-representations-for-continual-learning.pdf) , (2019) by *Javed, Khurram and White, Martha* [[bib]](../bibtex.bib#L394-L404) 
- **Learning from the Past: Continual Meta-Learning via Bayesian Graph Modeling**, (2019) by *Yadan Luo, Zi Huang, Zheng Zhang, Ziwei Wang, Mahsa Baktashmotlagh and Yang Yang* [[bib]](../bibtex.bib#L406-L414) 
- [**Online Meta-Learning**](http://proceedings.mlr.press/v97/finn19a.html) , (2019) by *Finn, Chelsea, Rajeswaran, Aravind, Kakade, Sham and Levine, Sergey* [[bib]](../bibtex.bib#L426-L441) 
- [**Reconciling meta-learning and continual learning with online mixtures of tasks**](http://papers.nips.cc/paper/9112-reconciling-meta-learning-and-continual-learning-with-online-mixtures-of-tasks.pdf) , (2019) by *Jerfel, Ghassen, Grant, Erin, Griffiths, Tom and Heller, Katherine A* [[bib]](../bibtex.bib#L443-L453) 
- [**Deep Online Learning Via Meta-Learning: Continual Adaptation for Model-Based {RL}**](https://openreview.net/forum?id=HyxAfnA5tm) , (2019) by *Anusha Nagabandi, Chelsea Finn and Sergey Levine* [[bib]](../bibtex.bib#L456-L463) 
- **Task Agnostic Continual Learning via Meta Learning**, (2019) by *Xu He, Jakub Sygnowski, Alexandre Galashov, Andrei A. Rusu, Yee Whye Teh and Razvan Pascanu* [[bib]](../bibtex.bib#L534-L541) 
- **Learning to Continually Learn**, (2020) by *Beaulieu, Shawn, Frati, Lapo, Miconi, Thomas, Lehman, Joel, Stanley, Kenneth O, Clune, Jeff and Cheney, Nick* [[bib]](../bibtex.bib#L925-L931) 
- **Meta-learnt priors slow down catastrophic forgetting in neural networks**, (2019) by *Spigler, Giacomo* [[bib]](../bibtex.bib#L933-L939) 
- **Learning to learn without forgetting by maximizing transfer and minimizing interference**, (2018) by *Riemer, Matthew, Cases, Ignacio, Ajemian, Robert, Liu, Miao, Rish, Irina, Tu, Yuhai and Tesauro, Gerald* [[bib]](../bibtex.bib#L942-L948) 

## Lifelong Reinforcement Learning
- [**Continual learning for robotics: Definition, framework, learning strategies, opportunities and challenges**](http://www.sciencedirect.com/science/article/pii/S1566253519307377) , (2020) by *Timothée Lesort, Vincenzo Lomonaco, Andrei Stoian, Davide Maltoni, David Filliat and Natalia Díaz-Rodríguez* [[bib]](../bibtex.bib#L823-L835) 
``` 
Extensive review of CL methods and their applications in robotics and framework proposition for continual learning
``` 
- **Experience replay for continual learning**, (2019) by *Rolnick, David, Ahuja, Arun, Schwarz, Jonathan, Lillicrap, Timothy and Wayne, Gregory* [[bib]](../bibtex.bib#L950-L957) 

## Continual Generative Modeling
- **Continual learning with deep generative replay**, (2017) by *Shin, Hanul, Lee, Jung Kwon, Kim, Jaehong and Kim, Jiwon* [[bib]](../bibtex.bib#L56-L63) 
``` 
Introduces generative replay
``` 
- **Continual Unsupervised Representation Learning**, (2019) by *Dushyant Rao, Francesco Visin, Andrei A. Rusu, Yee Whye Teh, Razvan Pascanu and Raia Hadsell* [[bib]](../bibtex.bib#L465-L473) 
- [**{Generative Models from the perspective of Continual Learning}**](https://hal.archives-ouvertes.fr/hal-01951954) , (2019) by *Lesort, Timoth{\'e}e, Caselles-Dupr{\'e}, Hugo, Garcia-Ortiz, Michael, Goudou, Jean-Fran{\c c}ois and Filliat, David* [[bib]](../bibtex.bib#L475-L487) 
- **Lifelong Generative Modeling**, (2017) by *Ramapuram, Jason, Gregorova, Magda and Kalousis, Alexandros* [[bib]](../bibtex.bib#L489-L495) 
- **Marginal replay vs conditional replay for continual learning**, (2019) by *Lesort, Timoth{\'e}e, Gepperth, Alexander, Stoian, Andrei and Filliat, David* [[bib]](../bibtex.bib#L902-L910) 
