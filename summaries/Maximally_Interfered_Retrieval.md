# [Online Continual Learning with Maximally Interfered Retrieval](https://arxiv.org/abs/1908.04742)
## Rahaf Aljundi, Lucas Caccia, Eugene Belilovsky, Massimo Caccia, Min Lin, Laurent Charlin, Tinne Tuytelaars
  
## Intro

Experience replay (ER) and generative replay (GEN) are two effective continual learning strategies. In the former, samples from a stored memory are replayed to the continual learner to reduce forgetting. In the latter, old data is compressed with a generative model and generated data is replayed to the continual learner. Both of these strategies assume a random sampling of the memories. But learning a new task doesn't cause **equal** interference (forgetting) on the previous tasks!  

In this work, we propose a controlled sampling of the replays. Specifically, we retrieve the samples which are most interfered, i.e. whose prediction will be most negatively impacted by the foreseen parameters update. The method is called Maximally Interfered Retrieval (MIR).

## Cartoon for explanation

https://i.imgur.com/5F3jT36.png

Learning about dogs and horses might cause more interference on lions and zebras than on cars and oranges. Thus, replaying lions and zebras would be a more efficient strategy.

## Method

1) incoming data: $(X_t,Y_t)$

2) foreseen parameter update: $\theta^v= \theta-\alpha\nabla\mathcal{L}(f_\theta(X_t),Y_t)$

### applied to ER (ER-MIR)
3) Search for the top-$k$ values $x$ in the stored memories using the criterion $$s_{MI}(x) = \mathcal{L}(f_{\theta^v}(x),y) -\mathcal{L}(f_{\theta}(x),y)$$

### or applied to GEN (GEN-MIR)
3)   
$$
     \underset{Z}{\max} \, \mathcal{L}\big(f_{\theta^v}(g_\gamma(Z)),Y^*\big) -\mathcal{L}\big(f_{\theta}(g_\gamma(Z)),Y^*\big)
$$
$$
         \text{s.t.}   \quad ||z_i-z_j||_2^2 > \epsilon \forall  z_i,z_j \in Z \,\text{with} \, z_i\neq z_j
$$
i.e. search in the latent space of a generative model $g_\gamma$ for samples that are the most forgotten given the foreseen update.

4) Then add theses memories to incoming data $X_t$ and train $f_\theta$

## Results

### qualitative
https://i.imgur.com/ZRNTWXe.png

Whilst learning 8s and 9s (first row), GEN-MIR mainly retrieves 3s and 4s (bottom two rows) which are similar to 8s and 9s respectively.

### quantitative 

GEN-MIR was tested on MNIST SPLIT and Permuted MNIST, outperforming the baselines in both cases.

ER-MIR was tested on MNIST SPLIT, Permuted MNIST and Split CIFAR-10, outperforming the baselines in all cases.


## Other stuff
### (for avid readers)

We propose a hybrid method (AE-MIR) in which the generative model is replaced with an autoencoder to facilitate the compression of harder dataset like e.g. CIFAR-10.


