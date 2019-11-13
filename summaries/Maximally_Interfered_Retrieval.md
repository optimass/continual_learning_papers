# [Online Continual Learning with Maximally Interfered Retrieval](https://arxiv.org/abs/1908.04742)
## Rahaf Aljundi, Lucas Caccia, Eugene Belilovsky, Massimo Caccia, Min Lin, Laurent Charlin, Tinne Tuytelaars
  
## Intro

Experience replay (ER) and generative replay (GEN) are two effective continual learning strategies. In the former, samples from a stored memory are replayed to the continual learner to reduce forgetting. In the latter, old data is compressed with a generative model and generated data is replayed to the continual learner. Both of these strategies assume a random sampling of the memories. But learning a new task doesn't cause **equal** interference (forgetting) on the previous tasks!  

In this work, we propose a controlled sampling of the replays. Specifically, we retrieve the samples which are most interfered, i.e. whose prediction will be most negatively impacted by the foreseen parameters update. The method is called Maximally Interfered Retrieval (MIR).

## Cartoon for explanation

![](https://i.imgur.com/5F3jT36.png)

Learning about dogs and horses might cause more interference on lions and zebras than on cars and oranges. Thus, replaying lions and zebras would be a more efficient strategy.

## Method

1) incoming data: ![](https://latex.codecogs.com/gif.latex?%28X_t%2CY_t%29)

2) foreseen parameter update: ![](https://latex.codecogs.com/gif.latex?%5Ctheta%5Ev%3D%20%5Ctheta-%5Calpha%5Cnabla%5Cmathcal%7BL%7D%28f_%5Ctheta%28X_t%29%2CY_t%29)

### applied to ER (ER-MIR)
3) Search for the top-k values x in the stored memories using the criterion ![](https://latex.codecogs.com/gif.latex?s_%7BMI%7D%28x%29%20%3D%20%5Cmathcal%7BL%7D%28f_%7B%5Ctheta%5Ev%7D%28x%29%2Cy%29%20-%5Cmathcal%7BL%7D%28f_%7B%5Ctheta%7D%28x%29%2Cy%29)

### or applied to GEN (GEN-MIR)
3)   

![](https://latex.codecogs.com/gif.latex?%5Cunderset%7BZ%7D%7B%5Cmax%7D%20%5C%2C%20%5Cmathcal%7BL%7D%5Cbig%28f_%7B%5Ctheta%5Ev%7D%28g_%5Cgamma%28Z%29%29%2CY%5E*%5Cbig%29%20-%5Cmathcal%7BL%7D%5Cbig%28f_%7B%5Ctheta%7D%28g_%5Cgamma%28Z%29%29%2CY%5E*%5Cbig%29)

![](https://latex.codecogs.com/gif.latex?%5Ctext%7Bs.t.%7D%20%5Cquad%20%7C%7Cz_i-z_j%7C%7C_2%5E2%20%3E%20%5Cepsilon%20%5Cforall%20z_i%2Cz_j%20%5Cin%20Z%20%5C%2C%5Ctext%7Bwith%7D%20%5C%2C%20z_i%5Cneq%20z_j)

i.e. search in the latent space of a generative model ![](https://latex.codecogs.com/gif.latex?g_%5Cgamma) for samples that are the most forgotten given the foreseen update.

4) Then add theses memories to incoming data ~[](https://latex.codecogs.com/gif.latex?X_t) and train ~[](https://latex.codecogs.com/gif.latex?f_%5Ctheta)

## Results

### qualitative

![](https://i.imgur.com/ZRNTWXe.png)

Whilst learning 8s and 9s (first row), GEN-MIR mainly retrieves 3s and 4s (bottom two rows) which are similar to 8s and 9s respectively.

### quantitative 

GEN-MIR was tested on MNIST SPLIT and Permuted MNIST, outperforming the baselines in both cases.

ER-MIR was tested on MNIST SPLIT, Permuted MNIST and Split CIFAR-10, outperforming the baselines in all cases.


## Other stuff
### (for avid readers)

We propose a hybrid method (AE-MIR) in which the generative model is replaced with an autoencoder to facilitate the compression of harder dataset like e.g. CIFAR-10.


