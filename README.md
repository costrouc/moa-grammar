# Mathematics of Arrays (MOA)

The purpose of this project is to help in understanding the MOA
grammar and be able to visualize the resulting ASTs. Work will
initially be based on the psi compiler written by [Lenore
Mullin](references/psi-compiler.pdf). 

The first step is to rewrite the compiler in Python. Not for
performance reasons but in order to explore the results and iterate
quickly.

Work:
 - [ ] compiler will be rewritten in Python
   - [X] lexer of tokens
   - [X] yacc of expressions works with most moa files (see note [1])
   - [ ] calculate resulting shape at each expression
   - [ ] reduce ast with psi compiler rules
 - [ ] visualize the resulting AST for different problems
 - [ ] compute number of flops required for calculation and predict performance
 - [ ] write FFT, Matrix Multiply, and chained operations

Notes:
  - 6/10/2018
    - [1] `test_files/examples/lu.moa` contains for loops and integers in
      function call. Why is this used and how does this affect the
      pure MOA language?
    - [2] `A[A > 5]` changes the shape of an array in a dynamic
      manner. How to capture this.
