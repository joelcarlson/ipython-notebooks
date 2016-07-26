from pprint import pprint
import math

"""
Non-recursive Permutation Algorithm

Description
-----------
This is an implementation of an algorithm
that utilizes a swapping and reversing mechanism
to produce permutations of a list of numbers. 

Time complexity ~O(N)

Usage
------

Decide on the length of the list, N, 
and run perm(N)

Returns
------

A list of lists of permutations 

See Also
------
https://goo.gl/eMGIW3
https://goo.gl/agk0Mu
https://goo.gl/Ix0IC8
"""

def permutation(N):
    """Create a list of lists of permutations
    of length N
    """
    # Create a matrix to be filled with perms
    mat = [[0 for idx in range(N)] 
              for permutation in range(math.factorial(N))]

    L = sorted(range(N))   
    # Set the first value to a copy of the original sorted list       
    mat[0] = L[:]
    perm_idx = 1
    while perm_idx < len(mat):

        #1. Let i be the last index such that input[i] < input[i + 1]. 
        for idx, val in enumerate(L):
            # Control for IndexError
            if idx < len(L) - 1:
                if L[idx] < L[idx + 1]:
                    i = idx

        #2. Let j be the last index such that input[i] < input[j].
        for idx, val in enumerate(L):
            if L[i] < L[idx]:
                j = idx

        #Swap input[i] with input[j].        
        L[i], L[j] = L[j], L[i]

        #4. Reverse input[i + 1] through input[input.length - 1].
        L = L[0:i + 1] + list(reversed(L[i+1:]))
        mat[perm_idx] = L[:]
        perm_idx += 1
        
    return mat

if __name__ == "__main__":
    L = 4
    pprint(permutation(L))

