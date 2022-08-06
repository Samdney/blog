title:      Primes matrix: Approximation 2
slug:       primesapprox2
date:       2018-04-05 07:37
category:   Math        
tags:       primes, number theory
author:     Carolin Zöbelein
summary:    Since I wasn't happy about the final sum in my last post, I think about an alternative way.
id:         post_0009   
basename:   primesmatrixapprox2

Since I wasn’t happy about the final sum in my last post [Primes matrix:
Approximation](https://samdney.github.io/2018/03/primes-matrix-approximation.html),
I think about an alternative way.

We had $$
    x_{\left(a,\dots,b\right),kj} = \lim_{m \rightarrow \infty} \left(\prod_{i=a}^{b} \exp\left(I 2\pi\frac{k-x_{i}}{2x_{i} + 1} \epsilon\left(m\right)\right)\right) \delta_{kj} \\
    = \lim_{m \rightarrow \infty} \exp\left(\sum_{i = a}^{b} I2\pi\frac{k - x_{i}}{2x_{i} + 1}\epsilon\left(m\right)\right) \delta_{kj}
$$

in which we made the product over all $\exp$-functions for each $x_{i}$.
Now, instead we will do the product over the arguments of the
$\exp$-functions

$$
     x_{\left(a,\dots,b\right),kj} = \lim_{m \rightarrow \infty} \exp\left(\prod_{i = a}^{b} I2\pi\frac{k - x_{i}}{2x_{i} + 1}\epsilon\left(m\right)\right) \delta_{kj}
$$

Let’s look at the qualities of this product

$$
    \prod_{i = a}^{b} \frac{k - x_{i}}{2x_{i} + 1}
$$

and under which conditions we receive integers. From my work
<a href="https://github.com/Samdney/primescalc"
target="_blank">https://github.com/Samdney/primescalc</a> we already
know that we get troubles if at least one of the $2x_{i} + 1$ is a
divisible number. Hence, we always asume that all our numbers
$2x_{i} + 1$ are primes.

We receive integer values in the following cases

-   **Case 1:** For all $k$-values which are also solutions for every
    single $\exp$-equation.

-   **Case 2:** For all $k$-values which is a solution for at least one
    single $\exp$-equation and also leads to the trivial solution with
    $x_{\left(1\right),j} = N\left(2x_{\left(2\right),i} + 1\right)$,
    $N \in \mathbb{N}$.

For the second case, we take the example of two equations with
$x_{1} = 2$ and $x_{2} = 3$

$$
    \frac{k - x_{1}}{2x_{1} + 1} \frac{k - x_{2}}{2x_{2} + 1} = \frac{\left(k - 2\right)\left(k - 3\right)}{5
    \cdot 7}
$$

Here we receive one solution for $k = 37$,
$\frac{35 \cdot 34}{35} = 34$, which is also a solution for
$\frac{37 - 2}{5} = 7$ and an other solution for $k = 38$,
$\frac{36 \cdot
35}{35} = 36$ which is also a solution for $\frac{38 - 3}{7} = 5$. We
see that $k$ leads to the trivial case in which $x_{j}$ of one single
$\exp$-equation is equal to the prime value of an other single
$\exp$-equation or the product of primes of several single
$\exp$-equations.
