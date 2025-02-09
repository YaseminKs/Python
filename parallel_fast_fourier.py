import numpy as np
from concurrent.futures import ThreadPoolExecutor

def fft( x ):
    n = len( x )
    if n <= 1:
        return x

    even = fft( x[0::2] )
    odd = fft( x[1::2] )

    factor = np.exp( -2j * np.pi * np.arange( n ) / n )
    return np.concatenate( [even + factor[:n // 2] * odd, even + factor[n // 2:] * odd] )

def parallel_fft( x ):
    n = len( x )
    if n <= 1:
        return x

    with ThreadPoolExecutor() as executor:
        even_future = executor.submit( fft, x[0::2] )
        odd_future = executor.submit( fft, x[1::2] )
        even = even_future.result()
        odd = odd_future.result()

    factor = np.exp( -2j * np.pi * np.arange( n ) / n )
    return np.concatenate( [even + factor[:n // 2] * odd, even + factor[n // 2:] * odd] )

# Example usage
data = np.array( [complex( i, 0 ) for i in range( 8 )] )
result = parallel_fft( data )
print( result )
