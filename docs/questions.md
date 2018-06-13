# Questions

 - several of the example files including `test_files/moa/lu.moa` have
   types not specified in the MOA language `int` and `for loops` how
   does this fit into the MOA language / compiler optimizations /
   reducibility?
 
 - matrix multiplication is an example of a problem that does not
   really require sequential execution. However some problems do like
   LU factorication and Gram-Schmidt. How does this look in MOA? Does
   it require for loops how is that represented?
   
 - numpy has a convenient syntax for selecting a subset of element
   based on a condition for example `A[A > 5] * 6` returns a new array
   composed of all the elements greater than five and multiplied
   by 6. The shape also changes in this calculations suppose A is
   initially shape `<N M>` goes to `<K>`. This modifies the shape and
   also the gamma function for the array. 
   - the best current idea for this implementation would be to put a
     condition on the gamma function where it checks for the next
     element that satisfies the condition.
     
 - Does MOA have any way of determining the best way to split the data
   for a distributed computation? Can it do this based on optimization
   and finding the most used and least used data.
   
 - Suppose we have a computation where a vector has shape `<N>` and we
   are going distribute the vector for a computation among `p`
   processors and `N` is not divisible by `p`. Is it safe to reshape
   the vector to `<p n>` where `p*n` is slightly larger than N? Does
   MOA indexing allow us to do this? How does this work with higher
   dimensional tensors?

 - What guarantees does the DNF representation give use? Minimize
   intermediate results (any others)? Does this property of MOA
   address the fact that many naive techniques for working with sparse
   arrays can lead to dense arrays. Is this a way around this problem?
   
 - In a perfect world a person would be able to write a complex
   computation that requires significant optimization. For example
   `||A multiply B multiply C - D||_F `. Do you believe MOA will be
   able to compile this expression down into effecient code from such
   a high level description?
   
 - In a paper you mention an implementation of matrix multiply `A x B
   x C` but performance was not mentioned. Is there a reason for this?

 - (unfair question) This is a very hard problem in numerical
   computing. Many people have tried this with heuristic based
   optimization and everyone is working towards this problem. I think
   its fair to say that everyone in the field is sceptical that the
   process can be "automated". Why has MOA not been adopted heavily in
   the field? Also what are the downsides of this technique that has
   prevented addoption? Reading the work this method sounds "too good
   to be true"

 - Hailide targets image processing. Many of these transformations
   require weighting local arrays. For instance blur. How would this
   look in MOA?
