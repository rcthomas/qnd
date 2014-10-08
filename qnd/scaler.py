
import  scipy

class Scaler ( object ) :

    """Transforms linearly between scaled and unscaled design point
    representations.  The scaled domain is a [-1,+1] (inclusive boundary)
    hypercube."""

    def __init__( self, lower, upper, rng = None ) :
        """Initialize with lower and upper bounds."""

        self.lower  = lower
        self.upper  = upper
        self.rng    = rng or scipy.random.RandomState()
        self._u2s   = 2.0 / ( self.upper - self.lower )
        self._s2u   = 1.0 / self._u2s

    @property
    def dims( self ) :
        """Dimensionality of design space."""
        return len( self.lower )

    def scaled( self, unscaled ) :
        """Transform unscaled representation to scaled representation."""
        return self._u2s * ( unscaled - self.lower ) - 1.0

    def unscaled( self, scaled ) :
        """Transform scaled representation to unscaled representation."""
        return self._s2u * ( scaled + 1.0 ) + self.lower

    def generate_scaled( self, size = 1, resolution = 6 ) :
        """Generate random scaled design points."""

        bounds = 10 ** resolution
        shape  = self.dims if size == 1 else ( size, self.dims )
        return self.rng.random_integers( -bounds, bounds, shape ) / float( bounds )
