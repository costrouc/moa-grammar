# References

## [A Reduction Semantics for Array Expressions: The PSI Compiler (1994)](http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.54.4307)

This paper gives an overview of the MOA language and how it can be
used to generate a compiler. 

1. compile MOA language ([examples](../test_files/moa/)) to AST
2. compute shape (rules defined) of each node in AST (given formal definitions)
3. apply reductions to AST in deterministic manner (rules defined)
4. finally compile reduced AST into code

It is important to note that future papers talk about how the AST
needs to be broken into several compilation steps.

## [Four Easy Ways to a Faster FFT](https://doi.org/10.1023/A:1020590506372) 10.1023/A:1020590506372

 - FFT implementation

Available on Research Gate.

The FFT is a special problem that involves a sparse matrix and
requires special tuning for each architecture for the
implementation. This paper gives an introduction to the DNF and ONF
representations.

MOA really excels in this problem due to the need for reshaping at
each iteration and temporary values.

Saddly this paper is not heavy on MOA and PSI calculus explanation.

A later paper [Applications of Conformal Computing techniques to
problems in computational physics: the Fast Fourier
Transform](https://doi.org/10.1016/j.cpc.2005.02.004) is much heavier
on the math.

## [Seminar](https://www.albany.edu/CC05/)

Introduction talk by Leonore gives highlights.

## [Parallelizing Optimal Multiple Sequence Alignment by Dynamic Programming](https://doi.org/10.1109/ISPA.2008.93)

Available on Research Gate.

This article discusses how the ONF and communication patterns can be
optimized with MOA. They model the communication cost (not determined
automatically...). They get provably optimal communication.


## [On minimizing materializations of array-valued temporaries](https://doi.org/10.1145/1186632.1186637)

**a must read** I probably did not understand correctly.

"monolithic" array operations. Nonmaterialization are mathematical
operators that simply shuffle the data (not changing it). For example
`transpose`, `cshift`, `reshape`, and `spread`. It is possible to
compile array these rearangements with appropriate tracking of the
indicies. Could be a great paper but I had a hard time following and
seeing the implications of psi calculus. Established a minimum bound
on the number of temporaries.

## [Generating indexing functions of regularly sparse arrays for array compilers](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.53.7877&rep=rep1&type=pdf)

Talks about how the indexing function can be generalized for sparse arrays.

## [Scalable, Portable, Verifiable Kronecker Products on Multi-scale Computers](https://doi.org/10.1007/978-3-319-04280-0_14)

**must read**

- Kroneker Product implementation

Paper discusser ONF and DNF and how it is applied using psi calculus. Also discuses how the algorithm is faster due to the elimination of temporaries.

## [A uniform way of reasoning about array-based computation in radar: Algebraically connecting the hardware/software boundary](https://doi.org/10.1016/j.dsp.2005.02.003)

link: https://people.csail.mit.edu/bushl2/rpi/portfolio/hpec/cites/0-mullin_mit_radar.pdf

 - matrix multiply and QR factorization implementation.

Great paper on theory.



