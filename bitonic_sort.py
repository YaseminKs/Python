def compare_and_swap( arr, i, j, ascending ):
    if( ascending and arr[i] > arr[j] )or( not ascending and arr[i] < arr[j] ):
        arr[i], arr[j] = arr[j], arr[i]  # Swap elements

def bitonic_merge( arr, low, count, ascending ):
    if count > 1:
        mid = count // 2
        for i in range( low, low + mid ):
            compare_and_swap( arr, i, i + mid, ascending )
        
        bitonic_merge( arr, low, mid, ascending )
        bitonic_merge( arr, low + mid, mid, ascending )

def bitonic_sort( arr, low, count, ascending ):
    if count > 1:
        mid = count //  2
        bitonic_sort( arr, low, mid, True )   # Sort first half in ascending order
        bitonic_sort( arr, low + mid, mid, False )  # Sort second half in descending order
        bitonic_merge( arr, low, count, ascending )  # Merge the sequence

def sort_bitonic( arr ):
    bitonic_sort( arr, 0, len( arr ), True )  # Sort entire array in ascending order

# Example usage
arr = [ 3, 7, 4, 8, 6, 2, 1, 5 ]  # Example array
print( "Original array:", arr )

sort_bitonic( arr )  # Perform bitonic sort

print( "Sorted array:", arr )
