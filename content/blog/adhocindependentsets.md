title:      Ad hoc method for independent sets
slug:       adhocindependentsets
date:       2020-05-20 19:30
category:   Math        
tags:       graph theory, independent sets, algorithm, complexity
author:     Carolin Zöbelein
summary:    Today, we want to determine indpendent sets of an arbitrary undirected graph. Which can be done by a trivial ad hoc method, described as follows...
id:         post_0014   
basename:   adhocindependentsets

Today, we want to determine indpendent sets of an arbitrary undirected
graph. Which can be done by a trivial ad hoc method, described as
follows.

## Algorithm

We have given an arbitrary undireced graph $G = \left(V, E\right)$ with
$\deg\left(u_{i}\right) \geq 1$ for all $u_{i} \in V$. The set
$V_{0} \subseteq V$ of vertices with $\deg\left(u_{i}\right) = 0$ will
not be considered. Since, we are interested in the independent sets of
$G$, the set $V_{0}$ is a trivial case which, and it’s subsets, can be
simply added to any final solution of independent sets. Our following
considerations will work for every arbitrary kind of graph, so we don’t
have to make any other further assumption regarding possible special
kinds of graphs respectively sub-graphs, at the moment.

We start our independent set generation with the assumption that all
edges $\left(u_{i}, u_{j}\right) \in E$ are removed from our graph $G$.
For this trivial case, we would have the one largest independet set easy
given by
$S_{0} := \{u_{1}, u_{2}, u_{3}, u_{4}, \dots, u_{|V|-1}, u_{|V|}\}$.

Now, we take an arbitrary edge $e_{1} := \left(u_{1}, u_{2}\right)$ from
the set of the belonging edges $E$ of $G$. From the definition of an
independent set follows that $u_{1}$ and $u_{2}$ can not be element of
the same independent set of the same time. Since
$u_{1} \in S_{0} \wedge u_{2} \in S_{0}$ is given, we have to split
$S_{0}$ into the two new independet sets
$S_{0} = \{u_{1}, u_{3}, u_{4}, \dots, u_{|V|-1}, u_{|V|}\}$ and
$S_{1} = \{u_{2}, u_{3}, u_{4}, \dots, u_{|V|-1}, u_{|V|}\}$.

In the next step, we take edge $e_{2}$. Here, we have now to differ
between three cases. The two vertices of $e_{2}$ both lies completely in
$S_{0}$ or both lies in $S_{1}$ or in $S_{0}$ and $S_{1}$, at the same
time. Which means our possible outcome for
$e_{2} := \left(u_{1}, u_{3}\right)$ would be
$S_{0} \setminus \{u_{1}\}$, $S_{0} \setminus \{u_{3}\}$ and $S_{1}$, or
for $e_{2} := \left(u_{2}, u_{3}\right)$ we get $S_{0}$,
$S_{1} \setminus \{u_{2}\}$ and $S_{1} \setminus \{u_{3}\}$, or finally
for $e_{2} := \left(u_{3},u_{4}\right)$ we get
$S_{0} \setminus \{u_{3}\}$, $S_{0} \setminus \{u_{4}\}$,
$S_{1} \setminus \{u_{3}\}$ and $S_{1} \setminus \{u_{4}\}$.

So, we see that we can generate all of our independent sets by a simple,
naive way of taking an edge of $E$ and looking if this edge is an
element of an already generated independet set $S_{i}$. If yes then
split this set into two new ones, by copy $S_{i}$ to a second set
$S_{j}$ and removing the first vertex of $e$ from $S_{i}$ and removing
the second vertex of $e$ from $S_{j}$, else nothing has to be done.

By doing this for all edges $e$ of $E$, we finally get all independent
sets of $G$.

## Complexity

The complexity of this algorithm is easy to determine. Assume we have
given the worst case scenario of a complete graph $G$ (a graph in which
every pair of distinct vertices is connected by an unique edge) with
$|V|$ vertices and edges whose number is given by
$|E| = \tbinom{|V|}{2} = \frac{1}{2}|V|^{2} - \frac{1}{2}|V|$. To
determine all independent sets, we have to do our algorithm for $|E|$
steps, in which we will have to check for this edge in every already
existing independent set and finally split it into two. Hence, in the
$|E|$’th step, we have to check $2^{|E|}$ independent sets for the
current edge. For the complexity we get with this
$\mathcal{O}\left(2^{|V|^{2}}\right)$.

## Outlook

All of this seems not to look very exciting, but we will see that we can
derive nice things from it, in future blog posts.
