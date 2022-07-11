title:      Let`s calculate primes! Part I - Representation of times tables
date:       2017-12-29 21:21
category:   Math
tags:       primes, number theory
author:     Carolin Zöbelein
summary:    Describtion of prime numbers.

Some days ago, I had several nice ideas for calculating primes recursively, which I want to share with you in a small series of posts.  

I will use some insights of my work [https://github.com/Samdney/primescalc](https://github.com/Samdney/primescalc){target="_blank"} and assume you already know they. If not, please read it sidewise to the following posts.  

We have given our already known equation  
$$
	x_{i,j} 	= 2x_{i}x_{j} + x_{i} + x_{j}\\
			= \left(2x_{j} + 1\right)x_{i} + x_{j}\\
			= \left(2x_{i} + 1\right)x_{j} + x_{i}
$$
with $x_{i}, x_{j} \in \mathbb{N}$. Remember that this equation gives us all $x_{i,j}$ for which $2x_{i,j} + 1$ is an integer divisible number. 

So let`s look, for example on the numbers of $x_{i} = 1$, which are
$$x_{1,j} = 4, 7, 10, 13, 16, 19, 22, 25, 28, \dots$$.

Now we will choose a simple way of representation of this numbers. Be given the general form of a number in decimal representation:
$$
	\sum_{k = 0}^{n} 10^{k}
$$
with $n+1$, $n \in \mathbb{N}$, digits. Now assume, in our example, the number 4 is represented by the number 1, at the $4+1$ digit, the number 7 by the number 1, at the $7+1$ digit and so on. So we can write (read from right to left) as represenation for $x_{1,j}$:
$$
	\sum_{x_{j}} 10^{\left(2x_{i} + 1\right)x_{j} + x_{i}} = \sum_{x_{j}} 10^{3x_{j} + 1}
$$
and
$$
\dots 10010010010010010010010010000
$$

In this way, we can write every of our times tables which are given by $x_{i,j} = \left(2x_{i} + 1\right)x_{j} + x_{i}$.  

If we finally calculate this sum, we receive
$$
	\sum_{x_{j} = l}^{u} 10^{\left(2x_{i} + 1\right)x_{j} + x_{i}} = - \frac{10^{\left(2x_{i} + 1\right)l + x_{i}} - 10^{\left(2x_{i} + 1\right)\left(u+1\right) + x_{i}}}{10^{2x_{i} + 1} - 1}
$$. See also [wolframalpha.com](https://www.wolframalpha.com/input/?i=sum+z%3Dl,+u,+10%5E%28%282*x+%2B+1%29*z+%2B+x%29#7928802016733054506){target="_blank"}.


But what can we do with this, now?  
In the next post we will look at the intersection of times tables with this kind of representation.
