import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import stft

# Generate a sample signal
t = np.linspace( 0, 1.0, 1000 )
signal = np.sin( 2 * np.pi * 50 * t ) + np.sin( 2 * np.pi * 120 * t )

# Compute STFT
frequencies, times, Zxx = stft( signal, fs = 1000, nperseg = 100 )

# Plot the STFT
plt.pcolormesh( times, frequencies, np.abs( Zxx ), shading='gouraud' )
plt.title( 'Short-Time Fourier Transform (STFT)' )
plt.xlabel( 'Time [sec]' )
plt.ylabel( 'Frequency [Hz]' )
plt.colorbar()
plt.show()
