title:      Primes matrix: Approximation
slug:       primes-matrix-approximation
date:       2018-03-31 01:44
category:   Math        
tags:       primes, number theory
author:     Carolin Zöbelein
summary:    Last week, I wrote about a possibility to represent primes. The negative part of ...
id:         post_0008   
basename:   primesmatrixapprox

Last week, I wrote in [Primes
matrix](https://samdney.github.io/2018/03/primes-matrix.html) about a
possibility to represent primes. The negative part of this was, that
there isn’t a nice way to generate $X_{\left(i\right)}^{n\times n}$.
Today, I want to add a few lines, how you can approximate it.

Let’s look again at

$$
X_{\left(1\right)}^{n\times n} :=
\begin{pmatrix}
0 & 0 & 0 & 0 & 0 & 0 & 0 & \cdots \\
0 & 0 & 0 & 0 & 0 & 0 & 0 & \cdots \\
0 & 0 & 0 & 0 & 0 & 0 & 0 & \cdots \\
0 & 0 & 0 & 1 & 0 & 0 & 0 & \cdots \\
0 & 0 & 0 & 0 & 0 & 0 & 0 & \cdots \\
0 & 0 & 0 & 0 & 0 & 0 & 0 & \cdots \\
0 & 0 & 0 & 0 & 0 & 0 & 1 & \cdots \\
\vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \ddots
\end{pmatrix}
= \left(x_{\left(1\right),kj}\right)_{k=1,\dots,n \ , j=1,\dots, n} \  \delta_{kj}
$$

$$
X_{\left(2\right)}^{n\times n} :=
\begin{pmatrix}
0 & 0 & 0 & 0 & 0 & 0 & 0 & \cdots \\
0 & 0 & 0 & 0 & 0 & 0 & 0 & \cdots  \\
0 & 0 & 0 & 0 & 0 & 0 & 0 & \cdots \\
0 & 0 & 0 & 0 & 0 & 0 & 0 & \cdots \\
0 & 0 & 0 & 0 & 0 & 0 & 0 & \cdots \\
0 & 0 & 0 & 0 & 0 & 0 & 0 & \cdots \\
0 & 0 & 0 & 0 & 0 & 0 & 1 & \cdots \\
\vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \ddots
\end{pmatrix}
= \left(x_{\left(2\right),kj}\right)_{k=1,\dots,n \ , j=1,\dots, n} \  \delta_{kj}
$$

Instead of the definition from my last post, now, we will define
$x_{\left(i\right),kj}$ in the following way

$$
    x_{\left(i\right),kj} := \lim_{m \rightarrow \infty} \cos^{2m}\left(2\pi\frac{k - x_{i}}{2x_{i} + 1}\right) \delta_{kj} 
$$

and

$$
\delta_{kj} := \left\{
    \begin{array}{l@{\quad \quad}l}
    1 & \mathrm{if} \ k = j \\
    0 & \mathrm{else}
    \end{array}
\right.
$$

**Explanation:** Like in our old definition, we always get an ‘1’ at all
places which presents a divisible number for a given $x_{i}$. Now, at
the other positions, we get an value $v$ between $0 < |v| < 1$, instead
of ‘0’ in our old definition. To get our ’0’s, like before, we use
$\lim_{m \rightarrow \infty}$. The factor two ensures a positive
approxiation value.

With this, we also get $$
    \overline{x_{\left(i\right),kj}} := \left(1 - x_{\left(i\right),kj}\right)\delta_{kj} \\
    = \lim_{m \rightarrow \infty} \left(1 - \cos^{2m}\left(2\pi\frac{k- x_{i}}{2x_{i} + 1}\right)\right)\delta_{kj}  
$$

An alternative way also to write this, is given by

$$
    \overline{x_{\left(i\right),kj}} := \lim_{m \rightarrow \infty} \sin^{\frac{2}{m}}\left(2\pi\frac{k - x_{i}}{2x_{i} + 1}\right) \delta_{kj}
$$

**Explanation:** We have a similiar situation like for our
$x_{\left(i\right),kj}$, but in this case now, we have to use $2/m$ to
get an approximation for ‘1’.

We see that we can use $\cos$ and also $\sin$ depending on which values
we are interested in. Of course, don’t forget the different cases for
$\lim$ with $2m$ respectively $2/m$.

So, we can put this together to

$$
    \eta_{\left(i\right),kj}  := \lim_{m \rightarrow \infty} \exp\left(I 2\pi\frac{k-x_{i}}{2x_{i} + 1} \epsilon\left(m\right)\right) \delta_{kj}
$$

$I$ is the Imaginary unit, with $I^{2} = -1$ and

$$
\epsilon\left(m\right) := \left\{
    \begin{array}{l@{\quad \quad}l}
    2m & \mathrm{for \ real \ part \ Re\left(\eta\right)} \  \\
    \frac{2}{m} & \mathrm{for \ imaginary \ part \ Im\left(\eta\right)}
    \end{array}
\right.
$$

Ok. What do we need, next? We need

$$
    \exp\left(Iz_{1}\right) \cdot \exp\left(Iz_{2}\right) = \exp\left(I\left(z_{1} + z_{2}\right)\right)  = \cos\left(z_{1} + z_{2}\right) + I\sin\left(z_{1} + z_{2}\right)
$$

so let’s look at

$$
    z_{1} + z_{2} = 2\pi \epsilon\left(m\right)\left(\frac{k - x_{1}}{2x_{1} + 1} + \frac{k - x_{2}}{2x_{2} + 1}\right) \\
    = 2\pi \epsilon\left(m\right) \frac{\left(k - x_{1}\right)\left(2x_{2} + 1\right) + \left(k - x_{2}\right)\left(2x_{1} + 1\right)}{\left(2x_{1} + 1\right)\left(2x_{2} + 1\right)}
$$

In <a href="https://github.com/Samdney/primescalc"
target="_blank">https://github.com/Samdney/primescalc</a> we already
discussed a similiar situation, which showed us that we don’t have any
problems if $2x_{1} + 1$ and $2x_{2} + 1$ are primes. For more
information about this, please read the mentioned paper.

So we can do our final step $$
    x_{\left(a,\dots,b\right),kj} = \lim_{m \rightarrow \infty} \left(\prod_{i=a}^{b} \exp\left(I 2\pi\frac{k-x_{i}}{2x_{i} + 1} \epsilon\left(m\right)\right)\right) \delta_{kj} \\
    = \lim_{m \rightarrow \infty} \exp\left(\sum_{i = a}^{b} I2\pi\frac{k - x_{i}}{2x_{i} + 1}\epsilon\left(m\right)\right) \delta_{kj}
$$

Now we look at the special case of
$x_{i} = a, a+1, a+2, \dots, b-2, b-1,b$ for the given sum

$$
  \sum_{i = a}^{b} I2\pi\frac{k - x_{i}}{2x_{i} + 1}\epsilon\left(m\right) = \\
  = I2\pi\frac{1}{4}\left(2k\psi^{\left(0\right)}\left(b + \frac{3}{2}\right) + \psi^{\left(0\right)}\left(b + \frac{3}{2}\right) - 2k\psi^{\left(0\right)}\left(\left(a - 1\right) + \frac{3}{2}\right) - \psi^{\left(0\right)}\left(\left(a-1\right) + \frac{3}{2}\right)\right)\epsilon\left(m\right)   
$$

since

$$
    \sum_{x=1}^{n} \frac{k - x}{2x + 1}\\
    = \frac{1}{4}\left(2k\psi^{\left(0\right)} \left(n + \frac{3}{2}\right) -
    2k\psi^{\left(0\right)}\left(\frac{3}{2}\right) - 2k + \psi^{\left(0\right)}\left(n + \frac{3}{2}\right) - \psi^{\left(0\right)}\left(\frac{3}{2}\right)\right) 
$$

$\psi^{\left(n\right)}\left(x\right)$ is the n-the derivate of the
digamma function.

Finally, a small comment about permitted ranges.  
Since our functions work with fix period $(k - x_{i})/(2x_{i} + 1)$, we
have to ignore the range $[1,x_{i}]$ for each $x_{i}$-equation, else we
will also receive invalid results.
