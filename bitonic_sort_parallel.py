import multiprocessing

def compare_and_swap( arr, i, j, ascending ):
    """Compares and swaps elements if they are not in the correct order."""
    if( ascending and arr[i] > arr[j] )or( not ascending and arr[i] < arr[j] ):
        arr[i], arr[j] = arr[j], arr[i]

def bitonic_merge( arr, low, count, ascending ):
    """Merges two bitonic sequences."""
    if count > 1:
        mid = count // 2
        processes = []
        for i in range( low, low + mid ):
            p = multiprocessing.Process( target=compare_and_swap, args=( arr, i, i + mid, ascending ) )
            processes.append( p )
            p.start()
        
        for p in processes:
            p.join()
        
        bitonic_merge( arr, low, mid, ascending )
        bitonic_merge( arr, low + mid, mid, ascending )

def bitonic_sort( arr, low, count, ascending ):
    """Recursively divides the array and sorts the subarrays."""
    if count > 1:
        mid = count // 2
        p1 = multiprocessing.Process( target=bitonic_sort, args=( arr, low, mid, True ) )  # Ascending order
        p2 = multiprocessing.Process( target=bitonic_sort, args=( arr, low + mid, mid, False ) )  # Descending order
        p1.start()
        p2.start()
        p1.join()
        p2.join()

        bitonic_merge( arr, low, count, ascending )

def parallel_bitonic_sort( arr ):
    """Wrapper function to start parallel bitonic sort."""
    bitonic_sort( arr, 0, len( arr ), True )

# Example usage
if __name__ == "__main__":
    arr = multiprocessing.Array( 'i', [ 3, 7, 4, 8, 6, 2, 1, 5 ] )  # Shared memory array
    print( "Original array:", list( arr ) )

    parallel_bitonic_sort( arr )  # Perform parallel bitonic sort

    print( "Sorted array:", list( arr ) )
