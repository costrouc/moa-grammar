# Questions

 - several of the example files including `test_files/moa/lu.moa` have
   types not specified in the moa language `int` and for loops how
   does this fit into the MOA language / compiler optimizations /
   reducibility?
 
 - matrix multiplication is an example of a problem that does not
   really require coordination. However some problems like LU
   factorication and Gram-Schmidt look in MOA? Does it require loops
   how is that represented?
   
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
