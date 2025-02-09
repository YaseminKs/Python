# Python: Uses multiprocessing to apply counting sort in parallel.

import numpy as np
import multiprocessing

def counting_sort( arr, exp ):
    n = len( arr )
    output = np.zeros( n, dtype=int )
    count = np.zeros( 10, dtype=int )

    for num in arr:
        count[( num // exp ) % 10] += 1
    count = np.cumsum( count )

    for i in range( n - 1, -1, -1 ):
        output[count[( arr[i] // exp ) % 10] - 1] = arr[i]
        count[( arr[i] // exp ) % 10] -= 1

    return output

def parallel_radix_sort( arr ):
    max_val = max( arr )
    exp = 1
    with multiprocessing.Pool( processes=multiprocessing.cpu_count() ) as pool:
        while max_val // exp > 0:
            arr = pool.apply( counting_sort, ( arr, exp ) )
            exp *= 10
    return arr

if __name__ == "__main__":
    arr = np.array( [170, 45, 75, 90, 802, 24, 2, 66] )
    sorted_arr = parallel_radix_sort( arr )
    print( sorted_arr )
