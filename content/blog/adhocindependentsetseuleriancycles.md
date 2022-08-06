title:      Eulerian cycles for combinatorial independent sets determination
slug:       adhocindependentsets-euleriancycles
date:       2020-06-12 19:30
category:   Math        
tags:       graph theory, independent sets, algorithm, complexity, combinatorial, eulerian cycles
author:     Carolin Zöbelein
summary:    In the last post, we described a naive algorithm to determine independent sets and got a terrible complexity. Now, we want to grab this algorithm to use it as a base for an alternative way of independent set generation.
id:         post_0016   
basename:   adhocindependentsetseuleriancycles

This post is the second part of a series regarding combinatorial
independent sets determination.

-   First post of this series: [Ad hoc method for independent
    sets](https://blog.carolin-zoebelein.de/2020/05/adhocindependentsets.html)

In the last post, we described a naive algorithm to determine
independent sets and got a terrible complexity. Now, we want to grab
this algorithm to use it as a base for an alternative way of independent
set generation. Instead of putting edges in an arbitrary order into our
algorithm, we will consider properties of the set of edges $E$, given by
Eulerian cycles.

## Eulerian cycle expansions

For improving our algorithm, we will need Eulerian cycles.

**Definition 1** (Eulerian cycle)  
*An Eulerian cycle in an undirected graph is a cycle that uses each edge
exactly once. A graph which owns such a cycle is called Eulerian.*

*If $G$ is a connected graph, then the following statements are
equivalent:*

-   *$G$ is Eulerian*
-   *Every vertex $v \in V$ of $G$ have an even degree
    $\deg\left(v\right)$*
-   *The set $E$ of $G$ is the set union of all edges of pairwise
    disjunct cycles*

*This was proofed by Hierholzer \[HiWi73\].*

So, what we need is a connected graph which only has vertices with even
degree. Because, of course, not all graphs statisfy this conditions by
default, we will now think, how we can map a given graph $G$ to a graph
$G^{\prime}$ which statisfies the conditions, but still gives us the
searched independent sets of $G$, without increasing noticeable the full
algorithm complexity, finally.

### Connectivity

At first, let’s check if the graph $G$ is connected. This can be done by
breadth-first search with $\mathcal{O}\left(|V| + |E|\right)$. If yes,
we don’t have to do anything anymore regarding connectivity. In the case
of no, we have several independent, pairwise disconnected, subgraphs
$G_{0}, G_{1}, \dots$ which we can handle without much work. We
determine the independent sets $S_{G_{i}}$ for each $G_{i}$ separately.
After determining all independet sets, we finally have simply to combine
all of this $S_{G_{i}}$ with each other. To find all strongly components
of a graph we can use Tarjan’s algorithm \[Tarj72\] which also works
with $\mathcal{O}\left(|V| + |E|\right)$. Later, we will see that the
final independent sets can be easily derived from our partial results.

### Even degrees

The second condition for an Eulerian graph is regarding even degrees. At
first, let’s check the degree of each vertex in $G$. This is a trivial
thing with linear complexity. If yes, we don’t have to do anything
anymore regarding even degrees. In the case of no, we have to do some
modification of $G$. From basic graph theory we know that for every
graph $G$ we have $2|E| = \sum_{v_{i} \in V} \deg\left(v_{i}\right)$.
Hence, we know that we always have an even number of vertices with odd
degree. With this we can simply map our graph $G$ to an Eulerian graph
by connecting always two of our odd degree vertices $\{u,v\}$ by one new
introduced helper vertex $h \in H$ (be $H$ the set of helper vertices)
and hence we get the two new edges $\left(u,h\right)$ and
$\left(h,v\right)$. So, what will be the consequences of adding an
helper vertex to our graph, regarding the independent sets? We have two
possible cases here:

-   The helper vertex $h$ connects two vertices $u$ and $v$ which belong
    to the same independent set $S$ which means $u \in S \wedge v \in S$
    and hence $\left(u,v\right) \notin E$.  
    *Consequence:* Since $u$ and $v$ are still not directly connected
    with each other, they will still belong to the same independent set.
    Since, each of them have a connection to $h$, $h$ will become a
    member of an other, second, independent set. So, we will get our
    original independent set $S$ unchanged and any other second
    independent set with $S^{\prime} \cup \{h\}$.

-   The helper vertex $h$ connects two vertices $u$ and $v$ which belong
    to two different independent sets $S_{i}, S_{j}$ with
    $S_{i} \nsubseteq S_{j}$, which means
    $u \in S_{i} \wedge v \in S_{j}$ and hence
    $\left(u,v\right) \in E$.  
    *Consequence:* Since $u$ and $v$ are already directly connected,
    also with a connection to $h$ they will still both belong to two
    different sets. Since, each of them have a connection to $h$, $h$
    will become a member of an other, third, independent set. So, we
    will get our original two independent sets $S_{i}$ and $S_{j}$
    unchanged and any other third independent set with
    $S_{k} \cup \{h\}$.

We will come back to this, later.

## Eulerian cycle partitioning

After mapping our graph $G$ to an Eulerian one, we determine the
Eulerian cycles with Hierholzer’s algorithm \[HiWi73\] and complexity
$\mathcal{O}\left(|E|\right)$. Like already mentioned, a graph $G$ can
be disconnected into several subgraphs $G_{0}, G_{1}, \dots$. For each
of them we have to identify the Euler cycles. The outcome of this can be
written in a general way like as the following example:

$$\begin{equation}
    \underbrace{\left(\overbrace{\underset{0}{a_{1}},\underset{1}{b_{1}},\underset{2}{c_{1}}}^{C_{0}}, \overbrace{a_{2},\underset{3}{d_{1}},\underset{4}{e_{1}},\underset{5}{f_{1}}}^{C_{1}},\overbrace{b_{2}}^{C_{2}},\overbrace{e_{2}}^{C_{3}},\overbrace{a_{3}}^{C_{4}}\right)}_{G_{0}} \underbrace{\left(\overbrace{\underset{0}{g_{1}},\underset{1}{h_{1}},\underset{2}{i_{1}}}^{C^{\prime}_{0}},\overbrace{\underset{3}{g_{2}}}^{C^{\prime}_{1}}\right)}_{G_{1}}\cdots
\label{eq:eulercycles}
\end{equation}$$

Here, $a_{i}, b_{i}, \cdots, h_{i}, i_{i}$ are vertices of $V$, their
indices are the numbers of their appeareance and the numbers below them
are the numbering of the first appeareance order within the Eulerian
graph. In each graph we can find inner cycles $C_{i}$ which are
recognized through an additional appeareance of an already in the
sequence existing vertex. For our further steps, we will see, that it is
useful to cut a graph sequence exactly at this points.

What we want to do now, is to put this information of one graph $G_{i}$
in a more helpful data structure. For this we use a list of linked lists
for each $G_{i}$ in which we save for each cycle its size $s$, its first
element and the the position of this first element within the sequence
of all first appearences of numbers of the whole Eulerian sequence, (see
table 1), at all.

![GitHub
Logo](/blog/images/adhocindependentsets-euleriancycles/table1AdjacenceList.jpg)

We know the maximum number of edges of a graph $G$ is
$\frac{1}{2}\left(|V|^{2} - |V|\right)$ and that we have this value plus
one for entries of $G$, like in (). So we have a total complexity of
$\mathcal{O}\left(\left(\frac{1}{2}\left(|V|^{2} - |V|\right) + 1\right)^{2}\right) = \mathcal{O}\left(|V|^{4}\right)$
for generating all lists of linked lists of a given $G$, like that.

## Outlook

In the next post, we will use this information given by the eulerian
cycle to define an appropriate representation for a combinatorial
approach for determination of independent sets.

## References

<span class="csl-left-margin">\[HiWi73\] </span><span
class="csl-right-inline"><span class="smallcaps">Hierholzer, Carl</span>
; <span class="smallcaps">Wiener, Chr</span>: Über die Möglichkeit,
einen Linienzug ohne Wiederholung und ohne Unterbrechung zu umfahren.
In: *Mathematische Annalen* Bd. 6, Springer-Verlag (1873), Nr. 1,
S. 30–32</span>

<span class="csl-left-margin">\[Tarj72\] </span><span
class="csl-right-inline"><span class="smallcaps">Tarjan, Robert</span>:
Depth-first search and linear graph algorithms. In: *SIAM journal on
computing* Bd. 1, SIAM (1972), Nr. 2, S. 146–160</span>
