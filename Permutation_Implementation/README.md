
## Non-Recursive Permutation Algorithm

Contained in this repo is an implentation of a method for generating permutations of 
the elements of a list of length N. 

## Usage

Usage for the algorithm is extremely simple, as it is just a single function. 

Import the package, choose N, and run the function:

```python
from permutation import permutation

N = 3
permutation.permutation(N)
```

        [[0, 1, 2],
         [0, 2, 1],
         [1, 0, 2], 
         [1, 2, 0], 
         [2, 0, 1], 
         [2, 1, 0]]


Here is a visualization of the algorithm in action, permuting a list of 4 (each color represents a digit):

<img src="https://raw.githubusercontent.com/joelcarlson/GravityImageFilter/master/output/source.png" />