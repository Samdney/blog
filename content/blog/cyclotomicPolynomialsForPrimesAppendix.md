title:      Cyclotomic polynomials for primes: Appendix
slug:       cyclotomic-polynomials-for-primes-appendix
date:       2018-07-30 13:33
category:   Math        
tags:       cyclotomic polynomials, primes, number theory
author:     Carolin Zöbelein
summary:    Ok, last time, we had ...
id:         post_0012   
basename:   cyclotomicPolynomialsForPrimesAppendix

Ok, last time, we had

$$\begin{alignat}{3}
    \phi_{p}\left(x\right) &= \sum_{k = 0}^{p-1} x^{k} \notag \\
    &= \sum_{k = 0}^{p-1} e^{k\ln\left(x\right)} \notag \\
    &= e^{0\ln\left(x\right)} + \sum_{k = 1}^{p-1} e^{k\ln\left(x\right)}
    \notag \\
    &= 1 + \frac{e^{\ln\left(x\right)} \left(e^{\left(p-1\right)\ln\left(x\right)} - 1\right)}{e^{\ln\left(x\right)} - 1}
\end{alignat}$$

. All what I want to add in this small appendix is, that we can, of
course, also write here

$$\begin{alignat}{3}
    \phi_{p}\left(x\right) &= 1 + \frac{e^{\ln\left(x\right)} \left(e^{\left(p-1\right)\ln\left(x\right)} - 1\right)}{e^{\ln\left(x\right)} - 1} \notag \\
    &= 1 + \frac{x\left(x^{p-1} - 1\right)}{x - 1} \\
        &= 1 + \frac{x^{p} - x}{x - 1} \notag
\end{alignat}$$

Now, if we solve this for $p$

$$\begin{alignat}{3}
    \phi_{p}\left(x\right) &= 1 + \frac{x^{p} - x}{x - 1} \notag \\
    \phi_{p}\left(x\right) - 1 &= \frac{x^{p} - x}{x - 1} \notag \\
    \left(\phi_{p}\left(x\right) - 1\right)\left(x - 1\right) &= x^{p} - x \notag \\
    \left(\phi_{p}\left(x\right) - 1\right)\left(x - 1\right) + x &= x^{p} \notag \\
    p &= \ln\left(\frac{\left(\phi_{p}\left(x\right) - 1\right)\left(x - 1\right) + x}{x}\right).
\end{alignat}$$

That’s it.
