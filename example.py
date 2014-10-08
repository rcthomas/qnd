#!/usr/bin/env python

import  scipy

import  qnd

class SmokePoint ( qnd.Point ) :

    def __init__( self, nickel_mass, ime_mass, unburned_mass, nickel_radius, opacity ) :
        self.nickel_mass    = nickel_mass
        self.ime_mass       = ime_mass
        self.unburned_mass  = unburned_mass
        self.nickel_radius  = nickel_radius
        self.opacity        = opacity

    @property
    def ejecta_mass( self ) :
        """Just the sum of the parts."""

        return self.nickel_mass + self.ime_mass + self.unburned_mass

    @property
    def kinetic_energy( self ) :
        """Nuclear energy released minus binding plus internal."""

        pass

    @property
    def rise_time( self ) :
        """Rise time in days estimated from a GP for instance."""

        pass

    @property
    def peak_luminosity( self ) :
        """Peak luminosity estimated from a GP for instance."""

        pass

    def _is_compliant( self ) :
        """Is this point okay, does it violate our custom constraints?"""

        if self.ejecta_mass < 0.6 :
            return False
        if self.ejecta_mass > 1.38 :
            return False
        return True

if __name__ == "__main__" :

    lower = scipy.array( [ 0.20, 0.20, 0.00, 0.00, 0.05 ] )
    upper = scipy.array( [ 1.38, 1.00, 0.10, 1.38, 0.25 ] )

    design = qnd.random_design( SmokePoint, lower, upper )
    print design.unscaled
