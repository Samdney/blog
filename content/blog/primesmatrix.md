title:      Primes matrix
date:       2018-03-23 01:30
category:   Math
tags:       primes, number theory
author:     Carolin Zöbelein
summary:	Some time ago, I already wrote about representation ideas of primes ...

Some time ago, I already wrote about representation ideas of primes and we saw
that we run in troubles with this. Today, I want to present you a similar
approach.  

Let's start again with our equation

$$
x_{ij} = \left(2x_{i} + 1\right)x_{j} + x_{i} \\
y_{ij} = \left(2x_{ij} + 1\right)
$$

and the following represenation

$$
x_{1j} \ \ \ \  | 00010010010010010010 \dots \\  
x_{2j} \ \  \ \  | 00000010000100001000 \dots \\ 
x_{\left(1,2\right),j} | 11101101101001100101 \dots
$$

The first line is given by $x_{1j} = 3x_{j} + 1 = 4, 7, 10, 13, 16, 19$. If
we look a the numbers from 1 to 20 (from left to right), we represent all numbers which are generated
by $x_{1j}$, by '1' and the other numbers by '0'. In the second line, we do
the same for $x_{2j} = 5x_{j} + 2 = 7, 12, 17$.

In the third line we see $x_{\left(1,2\right),j}$, which represents all
numbers which are not element of $x_{1j}$ and not element of $x_{2j}$ by
'1' and the others by '0'. So we can write

$$
x_{\left(1,2\right),j} = \overline{x_{1j}} \cdot \overline{x_{2j}}
$$
. Ok. What can we do with this, now?

At first, we look at $x_{1j}$ and $x_{2j}$. We will rewrite them to matrices
$X_{\left(1\right)}^{n\times n}$ and $X_{\left(2\right)}^{n\times n}$. This
matrices, all of the same size $n\times n$, have the numbers from the
representation above as diagonal entries. All other entries are '0'.

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

Here are
$$
x_{\left(i\right),kj} := \left\{
    \begin{array}{l@{\quad \quad}l}
    1 & \mathrm{if} \ k = \left(2x_{i} + 1\right)x_{l} + x_{i} \\
    0 & \mathrm{else}
    \end{array}
    \right. 
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

With this, we get $\overline{X_{\left(i\right)}^{n\times n}}$ by

$$
\overline{X_{\left(i\right)}^{n\times n}} = \mathbb{1}_{n} - X_{\left(i\right)}^{n\times n}
$$

For an arbitrary number $i=a,\dots,b$, $a,b \in
\mathbb{N}$, $a \le b$, of equations $x_{ij}$ we receive

$$
X_{\left(a,\dots,b\right)}^{n \times n} = \prod_{i=a}^{b} \left(\mathbb{1}_{n} -
X_{\left(i\right)}^{n\times n}\right)
$$

and so

$$
x_{\left(a,\dots,b\right),kj} = \prod_{i=a}^{b} \left(1 - x_{\left(i\right),kj}\right)\delta_{kj} \\
$$

We received a matrix with '1' entries at the places $j=k$ which represent
primes and else '0'.  
