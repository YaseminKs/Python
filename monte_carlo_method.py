# easy to read but slower

import random

def monte_carlo_pi( samples=1_000_000 ):
    inside_circle = sum( 1 for _ in range( samples ) if ( random.random()**2 + random.random()**2 ) <= 1 )
    return 4 * inside_circle / samples

print( "Estimated Pi:", monte_carlo_pi() )
