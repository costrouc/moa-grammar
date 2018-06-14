**All issues and contributions should be done on
[Gitlab](https://gitlab.com/costrouc/moa-grammar). Github is used only as a
mirror for visibility**

<table>
<tr>
  <td>Build Status</td>
  <td> <a href="https://gitlab.com/costrouc/moa-grammar/pipelines"> <img
src="https://gitlab.com/costrouc/moa-grammar/badges/master/pipeline.svg"
alt="gitlab pipeline status" /> </a> </td>
</tr>
<tr>
  <td>Coverage</td> <td><img src="https://gitlab.com/costrouc/moa-grammar/badges/master/coverage.svg" alt="coverage" /></td>
</tr>
</table>

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


# Contributing

All contributions, bug reports, bug fixes, documentation improvements,
enhancements and ideas are welcome. These should be submitted at the
[Gitlab repository](https://gitlab.com/costrouc/moa-grammar). Github
is only used for visibility.

# License

MIT
