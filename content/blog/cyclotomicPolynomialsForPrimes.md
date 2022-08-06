title:      Cyclotomic polynomials for primes
slug:       cyclotomic-polynomials-for-primes
date:       2018-07-18 05:33
category:   Math        
tags:       cyclotomic polynomials, primes, number theory
author:     Carolin Zöbelein
summary:    How you can use cyclotomic polynomials for primes number describtion.
id:         post_0011   
basename:   cyclotomicPolynomialsForPrimes

Currently, I’m spending my time with cyclotomic polynomials. So, I don’t
want to miss the possibility also to mention a small note about the
connection of this polynomials to the set of prime numbers.

At first, we have a cyclotomic polynomial in the following way

$$\begin{equation}
    \phi_{n}\left(x\right) = \prod_{\substack{1 \leq g \leq n \\ ggT\left(g,n\right) = 1}}
    \left(x - e^{\frac{2\pi i g}{n}}\right)
\end{equation}$$

with $n, g \in \mathbb{N}$, respectively

$$\begin{alignat}{3}
    x^{n} - 1 &= \prod_{1 \leq g \leq n} \left(x - e^{\frac{2\pi i g}{n}}\right) \notag \\
    &= \prod_{d | n} \prod_{\substack{1 \leq g \leq n \\ ggT\left(g,n\right) = d}} \left(x - e^{\frac{2\pi i g}{n}}\right) \notag \\
    &= \prod_{d | n} \phi_{n/d}\left(x\right) \notag \\
    &= \prod_{d | n} \phi_{d}\left(x\right)
\end{alignat}$$

. In the case of pime numbers $p \in \mathbb{P}$, we also have

$$\begin{equation}
    \phi_{p}\left(x\right) = 1 + x + x^{2} + \dots + x^{p-1} = \sum_{k =
    0}^{p-1} x^{k}
\end{equation}$$

. From this follows the first rewriting

$$\begin{alignat}{3}
    \phi_{p}\left(x\right) &= \sum_{k = 0}^{p-1} x^{k} \notag \\
    &= \sum_{k = 0}^{p-1} e^{k\ln\left(x\right)} \notag \\
    &= e^{0\ln\left(x\right)} + \sum_{k = 1}^{p-1} e^{k\ln\left(x\right)}
    \notag \\
    &= 1 + \frac{e^{\ln\left(x\right)} \left(e^{\left(p-1\right)\ln\left(x\right)} - 1\right)}{e^{\ln\left(x\right)} - 1}
\end{alignat}$$

, since

$$
    \sum_{k = 1}^{n} e^{kA} = \frac{e^{A}\left(e^{An} - 1\right)}{e^{A} - 1}
$$

. Now we will solve this equation for $p$.

$$\begin{alignat}{3}
    \phi_{p}\left(x\right) &= 1 + \frac{e^{\ln\left(x\right)} \left(e^{\left(p-1\right)\ln\left(x\right)} - 1\right)}{e^{\ln\left(x\right)} - 1} \notag \\
    \left(\phi_{p}\left(x\right) - 1\right)\left(e^{\ln\left(x\right)} - 1\right) &=
    e^{\ln\left(x\right)}\left(e^{\left(p-1\right)\ln\left(x\right)} - 1\right)
    \notag \\
    \frac{\left(\phi_{p}\left(x\right) - 1\right)\left(e^{e^{\ln\left(x\right)}} - 1\right)}{e^{\ln\left(x\right)}} + 1 &= e^{\left(p-1\right)\ln\left(x\right)} \notag \\
    \left(p-1\right)\ln\left(x\right) &= \ln\left(\frac{\left(\phi_{p}\left(x\right) - 1\right)\left(e^{\ln\left(x\right)} - 1\right)}{e^{\ln\left(x\right)}} + 1\right) \notag \\
    \left(p-1\right)\ln\left(x\right) &= \ln\left(\frac{\left(\phi_{p}\left(x\right) - 1\right)\left(x - 1\right) + x}{x}\right) \notag \\
    \ln\left(x\right)\left(\left(p-1\right) + 1\right) &=
    \ln\left(\left(\phi_{p}\left(x\right) - 1\right)\left(x - 1\right) + x\right) \notag \\
    p &= \ln\left(\frac{\left(\phi_{p}\left(x\right) - 1\right)\left(x - 1\right) + x}{x}\right)
\end{alignat}$$

Additionally, we have our second, very easy to see, connection for prime
numbers

$$\begin{alignat}{3}
    \phi_{p}\left(x\right) &= x^{p} - 1 \notag \\
    &= \sum_{k' = 0}^{p} x^{k'} - \sum_{k'' = 0}^{p-1} x^{k''} - 1 \notag \\
    &= \phi_{p+1}\left(x\right) - \phi_{p}\left(x\right) - 1
\end{alignat}$$

. I have no idea for which this can be useful, but I think it is nice to
know :P.
