"""
Write program to count the number of bits that are set to 1 in a non-negative integer.

The function signature 'count_bits(x: int) -> int:' indicates that the function accepts an int and returns an int
    while loop:  program performs O(1) computations per bit, thus the time complexity is O(n) where n := number of bits needed to represent the integer
"""
def count_bits(x: int) -> int: # accepts an int, returns an int
    num_bits = 0
    while x: #loop continues until x=0
        num_bits += x & 1   # program ands the lowest bit of x with 1
        x >>= 1 # right shift bits by 1
        # performs O(1) computations per bit, thus the time complexity is O(n) where n := number of bits needed to represent the integer
    return num_bits