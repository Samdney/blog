title:      OOP Ahead Neural Network Designs and Metaprogramming
slug:       oop-ahead-neural-network-designs-and-metaprogramming
date:       2022-08-27 14:00
category:   Math        
tags:       neural networks, oop, object oriented programming, metaprogramming, graph theory
author:     Carolin Zöbelein
summary:    A disruptive design concept for neural networks.
id:         post_0019   
basename:   disruptivedesignneuralnetworks

**The following research project is seeking for funding.  
Go to
<a href="https://research.carolin-zoebelein.de/funding.html" title="External: Funding" targe="_blank">https://research.carolin-zoebelein.de/funding.thml</a>
(Private Investors), for checking for further information, if you are
interested in supporting this project.**

Today, we want to talk about one of my current projects. Its one of my
newer work, hence I just want to present the basic research idea.

Have you ever thought about new, different and disruptive design
concepts for neural networks (NN), which have the potential to enhanced
the abilities of NNs? I do.

In the following graphics, you can see the most basic and known concept
of an usual NN:


![Neural Network](/blog/images/disruptivedesignneuralnetworks/neuralnetwork.png)


Given are the three layers $L_{0}$ (Input), $L_{1}$ (Hidden), and
$L_{2}$ (Ouput), each consisting of several nodes. The NN works in such
a way, that the output at each neuron is the activation of a weighted
sum of inputs. So, the on/off switch of each neuron is given by two
factors: the choosen activation function, and the weights, retrieved by
training the network.

Let’s assume for the moment, that we have given just the two input nodes
$I_{1}$, and $I_{2}$, and the one hidden node $H_{1}$, and asssuming a
simple hard limit as activation function at $H_{1}$. So, mathematical we
can write for the activation $v$ for inputs $x_{1}$, and $x_{2}$, with
weights $w_{1}$, and $w_{2}$

$$\begin{equation}
  v = \sum_{i = 1}^{2} w_{i}x_{i},
\end{equation}$$

with the activation function

$$\begin{equation}
  \varphi^{\mathrm{hlim}}\left(v\right) =
  \begin{cases}
    1 & \mathrm{if } v \geq h \\
    0 & \mathrm{if } v < h
  \end{cases}
\end{equation}$$

for the neuron $H_{1}$ (McCulloch-Pitts). Here, $h$ is the choosen
limit, often set to $0$. Now, we want to look at a specific case. For
this, we define $x_{1}, x_{2} \in \{ 0, 1\}$ and $h := 0$, at first.
This means we have the possible inputs $00$, $01$, $10$, and $11$.
Furthermore, let’s say $w_{1} = w_{2} = -0.5$. So, what do we get with
that? In fact, that’s a logical NOR.

$$\begin{equation}
  X\left(x_{1}, x_{2} \right) =
  \begin{cases}
    00 & v = \left(-0.5\right) \cdot 0 + \left(-0.5\right) \cdot 0 = 0 \Rightarrow 1 \\
    01 & v = \left(-0.5\right) \cdot 0 + \left(-0.5\right) \cdot 1 = -0.5 \Rightarrow 0 \\
    10 & v = \left(-0.5\right) \cdot 1 + \left(-0.5\right) \cdot 0 = - 0.5 \Rightarrow 0 \\
    11 & v = \left(-0.5\right) \cdot 1 + \left(-0.5\right) \cdot 1 = -1 \Rightarrow 0
  \end{cases}
\end{equation}$$

We see, that the combination of the input and the hidden layer, with
specific weights and activiation function, can be identified with
specific logical statements. Well, the question is now, are there also
other ways to present, in our example NOR, by an other kind of graph
representation. For this, look at the following ones:

 
![NOR network](/blog/images/disruptivedesignneuralnetworks/ifmaxISs.png)


Given be a graph $G = \left(V, E\right)$ consisting of the three
vertices $v_{1}$, $v_{2}$, and $v_{3}$. We want to map the four possible
$x_{2}x_{1}$ constellations on the edges $e_{i}$ of $G$. For this, we
say that $G$ never has an edge $e_{1} := \{ v_{1}, v_{2} \}$, the edge
$e_{2} := \{ v_{2}, v_{3} \}$ exists iff input $x_{1} = 1$, else it
doesn’t exist, and that the edge $e_{3} := \{ v_{1}, v_{3} \}$ exists
iff input $x_{2} = 1$, else it doesn’t exist. In this way, we represent
each possible input by one specific graph.

We can now identifiy this graphs with an logical NOR by the following
consideration. Assuming $P$, be an unique graph property, then we can
indentify the output of NOR with one specific graph property
characteristics, or the changing of it, respectively.

In our case, for example, we will take the maximum independent set of
each possible input (see also graphic). We can see that for the cases
$11$ and $00$, each, we only have one maximum set, which we can differ
between this two cases by its size. Compared to this the inputs $01$,
and $10$, has two maximum independent sets, each, but one differently to
each other.

We take this observations, and decide to identify the case of a maximum
independent set of size $3$, as true, else as false. Hence, our graphics
shows us the belonging NOR graph representation of the neural network
definition of above.


![Concept](/blog/images/disruptivedesignneuralnetworks/concept.png)


Well that have been a very primitive example, but in our work (see
graphics), we will show, that it is possible to map much more complex
classical coding structures on corresponding graph representations, also
able to act dynamically. Even more, we investigate in an enhancement of
this concept to object oriented programming and the possibilites of
metaprogramming, a naturally given application of this new kind of
neural network approach.

In future blog posts, we will discuss the current state of research
regarding this neural network design, as well as the deeper mathematical
structure of our proposed concept.

’till then!
