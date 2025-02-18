import numpy as np
import pywt
import matplotlib.pyplot as plt

# Generate a sample signal
t = np.linspace( 0, 1, 1000 )
signal = np.sin( 2 * np.pi * 50 * t ) + np.sin( 2 * np.pi * 120 * t )

# Perform Discrete Wavelet Transform
coeffs = pywt.wavedec( signal, 'db4', level=4 )

# Plot the original signal and DWT coefficients
plt.figure( figsize=( 10, 8 ) )
plt.subplot( 5, 1, 1 )
plt.plot( t, signal )
plt.title( 'Original Signal' )

for i, coeff in enumerate( coeffs ):
    plt.subplot( 5, 1, i + 2 )
    plt.plot( coeff )
    plt.title( f'DWT Coefficients Level { i }' ) 

plt.tight_layout()
plt.show()
