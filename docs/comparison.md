# Comparisons

MOA is one approach to solving these computations. Here we would like
to list alternatives and give the best comprison that we can. Please
correct this if it is wrong.

## Halide

Quotes from [issue 1 of moa](https://github.com/saulshanabrook/moa/issues/1)

What Halide offers is a methodology to automatically visit the state
space of possible schedules so that you can empirically measure what
the best execution schedule is for a particular piece of
hardware. That too fights with the idea of parallel hardware doing the
scheduling, but with many tensor products there are few write/read
dependencies, so the number of possible schedules is vast and their
paging behavior is difficult to predict without actual execution as
strides, page sizes, and concurrent pages will all vary among hw
systems.

 - detailed article: https://cacm.acm.org/magazines/2018/1/223877-halide/fulltext
 - repository: https://github.com/halide/Halide
 - first introduction talk: https://people.csail.mit.edu/jrk/halide12/
 - website: http://halide-lang.org/

Points Gleaned from Reading:
  - uses C++ templates to represent the calculation
  - C++ compiler then does optimizations (as oppesed to mathematical reductions from MOA)
  - compiles into LLVM code to target everythat that LLVM can target
  - used by google pixel phones and many other companies (adobe, mit, etc.)
  - repository https://github.com/halide/Halide and released by MIT 2012
  - used for dense arrays computations (like image processing)

Questions:
 - how does this address sparse computations?
 - does this do anything to remove temporaries automatically from a caluculation?
 - are there any mathematical motivations for operations? guarantees of optimality?



