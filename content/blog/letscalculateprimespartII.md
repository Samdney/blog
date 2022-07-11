title:      Let`s calculate primes! Part II - Intersection of times tables
date:       2017-12-29 22:32
category:   Math
tags:       primes, number theory
author:     Carolin Zöbelein
summary:    Describtion of prime numbers part 2.


Ok. What is the intersection of two or more times tables in our new representation? That is easy! It is the sum of this times tables. Let`s look a the addition of the two times tables 
$$x_{1, j} = 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34, 37, 40 \dots$$
and
$$x_{2, j} = 7, 12, 17, 22, 27, 32, 37, 42, \dots$$. 
and the result

$$
001001001001001001001001001001001001001000 \\ 
100001000010000100001000010000100001000000 \\    
  \\
101002001011001101002001011001101002001000
$$.  

Yes, it is easy. At the places, at which we have no integer divisible numbers, we have zeros. That is great!  
At the places, at which we have divisible numbers, we have an 1, that`s also good, but also a 2, at some places. This is not good! It means both times tables have the same divisible number.  
If we only add two numbers, this can still going well. But assume we add more times tables, so that we finally have more than 9 times tables with the same integer divisible number. This leads us to troubles, since in this case we would have a carry, which would falsify the next digits and our final result would have no meaning anymore.  

In the next posts, we will see that this is not really a problem, since we have the ability to eliminate the *not so nice* numbers.  
But, before we will do this, we will examine the sum formula for the sum over several times tables, at first.
