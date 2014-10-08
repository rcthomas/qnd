
import  scipy

from    design  import  Design
from    scaler  import  Scaler

def random_design( point_type, lower, upper, size = 100, rng = None ) :
    scaler = Scaler( lower, upper, rng )
    design = Design( point_type, scaler, scipy.zeros( ( size, scaler.dims ) ) )
    design.randomize()
    return design
