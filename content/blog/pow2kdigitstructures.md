title:      Powers of 2 and k-digits structures
slug:       powers-of-2-and-k-digits-structures
date:       2022-06-01 14:00
category:   Math 
tags:       number theory, powers of 2 
author:     Carolin Zöbelein
summary:    Powers of 2 and some of their k-digit structures.

In my paper <i>Powers of $2$ whose digits are powers of $2$</i> (see also <a href="https://research.carolin-zoebelein.de/public.html#bib6" title="External: Research website" target="_blank">https://research.carolin-zoebelein.de/public.html#bib6</a>), I'm discussing digits of powers of 2, and which conditions are necessary to get for them powers of 2, too.


Given be the set of powers of $2$ by $P_{y} = 2^{y}$, $y \in \mathbb{N}_{0}$. It is unknown if, apart from $P_{y=0} = 2^{0} = 1$, $P_{y=1} = 2^{1} = 2$, $P_{y=2} = 2^{2} = 4$, $P_{y=3} = 2^{3} = 8$ and $P_{y=7} = 2^{7} = 128$, there exist more $P_{y}$'s whose digits are powers of $2$ (<i>A130693</i> in the On-line Encyclopedia of Integer Sequences (OEIS) <a href="http://oeis.org/A130693" title="External: On-line Encyclopedia of Integer Sequences (OEIS)" target="_blank">http://oeis.org/A130693</a> [Dre07]) [Wel97], too.

Looking at the set of powers of $2$'s [Slo], we know that a $m$-digit power of $2$ by $P_{y}$, has a periodicity of $\varphi\left(5^{k}\right) = 4 \cdot 5^{k-1}$ for the last $k \leq m$ digits, starting at $2^{k}$ [YY64]. Taking the known periodicity of the last $k$-digits into account, we want to discuss properties for the last $k^{\prime} > k$ digits, for fixed last $k$-digits of $P_{y}$.

<b>Notation.</b> If we write $2^{y}_{k}$, we are talking about the $k$'th digit (counted from right to left, starting counting by $1$) of $2^{y}$, in base $10$ representation. For step sizes we write $d^{k + 1}_{y,k}$, meaning the step size of the $k + 1$-digit, starting by $2^{y}$, with a $k$-digit periodicity. Furthermore, we will denote the set of all one-digit powers of $2$ by $\mathcal{P}_{2} := \{ 1, 2, 4, 8 \}$.

For this, at first, we also considered $k$-digit structures of powers of $2$ in generally, and used the following two lemmas as starting point for our proofs in the mentioned paper.


<br />

<b>Lemma 2.1</b> ($k$-digits structure). <i>Let be $P_{y} = 2^{y}$, $y \in \mathbb{N}_{0}$, and the last $k^{\star}$-digits periodical with $\varphi\left(5^{k^{\star}}\right) = 4 \cdot 5^{k^{\star} - 1}$, for all $2^{y} \geq 2^{k^{\star}}$, $k^{\star} \geq 2$. Then for $2^{k + k^{\star} + \varphi\left(5^{k}\right)}$, $k \in \left[ k^{\star}, k^{\star} + \varphi\left(5^{k^{\star} - 1}\right) - 1 \right]$, the last $k$-digits are given by $2^{1 + k^{\star} + \varphi\left(5^{1}\right)}_{1} \cdot 2^{k - 1}$, with $k - x \approx \left(1 - \log_{10}\left(2\right)\right)k - k^{\star}\log_{10}\left(2\right)$ leading zeros for $k \geq 2$, and at least one leading zero for $k \geq 3$.</i>


<i>Proof.</i> We know, that for the last $k$-digits $2^{k + k^{\star} + \varphi\left(5^{k}\right)} \sim 2^{k + k^{\star}}$, which have $x \approx \left(k + k^{\star}\right) \log_{10}\left(2\right)$ digits. Since, we also have the periodicity $\varphi\left(5^{k}\right)$, we directly get $k - x \approx \left(1 - \log_{10}\left(2\right)\right)k - k^{\star}\log_{10}\left(2\right)$ for the number of leading zeros. Looking at $0 \leq k - x$, we receive $k \gtrsim k^{\star} \frac{\log_{10}\left(2\right)}{1 - \log_{10}\left(2\right)}$, and hence $k \geq 2$ by the constraint $k^{\star} \geq 2$, and for $1 \geq k - x$, with $k = k^{\star}$, we recive $k \gtrsim \frac{1}{1 - 2\log_{10}\left(2\right)}$, and hence $k \geq 3$. Finally it is easy to see, that the statement is always satisfied for $k \geq k^{\star}$, because of $k^{\star} \gtrsim k^{\star} \frac{\log_{10}\left(2\right)}{1 - \log_{10}\left(2\right)} \approx 0.4k^{\star}$ for $k = k^{*}$.

<br />

<b>Lemma 2.2</b> ($k^{\star}$-digits fixed structure). <i> Let be $P_{y} = 2^{y}$, $y \in \mathbb{N}_{0}$, and the last $k^{\star}$-digits periodical with $\varphi\left(5^{k^{\star}}\right) = 4 \cdot 5^{k^{\star} - 1}$, for all $2^{y} \geq 2^{k^{\star}}$, $k^{\star} \geq 2$. Then for $2^{k + k^{\star} + \varphi\left(5^{k}\right)}$, $k \in \left[ k^{\star}, k^{\star} + \varphi\left(5^{k^{\star} - 1}\right) - 1 \right]$, the last $k + 1$ to $k + \delta k$-digits are fixed for at least $\delta k = k^{\star}$ digits. </i>


<i>Proof.</i>
    Consider $\left( 2^{k + k^{\star} + \varphi\left(5^{k}\right)} - 2^{1 + k^{\star} + \varphi\left(5^{1}\right)}_{1} \cdot 2^{k - 1} \right) \cdot 10^{-k} \cdot 2^{\varphi\left(5^{\delta k}\right)} \approx \left( 2^{\left(k + 1\right) + k^{\star} + \varphi\left(5^{k + 1}\right)} - 2^{1 + k^{\star} + \varphi\left(5^{1}\right)}_{1} \cdot 2^{\left(k + 1\right) - 1} \right) \\ \cdot 10^{-\left(k + 1\right)} \left( 2^{k + k^{\star} + \varphi\left(5^{k}\right)} - 2^{1 + k^{\star} + \varphi\left(5^{1}\right)}_{1} \cdot 2^{k - 1} \right) \cdot 2^{\varphi\left(5^{\delta k}\right)} \approx \left( 2^{k + k^{\star} + \varphi\left(5^{k}\right)} \cdot 2^{4\varphi\left(5^{k}\right)} - 2^{1 + k^{\star} + \varphi\left(5^{1}\right)}_{1} \cdot 2^{k - 1} \right) \\ \cdot 5^{-1}$, for which we can equating the coefficients with approximation. We look at $\varphi\left(5^{\delta k}\right) \approx 4\varphi\left(5^{k}\right)$, and receive $\delta k \approx \lfloor \log_{5}\left(4 \cdot 5^{k}\right) \rfloor \approx \lfloor 1.86 k \rfloor \approx k$. Finally, we can conclude $\delta k \gtrsim k^{\star}$ for $k \in \left[ k^{\star}, k^{\star} + \varphi\left(5^{k^{\star} - 1}\right) - 1 \right]$.



### References
[Dre07] Gregory P. Dresden. A130693 - OEIS: Powers of 2 whose digits are powers of 2. <a href="http://oeis.org/A130693" title="External: Powers of 2 whose digits are powers of 2" target="_blank">http://oeis.org/A130693</a>, 07 2007. (Accessed on 2021/07/18).<br />
[Slo] N. J. A. Sloane. Table of n, 2 n for n = 0..1000 - OEIS. <a href="http://oeis.org/A000079/b000079.txt" title="External: Table of n, 2 n for n = 0..1000" target="_blank">http://oeis.org/A000079/b000079.txt</a>. (Accessed on 2021/08/08).<br />
[Wel97] David Wells. The Penguin dictionary of curious and interesting numbers. Penguin, 1997.<br />
[YY64] AM Yaglom and IM Yaglom. Challenging mathematical problems with elementary solutions. I, 1964.


