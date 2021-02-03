"""Question: How would you compute the parity of a very large number of 64-bit words?
COMMIT TO MEMORY: Bit Fiddling Trick, x & (x-1) equals x with the lowest 1 dropped.

"""

def parity_shift(x : int) -> int:
    result = 0
    while x:
        result += x & 1
        x >>= 1 # the algorithm right shifts bits until they are all zero
    return result

def parity_bit_drop(x : int) -> int:
    result = 0
    while x:
        result ^= 1
        x &= x - 1 # Drops the lowest set bit
        # therefore, the complexity of this algorithm is O(k), where k = number of 1s set
    return result

def parity_bit(x : int) -> int:
    result = 0
    # notice 11011001 has the same parity as p(p(1101) p(1001))
    # notice a xor b will be 1 if the parity of ab is 1
    bit_length = 16
    return (PRECOMPUTED_PARITY(x >> bit_length * 4) ^ PRECOMPUTED_PARITY(x >> bit_length * 3) ^
            PRECOMPUTED_PARITY(x >> bit_length * 2) ^ PRECOMPUTED_PARITY(x >> bit_length))

# for computing the parity of a large number of large words, it may be more efficient
# to cache a table of PRECOMPUTED_PARITY BITS
