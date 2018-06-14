# Design

This is a document that is used to help clarify the implementation and
the assumptions being made. It also aims to provide a roadmap towards
the actual implementation and allow for criticism before any specific
design is chosen.

This project is already on great footing due to a formal specification
of the MOA grammar which allows us to have most of the design
decisions already made.

 - sparse arrays have been worked out in MOA [see issue 1](https://github.com/saulshanabrook/moa/issues/1#issuecomment-396812087)

 - MOA is the algebra
 - PSI Calculus is the reduction

## History:
 - Joseph Sylvester (invented matrix)
 - Phil Abrams (72 Stanford)
 - Alan Perl (should be in compilers)


DNF non machine optimized form.

ONF only optimizes based on size. At small sizes some things don't
matter. Fits in cache, distributed etc.

