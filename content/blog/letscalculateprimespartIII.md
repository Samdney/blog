title:      Let`s calculate primes! Part III - Intersection of times tables: sum formula
slug:       lets-calculate-primes-part-iii-intersection-of-times-tables-sum-formula
date:       2018-01-13 06:31
category:   Math        
tags:       primes, number theory
author:     Carolin Zöbelein
summary:    Describtion of prime numbers part 3.
id:         post_0005   
basename:   letscalculateprimespartIII

In the post before, we looked at the intersection ot times tables and
its problems. Now we will look at the belonging sum formula, which is
given by

$$
    \sum_{x_{i} = l^\prime}^{u^\prime}  \sum_{x_{j} = l}^{u} 10^{\left(2x_{i} + 1\right)x_{j} + x_{i}}  
$$

and with our results before as

$$
    \sum_{x_{i} = l^\prime}^{u^\prime} \left( - \frac{10^{\left(2x_{i} + 1\right)l + x_{i}} - 10^{\left(2x_{i} + 1\right)\left(u+1\right) + x_{i}}}{10^{2x_{i} + 1} - 1} \right)
$$.

We are not able to solve this second sum analytical, but it can be
interesting to look a bit around this sum. I had a look what <a
href="https://www.wolframalpha.com/input/?i=-%2810%5Ex+%2810%5E%28l+%282+x+%2B+1%29%29+-+10%5E%28%28u+%2B+1%29+%282+x+%2B+1%29%29%29%29%2F%2810%5E%282+x+%2B+1%29+-+1%29"
target="_blank">wolframalpha.com</a> is able to tell me about our first
sum result and I found one thing which catched my attention.

$$
    \int -\frac{10^{x}\left(10^{l\left(2x + 1\right)} - 10^{\left(u + 1\right)\left(2 x + 1\right)}\right)}{10^{2 x + 1} - 1} \mathrm{d}x
$$

$$
    = \frac{10^{x} \left(\frac{10^{2lx + l} {}_{2}F_{1}\left(1, l + \frac{1}{2}, l + \frac{3}{2}, 10^{2 x + 1}\right)}{2l + 1} - \frac{10^{(u + 1)(2 x + 1)} {}_{2}F_{1}\left(1, u + \frac{3}{2}, u + \frac{5}{2}, 10^{2 x + 1}\right)}{2 u + 3}\right)}{\log(10)} + constant,
$$

with

$$
    {}_{2}F_{1}\left(a, b; c; x\right)
$$

is the hypergeometric function.

It’s deeply interesting that we are able to find an integral which is
connected to the Gamma-Function over the hypergeometric function and
hence to primes. Althougth we are not able to do both sums exactly, this
gives us an hint, that we are maybe able to do the first calculation
with a sum and the second calculation with the help of an integration.

At the moment, we can’t use this information, but we should keep this in
mind.
