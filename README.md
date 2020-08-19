# Continual Learning Literature 
This repository is maintained by Massimo Caccia and Timothée Lesort don't hesitate to send us an email to collaborate or fix some entries ({massimo.p.caccia , t.lesort} at gmail.com). The automation script of this repo is adapted from [Automatic_Awesome_Bibliography](https://github.com/TLESORT/Automatic_Awesome_Bibliography).

 For contributing to the repository please follow the process [here](https://github.com/optimass/continual_learning_papers/blob/master/scripts/README.md) 

## Outline 
- [Classics](https://github.com/optimass/continual_learning_papers/blob/master/README.md#classics)
- [Surveys](https://github.com/optimass/continual_learning_papers/blob/master/README.md#surveys)
- [Influentials](https://github.com/optimass/continual_learning_papers/blob/master/README.md#influentials)
- [New Settings or Metrics](https://github.com/optimass/continual_learning_papers/blob/master/README.md#new-settings-or-metrics)
- [Regularization Methods](https://github.com/optimass/continual_learning_papers/blob/master/README.md#regularization-methods)
- [Distillation Methods](https://github.com/optimass/continual_learning_papers/blob/master/README.md#distillation-methods)
- [Rehearsal Methods](https://github.com/optimass/continual_learning_papers/blob/master/README.md#rehearsal-methods)
- [Generative Replay Methods](https://github.com/optimass/continual_learning_papers/blob/master/README.md#generative-replay-methods)
- [Dynamic Architectures or Routing Methods](https://github.com/optimass/continual_learning_papers/blob/master/README.md#dynamic-architectures-or-routing-methods)
- [Hybrid Methods](https://github.com/optimass/continual_learning_papers/blob/master/README.md#hybrid-methods)
- [Continual Few-Shot Learning](https://github.com/optimass/continual_learning_papers/blob/master/README.md#continual-few-shot-learning)
- [Meta-Continual Learning](https://github.com/optimass/continual_learning_papers/blob/master/README.md#meta-continual-learning)
- [Lifelong Reinforcement Learning](https://github.com/optimass/continual_learning_papers/blob/master/README.md#lifelong-reinforcement-learning)
- [Continual Generative Modeling](https://github.com/optimass/continual_learning_papers/blob/master/README.md#continual-generative-modeling)
- [Applications](https://github.com/optimass/continual_learning_papers/blob/master/README.md#applications)
- [Thesis](https://github.com/optimass/continual_learning_papers/blob/master/README.md#thesis)
- [Workshops](https://github.com/optimass/continual_learning_papers/blob/master/README.md#workshops)

## Classics
- [**Catastrophic forgetting in connectionist networks**](https://www.sciencedirect.com/science/article/abs/pii/S1364661399012942) , (1999) by *French, Robert M.* [[bib]](bibtex.bib#L1053-L1067) 
- [**Lifelong robot learning**](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.71.3723&rep=rep1&type=pdf) , (1995) by *Thrun, Sebastian and Mitchell, Tom M* [[bib]](bibtex.bib#L119-L128) 
``` 
Argues knowledge transfer is essential if robots are to learn control with moderate learning times
``` 
- [**Catastrophic interference in connectionist networks: The sequential learning problem**](https://www.sciencedirect.com/science/article/pii/S0079742108605368) , (1989) by *McCloskey, Michael and Cohen, Neal J* [[bib]](bibtex.bib#L723-L733) 
``` 
Introduces CL and reveals the catastrophic forgetting problem
``` 

## Surveys
- [**Continual learning for robotics: Definition, framework, learning strategies, opportunities and challenges**](http://www.sciencedirect.com/science/article/pii/S1566253519307377) , (2020) by *Timothée Lesort, Vincenzo Lomonaco, Andrei Stoian, Davide Maltoni, David Filliat and Natalia Díaz-Rodríguez* [[bib]](bibtex.bib#L1039-L1050) 
- [**Continual learning: A comparative study on how to defy forgetting in classification tasks**](https://arxiv.org/abs/1909.08383) , (2019) by *Matthias De Lange, Rahaf Aljundi, Marc Masana, Sarah Parisot, Xu Jia, Ales Leonardis, Gregory Slabaugh and Tinne Tuytelaars* [[bib]](bibtex.bib#L204-L213) 
``` 
Extensive empirical study of CL methods (in the multi-head setting)
``` 
- [**Continual lifelong learning with neural networks: A review**](http://www.sciencedirect.com/science/article/pii/S0893608019300231) , (2019) by *German I. Parisi, Ronald Kemker, Jose L. Part, Christopher Kanan and Stefan Wermter* [[bib]](bibtex.bib#L216-L227) 
``` 
An extensive review of CL
``` 
- [**Three scenarios for continual learning**](https://arxiv.org/abs/1904.07734) , (2019) by *van de Ven, Gido M and Tolias, Andreas S* [[bib]](bibtex.bib#L755-L762) 
``` 
An extensive review of CL methods in three different scenarios (task-, domain-, and class-incremental learning)
``` 
- [**Born to learn: The inspiration, progress, and future of evolved plastic artificial neural networks**](http://www.sciencedirect.com/science/article/pii/S0893608018302120) , (2018) by *Andrea Soltoggio, Kenneth O. Stanley and Sebastian Risi* [[bib]](bibtex.bib#L898-L909) 
``` 
 
``` 

## Influentials
- [**Efficient Lifelong Learning with A-GEM**](https://arxiv.org/abs/1812.00420) , (2019) by *Chaudhry, Arslan, Ranzato, Marc’Aurelio, Rohrbach, Marcus and Elhoseiny, Mohamed* [[bib]](bibtex.bib#L141-L148) 
``` 
More efficient GEM; Introduces online continual learning
``` 
- [**Towards Robust Evaluations of Continual Learning**](https://arxiv.org/abs/1805.09733) , (2018) by *Farquhar, Sebastian and Gal, Yarin* [[bib]](bibtex.bib#L131-L138) 
``` 
Proposes desideratas and reexamines the evaluation protocol
``` 
- [**Continual Learning in Practice**](https://arxiv.org/abs/1903.05202) , (2018) by *Diethe, Tom, Borchert, Tom, Thereska, Eno, Pigem, Borja de Balle and Lawrence, Neil* [[bib]](bibtex.bib#L1978-L1985) 
``` 
Proposes a reference architecture for a continual learning system
``` 
- [**Overcoming catastrophic forgetting in neural networks**](https://www.pnas.org/content/pnas/114/13/3521.full.pdf) , (2017) by *Kirkpatrick, James, Pascanu, Razvan, Rabinowitz, Neil, Veness, Joel, Desjardins, Guillaume, Rusu, Andrei A, Milan, Kieran, Quan, John, Ramalho, Tiago, Grabska-Barwinska, Agnieszka and others* [[bib]](bibtex.bib#L151-L159) 
- [**Gradient Episodic Memory for Continual Learning**](http://papers.nips.cc/paper/7225-gradient-episodic-memory-for-continual-learning.pdf) , (2017) by *Lopez-Paz, David and Ranzato, Marc-Aurelio* [[bib]](bibtex.bib#L163-L173) 
``` 
A model that alliviates CF via constrained optimization
``` 
- [**Continual learning with deep generative replay**](https://arxiv.org/abs/1705.08690) , (2017) by *Shin, Hanul, Lee, Jung Kwon, Kim, Jaehong and Kim, Jiwon* [[bib]](bibtex.bib#L177-L185) 
``` 
Introduces generative replay
``` 
- [**An Empirical Investigation of Catastrophic Forgetting in Gradient-Based Neural Networks**](https://arxiv.org/abs/1312.6211) , (2013) by *Goodfellow, I.~J., Mirza, M., Xiao, D., Courville, A. and Bengio, Y.* [[bib]](bibtex.bib#L188-L201) 
``` 
Investigates CF in neural networks
``` 

## New Settings or Metrics
- [**Wandering Within a World: Online Contextualized Few-Shot Learning**](https://arxiv.org/abs/2007.04546) , (2020) by *Mengye Ren, Michael L. Iuzzolino, Michael C. Mozer and Richard S. Zemel* [[bib]](bibtex.bib#L21-L29) 
``` 
proposes a new continual few-shot setting where spacial and temporal context can be leveraged to and unseen classes need to be predicted
``` 
- [**Defining Benchmarks for Continual Few-Shot Learning**](https://arxiv.org/abs/2004.11967) , (2020) by *Antoniou, Antreas, Patacchiola, Massimiliano, Ochal, Mateusz and Storkey, Amos* [[bib]](bibtex.bib#L63-L70) 
``` 
(title is a good enough summary)
``` 
- [**Online Fast Adaptation and Knowledge Accumulation: a New Approach to Continual Learning**](https://arxiv.org/abs/2003.05856) , (2020) by *Caccia, Massimo, Rodriguez, Pau, Ostapenko, Oleksiy, Normandin, Fabrice, Lin, Min, Caccia, Lucas, Laradji, Issam, Rish, Irina, Lacoste, Alexandre, Vazquez, David and others* [[bib]](bibtex.bib#L1191-L1198) 
``` 
Proposes a new approach to CL evaluation more aligned with real-life applications, bringing CL closer to Online Learning and Open-World learning
``` 
- [**Compositional Language Continual Learning**](https://openreview.net/forum?id=rklnDgHtDS) , (2020) by *Yuanpeng Li, Liang Zhao, Kenneth Church and Mohamed Elhoseiny* [[bib]](bibtex.bib#L1232-L1238) 
``` 
method for compositional continual learning of sequence-to-sequence models
``` 

## Regularization Methods
- [**Continual Learning with Bayesian Neural Networks for Non-Stationary Data**](https://openreview.net/forum?id=SJlsFpVtDB) , (2020) by *Richard Kurle, Botond Cseke, Alexej Klushyn, Patrick van der Smagt and Stephan Günnemann* [[bib]](bibtex.bib#L603-L610) 
``` 
continual learning for non-stationary data using Bayesian neural networks and memory-based online variational Bayes
``` 
- [**Improving and Understanding Variational Continual Learning**](https://arxiv.org/abs/1905.02099) , (2019) by *Siddharth Swaroop, Cuong V. Nguyen, Thang D. Bui and Richard E. Turner* [[bib]](bibtex.bib#L241-L249) 
``` 
Improved results and interpretation of VCL.
``` 
- [**Uncertainty-based Continual Learning with Adaptive Regularization**](http://papers.nips.cc/paper/8690-uncertainty-based-continual-learning-with-adaptive-regularization.pdf) , (2019) by *Ahn, Hongjoon, Cha, Sungmin, Lee, Donggyu and Moon, Taesup* [[bib]](bibtex.bib#L262-L272) 
``` 
Introduces VCL with uncertainty measured for neurons instead of weights.
``` 
- [**Functional Regularisation for Continual Learning with Gaussian Processes**](https://arxiv.org/abs/1901.11356) , (2019) by *Titsias, Michalis K, Schwarz, Jonathan, Matthews, Alexander G de G, Pascanu, Razvan and Teh, Yee Whye* [[bib]](bibtex.bib#L1069-L1076) 
``` 
functional regularisation for Continual Learning: avoids forgetting a previous task by constructing and memorising an approximate posterior belief over the underlying task-specific function
``` 
- [**Task Agnostic Continual Learning Using Online Variational Bayes**](https://arxiv.org/pdf/1803.10123.pdf) , (2018) by *Chen Zeno, Itay Golan, Elad Hoffer and Daniel Soudry* [[bib]](bibtex.bib#L275-L284) 
``` 
Introduces an optimizer for CL that relies on closed form updates of mu and sigma of BNN; introduce label trick for class learning (single-head)
``` 
- [**Overcoming Catastrophic Interference using Conceptor-Aided Backpropagation**](https://openreview.net/forum?id=B1al7jg0b) , (2018) by *Xu He and Herbert Jaeger* [[bib]](bibtex.bib#L331-L338) 
``` 
Conceptor-Aided Backprop (CAB): gradients are shielded by conceptors against degradation of previously learned tasks
``` 
- [**Riemannian Walk for Incremental Learning: Understanding Forgetting and Intransigence**](https://arxiv.org/abs/1801.10112) , (2018) by *Chaudhry, Arslan, Dokania, Puneet K, Ajanthan, Thalaiyasingam and Torr, Philip HS* [[bib]](bibtex.bib#L376-L383) 
``` 
Formalizes the shortcomings of multi-head evaluation, as well as the importance of replay in single-head setup. Presenting an improved version of EWC.
``` 
- [**Variational Continual Learning**](https://arxiv.org/abs/1710.10628) , (2018) by *Cuong V. Nguyen, Yingzhen Li, Thang D. Bui and Richard E. Turner* [[bib]](bibtex.bib#L407-L414) 
- [**Progress \& compress: A scalable framework for continual learning**](https://arxiv.org/abs/1805.06370) , (2018) by *Schwarz, Jonathan, Luketina, Jelena, Czarnecki, Wojciech M, Grabska-Barwinska, Agnieszka, Teh, Yee Whye, Pascanu, Razvan and Hadsell, Raia* [[bib]](bibtex.bib#L418-L425) 
``` 
A new P\&C architecture; online EWC for keeping the knowledge about the previous task, knowledge for keeping the knowledge about the current task (Multi-head setting, RL)
``` 
- [**Facilitating Bayesian Continual Learning by Natural Gradients and Stein Gradients**](https://arxiv.org/abs/1904.10644) , (2018) by *Chen, Yu, Diethe, Tom and Lawrence, Neil* [[bib]](bibtex.bib#L1988-L1995) 
``` 
Improves on VCL
``` 
- [**Overcoming catastrophic forgetting in neural networks**](https://www.pnas.org/content/pnas/114/13/3521.full.pdf) , (2017) by *Kirkpatrick, James, Pascanu, Razvan, Rabinowitz, Neil, Veness, Joel, Desjardins, Guillaume, Rusu, Andrei A, Milan, Kieran, Quan, John, Ramalho, Tiago, Grabska-Barwinska, Agnieszka and others* [[bib]](bibtex.bib#L151-L159) 
- [**Memory Aware Synapses: Learning what (not) to forget**](http://arxiv.org/abs/1711.09601) , (2017) by *Rahaf Aljundi, Francesca Babiloni, Mohamed Elhoseiny, Marcus Rohrbach and Tinne Tuytelaars* [[bib]](bibtex.bib#L389-L402) 
``` 
Importance of parameter measured based on their contribution to change in the learned prediction function
``` 
- [**Continual Learning Through Synaptic Intelligence**](http://proceedings.mlr.press/v70/zenke17a.html) , (2017) by *Zenke, Friedeman, Poole, Ben and Ganguli, Surya * [[bib]](bibtex.bib#L428-L443) 
``` 
Synaptic Intelligence (SI). Importance of parameter measured based on their contribution to change in the loss. 
``` 

## Distillation Methods
- [**Overcoming Catastrophic Forgetting With Unlabeled Data in the Wild**](https://arxiv.org/abs/1903.12648) , (2019) by *Lee, Kibok, Lee, Kimin, Shin, Jinwoo and Lee, Honglak* [[bib]](bibtex.bib#L765-L773) 
``` 
Introducing global distillation loss and balanced finetuning; leveraging unlabeled data in the open world setting (Single-head setting)
``` 
- [**Large scale incremental learning**](https://arxiv.org/abs/1905.13260) , (2019) by *Wu, Yue, Chen, Yinpeng, Wang, Lijuan, Ye, Yuancheng, Liu, Zicheng, Guo, Yandong and Fu, Yun* [[bib]](bibtex.bib#L776-L784) 
``` 
Introducing bias parameters to the last fully connected layer to resolve the data imbalance issue (Single-head setting)
``` 
- [**Lifelong learning via progressive distillation and retrospection**](https://arxiv.org/abs/1905.13260) , (2018) by *Hou, Saihui, Pan, Xinyu, Change Loy, Chen, Wang, Zilei and Lin, Dahua* [[bib]](bibtex.bib#L787-L795) 
``` 
Introducing an expert of the current task in the knowledge distillation method (Multi-head setting)
``` 
- [**End-to-end incremental learning**](https://arxiv.org/abs/1807.09536) , (2018) by *Castro, Francisco M, Marin-Jimenez, Manuel J, Guil, Nicolas, Schmid, Cordelia and Alahari, Karteek* [[bib]](bibtex.bib#L798-L806) 
``` 
Finetuning the last fully connected layer with a balanced dataset to resolve the data imbalance issue (Single-head setting)
``` 
- [**Learning without forgetting**](https://arxiv.org/abs/1606.09282) , (2017) by *Li, Zhizhong and Hoiem, Derek* [[bib]](bibtex.bib#L446-L454) 
``` 
Functional regularization through distillation (keeping the output of the updated network on the new data close to the output of the old network on the new data)
``` 
- [**icarl: Incremental classifier and representation learning**](https://arxiv.org/abs/1611.07725) , (2017) by *Rebuffi, Sylvestre-Alvise, Kolesnikov, Alexander, Sperl, Georg and Lampert, Christoph H* [[bib]](bibtex.bib#L809-L817) 
``` 
Binary cross-entropy loss for representation learning & exemplar memory (or coreset) for replay (Single-head setting)
``` 

## Rehearsal Methods
- [**Efficient Lifelong Learning with A-GEM**](https://arxiv.org/abs/1812.00420) , (2019) by *Chaudhry, Arslan, Ranzato, Marc’Aurelio, Rohrbach, Marcus and Elhoseiny, Mohamed* [[bib]](bibtex.bib#L141-L148) 
``` 
More efficient GEM; Introduces online continual learning
``` 
- [**Orthogonal Gradient Descent for Continual Learning**](https://arxiv.org/abs/1910.07104) , (2019) by *Mehrdad Farajtabar, Navid Azizan, Alex Mott and Ang Li* [[bib]](bibtex.bib#L515-L524) 
``` 
projecting the gradients from new tasks onto a subspace in which the neural network output on previous task does not change and the projected gradient is still in a useful direction for learning the new task
``` 
- [**Gradient based sample selection for online continual learning**](http://papers.nips.cc/paper/9354-gradient-based-sample-selection-for-online-continual-learning.pdf) , (2019) by *Aljundi, Rahaf, Lin, Min, Goujaud, Baptiste and Bengio, Yoshua* [[bib]](bibtex.bib#L528-L538) 
``` 
sample selection as a constraint reduction problem based on the constrained optimization view of continual learning
``` 
- [**Online Continual Learning with Maximal Interfered Retrieval**](http://papers.nips.cc/paper/9357-online-continual-learning-with-maximal-interfered-retrieval.pdf) , (2019) by *Aljundi, Rahaf, Caccia, Lucas, Belilovsky, Eugene, Caccia, Massimo, Lin, Min, Charlin, Laurent and Tuytelaars, Tinne* [[bib]](bibtex.bib#L542-L552) 
``` 
Controlled sampling of memories for replay to automatically rehearse on tasks currently undergoing the most forgetting
``` 
- [**Online Learned Continual Compression with Adaptative Quantization Module**](https://arxiv.org/abs/1911.08019) , (2019) by *Caccia, Lucas, Belilovsky, Eugene, Caccia, Massimo and Pineau, Joelle* [[bib]](bibtex.bib#L556-L563) 
``` 
Uses stacks of VQ-VAE modules to progressively compress the data stream, enabling better rehearsal
``` 
- [**Experience replay for continual learning**](https://arxiv.org/abs/1811.11682) , (2019) by *Rolnick, David, Ahuja, Arun, Schwarz, Jonathan, Lillicrap, Timothy and Wayne, Gregory* [[bib]](bibtex.bib#L1179-L1187) 
- [**Gradient Episodic Memory for Continual Learning**](http://papers.nips.cc/paper/7225-gradient-episodic-memory-for-continual-learning.pdf) , (2017) by *Lopez-Paz, David and Ranzato, Marc-Aurelio* [[bib]](bibtex.bib#L163-L173) 
``` 
A model that alliviates CF via constrained optimization
``` 
- [**icarl: Incremental classifier and representation learning**](https://arxiv.org/abs/1611.07725) , (2017) by *Rebuffi, Sylvestre-Alvise, Kolesnikov, Alexander, Sperl, Georg and Lampert, Christoph H* [[bib]](bibtex.bib#L809-L817) 
``` 
Binary cross-entropy loss for representation learning & exemplar memory (or coreset) for replay (Single-head setting)
``` 

## Generative Replay Methods
- [**Brain-Like Replay For Continual Learning With Artificial Neural Networks**](https://baicsworkshop.github.io/pdf/BAICS_8.pdf) , (2020) by *van de Ven, Gido M, Siegelmann, Hava T and Tolias, Andreas S* [[bib]](bibtex.bib#L111-L117) 
- [**Learning to remember: A synaptic plasticity driven framework for continual learning**](https://openaccess.thecvf.com/content_CVPR_2019/html/Ostapenko_Learning_to_Remember_A_Synaptic_Plasticity_Driven_Framework_for_Continual_CVPR_2019_paper.html) , (2019) by *Ostapenko, Oleksiy, Puscas, Mihai, Klein, Tassilo, Jahnichen, Patrick and Nabi, Moin* [[bib]](bibtex.bib#L1-L9) 
``` 
introdudes Dynamic generative memory (DGM) which relies on conditional generative adversarial networks with learnable connection plasticity realized with neural masking
``` 
- [**Generative Models from the perspective of Continual Learning**](https://hal.archives-ouvertes.fr/hal-01951954) , (2019) by *Lesort, Timoth{\'e}e, Caselles-Dupr{\'e}, Hugo, Garcia-Ortiz, Michael, Goudou, Jean-Fran{\c c}ois and Filliat, David* [[bib]](bibtex.bib#L669-L681) 
``` 
Extensive evaluation of CL methods for generative modeling
``` 
- [**Marginal replay vs conditional replay for continual learning**](https://arxiv.org/abs/1810.12069) , (2019) by *Lesort, Timoth{\'e}e, Gepperth, Alexander, Stoian, Andrei and Filliat, David* [[bib]](bibtex.bib#L1124-L1133) 
``` 
Extensive evaluation of generative replay methods
``` 
- [**Generative replay with feedback connections as a general strategy for continual learning**](https://arxiv.org/abs/1809.10635) , (2018) by *Michiel van der Ven and Andreas S. Tolias* [[bib]](bibtex.bib#L567-L575) 
``` 
smarter Generative Replay
``` 
- [**Continual learning with deep generative replay**](https://arxiv.org/abs/1705.08690) , (2017) by *Shin, Hanul, Lee, Jung Kwon, Kim, Jaehong and Kim, Jiwon* [[bib]](bibtex.bib#L177-L185) 
``` 
Introduces generative replay
``` 

## Dynamic Architectures or Routing Methods
- [**ORACLE: Order Robust Adaptive Continual Learning**](http://arxiv.org/abs/1902.09432) , (2019) by *Jaehong Yoon and
Saehoon Kim and
Eunho Yang and
Sung Ju Hwang* [[bib]](bibtex.bib#L287-L303) 
- [**Random Path Selection for Incremental Learning**](http://arxiv.org/abs/1906.01120) , (2019) by *Jathushan Rajasegaran and
Munawar Hayat and
Salman H. Khan and
Fahad Shahbaz Khan and
Ling Shao* [[bib]](bibtex.bib#L308-L325) 
``` 
Proposes a random path selection algorithm, called RPSnet, that progressively chooses optimal paths for the new tasks while encouraging parameter sharing and reuse
``` 
- [**Incremental Learning through Deep Adaptation**](https://openreview.net/forum?id=ryj0790hb) , (2018) by *Amir Rosenfeld and John K. Tsotsos* [[bib]](bibtex.bib#L469-L475) 
- [**Continual Learning in Practice**](https://arxiv.org/abs/1903.05202) , (2018) by *Diethe, Tom, Borchert, Tom, Thereska, Eno, Pigem, Borja de Balle and Lawrence, Neil* [[bib]](bibtex.bib#L1978-L1985) 
``` 
Proposes a reference architecture for a continual learning system
``` 
- [**Progressive Neural Networks**](https://arxiv.org/abs/1606.04671) , (2016) by *{Rusu}, A.~A., {Rabinowitz}, N.~C., {Desjardins}, G., 
{Soyer}, H., {Kirkpatrick}, J., {Kavukcuoglu}, K., 
{Pascanu}, R. and {Hadsell}, R.* [[bib]](bibtex.bib#L477-L492) 
``` 
Each task have a specific model connected to the previous ones
``` 

## Hybrid Methods
- [**Continual learning with hypernetworks**](https://openreview.net/forum?id=SJgwNerKvB) , (2020) by *Johannes von Oswald, Christian Henning, João Sacramento and Benjamin F. Grewe* [[bib]](bibtex.bib#L713-L720) 
``` 
Learning task-conditioned hypernetworks for continual learning as well as task embeddings; hypernetwors offers good model compression.
``` 
- [**Compacting, Picking and Growing for Unforgetting Continual Learning**](https://arxiv.org/abs/1910.06562) , (2019) by *Hung, Ching-Yi, Tu, Cheng-Hao, Wu, Cheng-En, Chen, Chien-Hung, Chan, Yi-Ming and Chen, Chu-Song* [[bib]](bibtex.bib#L230-L238) 
``` 
Approach leverages the principles of deep model compression, critical weights selection, and progressive networks expansion. All enforced in an iterative manner
``` 

## Continual Few-Shot Learning
- [**Wandering Within a World: Online Contextualized Few-Shot Learning**](https://arxiv.org/abs/2007.04546) , (2020) by *Mengye Ren, Michael L. Iuzzolino, Michael C. Mozer and Richard S. Zemel* [[bib]](bibtex.bib#L21-L29) 
``` 
proposes a new continual few-shot setting where spacial and temporal context can be leveraged to and unseen classes need to be predicted
``` 
- [**Defining Benchmarks for Continual Few-Shot Learning**](https://arxiv.org/abs/2004.11967) , (2020) by *Antoniou, Antreas, Patacchiola, Massimiliano, Ochal, Mateusz and Storkey, Amos* [[bib]](bibtex.bib#L63-L70) 
``` 
(title is a good enough summary)
``` 
- [**Online Fast Adaptation and Knowledge Accumulation: a New Approach to Continual Learning**](https://arxiv.org/abs/2003.05856) , (2020) by *Caccia, Massimo, Rodriguez, Pau, Ostapenko, Oleksiy, Normandin, Fabrice, Lin, Min, Caccia, Lucas, Laradji, Issam, Rish, Irina, Lacoste, Alexandre, Vazquez, David and others* [[bib]](bibtex.bib#L1191-L1198) 
``` 
Proposes a new approach to CL evaluation more aligned with real-life applications, bringing CL closer to Online Learning and Open-World learning
``` 
- [**Learning from the Past: Continual Meta-Learning via Bayesian Graph Modeling**](https://arxiv.org/abs/1911.04695) , (2019) by *Yadan Luo, Zi Huang, Zheng Zhang, Ziwei Wang, Mahsa Baktashmotlagh and Yang Yang* [[bib]](bibtex.bib#L591-L600) 
- [**Online Meta-Learning**](http://proceedings.mlr.press/v97/finn19a.html) , (2019) by *Finn, Chelsea, Rajeswaran, Aravind, Kakade, Sham and Levine, Sergey* [[bib]](bibtex.bib#L613-L628) 
``` 
defines Online Meta-learning; propsoses Follow the Meta Leader (FTML) (~ Online MAML)
``` 
- [**Reconciling meta-learning and continual learning with online mixtures of tasks**](http://papers.nips.cc/paper/9112-reconciling-meta-learning-and-continual-learning-with-online-mixtures-of-tasks.pdf) , (2019) by *Jerfel, Ghassen, Grant, Erin, Griffiths, Tom and Heller, Katherine A* [[bib]](bibtex.bib#L632-L642) 
``` 
Meta-learns a tasks structure; continual adaptation via non-parametric prior
``` 
- [**Deep Online Learning Via Meta-Learning: Continual Adaptation for Model-Based RL**](https://openreview.net/forum?id=HyxAfnA5tm) , (2019) by *Anusha Nagabandi, Chelsea Finn and Sergey Levine* [[bib]](bibtex.bib#L647-L654) 
``` 
Formulates an online learning procedure that uses SGD to update model parameters, and an EM with a Chinese restaurant process prior to develop and maintain a mixture of models to handle non-stationary task distribution
``` 
- [**Task Agnostic Continual Learning via Meta Learning**](https://arxiv.org/abs/1906.05201) , (2019) by *Xu He, Jakub Sygnowski, Alexandre Galashov, Andrei A. Rusu, Yee Whye Teh and Razvan Pascanu* [[bib]](bibtex.bib#L736-L744) 
``` 
Introduces What & How framework; enables Task Agnostic CL with meta learned task inference
``` 

## Meta-Continual Learning
- [**La-MAML: Look-ahead Meta Learning for Continual Learning**](https://arxiv.org/abs/2007.13904) , (2020) by *Gunshi Gupta, Karmesh Yadav and Liam Paull* [[bib]](bibtex.bib#L12-L18) 
``` 
Proposes an online replay-based meta-continual learning algorithm with learning-rate modulation to mitigate catastrophic forgetting
``` 
- [**Learning to Continually Learn**](https://arxiv.org/abs/2002.09571) , (2020) by *Beaulieu, Shawn, Frati, Lapo, Miconi, Thomas, Lehman, Joel, Stanley, Kenneth O, Clune, Jeff and Cheney, Nick* [[bib]](bibtex.bib#L1149-L1156) 
``` 
Follow-up of OML. Meta-learns an activation-gating function instead.
``` 
- [**Meta-Learning Representations for Continual Learning**](http://papers.nips.cc/paper/8458-meta-learning-representations-for-continual-learning.pdf) , (2019) by *Javed, Khurram and White, Martha* [[bib]](bibtex.bib#L578-L588) 
``` 
Introduces Learns how to continually learn (OML) i.e. learns how to do online updates without forgetting.
``` 
- [**Meta-learnt priors slow down catastrophic forgetting in neural networks**](https://arxiv.org/pdf/1909.04170.pdf) , (2019) by *Spigler, Giacomo* [[bib]](bibtex.bib#L1159-L1166) 
``` 
Learning MAML in a Meta continual learning way slows down forgetting
``` 
- [**Learning to learn without forgetting by maximizing transfer and minimizing interference**](https://arxiv.org/abs/1810.11910) , (2018) by *Riemer, Matthew, Cases, Ignacio, Ajemian, Robert, Liu, Miao, Rish, Irina, Tu, Yuhai and Tesauro, Gerald* [[bib]](bibtex.bib#L1170-L1177) 

## Lifelong Reinforcement Learning
- [**Continual learning for robotics: Definition, framework, learning strategies, opportunities and challenges**](http://www.sciencedirect.com/science/article/pii/S1566253519307377) , (2020) by *Timothée Lesort, Vincenzo Lomonaco, Andrei Stoian, Davide Maltoni, David Filliat and Natalia Díaz-Rodríguez* [[bib]](bibtex.bib#L1039-L1050) 
- [**Deep Online Learning Via Meta-Learning: Continual Adaptation for Model-Based RL**](https://openreview.net/forum?id=HyxAfnA5tm) , (2019) by *Anusha Nagabandi, Chelsea Finn and Sergey Levine* [[bib]](bibtex.bib#L647-L654) 
``` 
Formulates an online learning procedure that uses SGD to update model parameters, and an EM with a Chinese restaurant process prior to develop and maintain a mixture of models to handle non-stationary task distribution
``` 
- [**Experience replay for continual learning**](https://arxiv.org/abs/1811.11682) , (2019) by *Rolnick, David, Ahuja, Arun, Schwarz, Jonathan, Lillicrap, Timothy and Wayne, Gregory* [[bib]](bibtex.bib#L1179-L1187) 

## Continual Generative Modeling
- [**Continual Unsupervised Representation Learning**](https://arxiv.org/pdf/1910.14481.pdf) , (2019) by *Dushyant Rao, Francesco Visin, Andrei A. Rusu, Yee Whye Teh, Razvan Pascanu and Raia Hadsell* [[bib]](bibtex.bib#L657-L666) 
``` 
Introduces unsupervised continual learning (no task label and no task boundaries)
``` 
- [**Generative Models from the perspective of Continual Learning**](https://hal.archives-ouvertes.fr/hal-01951954) , (2019) by *Lesort, Timoth{\'e}e, Caselles-Dupr{\'e}, Hugo, Garcia-Ortiz, Michael, Goudou, Jean-Fran{\c c}ois and Filliat, David* [[bib]](bibtex.bib#L669-L681) 
``` 
Extensive evaluation of CL methods for generative modeling
``` 
- [**Lifelong Generative Modeling**](https://arxiv.org/abs/1705.09847) , (2017) by *Ramapuram, Jason, Gregorova, Magda and Kalousis, Alexandros* [[bib]](bibtex.bib#L684-L691) 

## Applications
- [**CLOPS: Continual Learning of Physiological Signals**](https://arxiv.org/abs/2004.09578) , (2020) by *Kiyasseh, Dani, Zhu, Tingting and Clifton, David A* [[bib]](bibtex.bib#L100-L107) 
``` 
a healthcare-specific replay-based method to mitigate destructive interference during continual learning
``` 
- [**LAMAL: LAnguage Modeling Is All You Need for Lifelong Language Learning**](https://openreview.net/forum?id=Skgxcn4YDS) , (2020) by *Fan-Keng Sun, Cheng-Hao Ho and Hung-Yi Lee* [[bib]](bibtex.bib#L1259-L1266) 
- [**Compositional Language Continual Learning**](https://openreview.net/forum?id=rklnDgHtDS) , (2020) by *Yuanpeng Li, Liang Zhao, Kenneth Church and Mohamed Elhoseiny* [[bib]](bibtex.bib#L1232-L1238) 
``` 
method for compositional continual learning of sequence-to-sequence models
``` 
- [**Unsupervised real-time anomaly detection for streaming data**](https://www.sciencedirect.com/science/article/pii/S0925231217309864) , (2017) by *Ahmad, Subutai, Lavin, Alexander, Purdy, Scott and Agha, Zuha* [[bib]](bibtex.bib#L73-L83) 
``` 
HTM applied to real-world anomaly detection problem
``` 
- [**Continuous online sequence learning with an unsupervised neural network model**](https://arxiv.org/abs/1512.05463) , (2016) by *Cui, Yuwei, Ahmad, Subutai and Hawkins, Jeff* [[bib]](bibtex.bib#L86-L97) 
``` 
HTM applied to a prediction problem of taxi passenger demand
``` 

## Thesis
- [**Continual Learning: Tackling Catastrophic Forgetting in Deep Neural Networks with Replay Processes**](https://arxiv.org/abs/2007.00487) , (2020) by *Timothée Lesort* [[bib]](bibtex.bib#L33-L42) 
- [**Continual Learning with Deep Architectures**](http://amsdottorato.unibo.it/9073/1/vincenzo_lomonaco_thesis.pdf) , (2019) by *Vincenzo Lomonaco* [[bib]](bibtex.bib#L1407-L1413) 
- [**Continual Learning in Neural Networks**](https://arxiv.org/abs/1910.02718) , (2019) by *Aljundi, Rahaf* [[bib]](bibtex.bib#L1838-L1845) 
- [**Continual learning in reinforcement environments**](https://www.cs.utexas.edu/~ring/Ring-dissertation.pdf) , (1994) by *Ring, Mark Bishop* [[bib]](bibtex.bib#L1475-L1482) 

## Workshops
- [**Workshop on Continual Learning at ICML 2020**](https://sites.google.com/view/cl-icml/organizers?authuser=0) , (2020) by *Rahaf Aljundi, Haytham Fayek, Eugene Belilovsky, David Lopez-Paz, Arslan Chaudhry, Marc Pickett, Puneet Dokania, Jonathan Schwarz, Sayna Ebrahimi* [[bib]](bibtex.bib#L44-L51) 
- [**4th Lifelong Machine Learning Workshop at ICML 2020**](https://openreview.net/group?id=ICML.cc/2020/Workshop/LifelongML#accept) , (2020) by *Shagun Sodhani, Sarath Chandar, Balaraman Ravindran and Doina Precup* [[bib]](bibtex.bib#L54-L61) 
