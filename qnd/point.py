
class Point ( object ) :

    """Base class for objects describing simulation parameters.  Derived-class
    initializers must to take a list of arguments in the same order as defined
    for the corresponding Design container."""
    
    @property
    def is_compliant( self ) :
        """True if point satisfies constraints, false otherwise."""
        return self._is_compliant()

    def _is_compliant( self ) :
        """Subclasses provide an implementation for this."""
        raise NotImplementedError
