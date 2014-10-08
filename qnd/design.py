
import  scipy

class Design ( object ) :

    def __init__( self, point_type, scaler, scaled ) :
        """Container of scaled design points that can be alternatively
        represented as unscaled design points or Point-derived objects.  The
        Point-derived representation is used to evaluate constraints."""

        self.point_type = point_type
        self.scaler     = scaler
        self.scaled     = scaled

    def __len__( self ) :
        """Number of design points."""
        return len( self.scaled )

    def __getitem__( self, index ) :
        """Return a particular point."""
        unscaled = self.scaler.unscaled( self.scaled[ index ] )
        return self.point_type( *unscaled )

    @property
    def dims( self ) :
        """Dimensionality of the design space."""
        return self.scaler.dims

    @property
    def unscaled( self ) :
        """Unscaled coordinate matrix."""
        return self.scaler.unscaled( self.scaled )

    @property
    def points( self ) :
        """List of Point objects."""
        return [ self[ index ] for index in range( len( self ) ) ]

    @property
    def compliance( self ) :
        """True for Points satisfying constraints, False otherwise."""
        return scipy.array( [ point.is_compliant for point in self.points ] )

    def randomize( self, mask = None ) :
        """Randomizes a subset of points until they are all compliant.  If no
        mask is specified the entire design is randomized."""

        if mask is None :
            self.scaled = self.scaler.generate_scaled( len( self ) )
        else :
            if mask.any() :
                self.scaled[ mask ] = self.scaler.generate_scaled( mask.sum() )
            else :
                return
        return self.randomize( ~self.compliance )
