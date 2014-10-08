qnd
===

Quick and dirty but pretty good designs.

Main Idea
---------

The main idea is to have a re-usable Python framework for making quick and dirty
but still pretty good initial designs for computer simulations.  The designs are
probably not optimal but should be a good starting point for sequential designs
especially for constructing surrogate models.  We do not assume that bounds on
the simulation space are hypercubic or easily map to a hypercube.

Example Usage
-------------

Sub-class `Point` like so:

    class Cake ( Point ) :
        def __init__( self, flour, sugar, milk, eggs ) :
            ...

        def _is_compliant( self ) :
            if sugar > flour :
                return False
            return True

Then you just make a design of it using package level function `random_design`
like so:

    design = random_design( Cake, lower, upper )

Where `lower` and `upper` are just lower and upper bounds on each of the
parameters your class's initializer takes.  Then you have a starting design that
you need to iterate.

FIXME Explain that part.
