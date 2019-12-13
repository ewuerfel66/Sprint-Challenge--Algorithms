#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) Given that `n` is fixed, this block of code is quite inefficient.
Every time the condition of the `while` loop is checked, n^3 is calculated.
Everytime `a` is altered within the `while` loop, n^2 is calculated.
Saving n^2 and n^3 as variables should reduce runtime. 

``` a = 0                       # 1
    while (a < n * n * n):      # 1:
      a = a + n * n                 # 1
```


b) This block of code is O(n) because it iterates through `range(n)` once.


```
    sum = 0                 # 1
    for i in range(n):      # n:
      j = 1                     # 1
      while j < n:              # 1
        j *= 2                      # 1
        sum += 1                    # 1
```


c) This is a recursive function that returns the amount of ears
associated with a given integer amount of bunnies. By subtracting one
from `bunnies` in each recursive call, we make our way toward the base
case of 0 bunnies having 0 ears.

```
    def bunnyEars(bunnies):             
      if bunnies == 0:                  # 1:
        return 0                            # 1:

      return 2 + bunnyEars(bunnies-1)   # Recursive Call
```

## Exercise II

def find_floor_f(floors, range=None):
    lower_range = midpoint = floors // 2    # 1            
    upper_range = midpoint + floors         # 1

    drop egg from midpoint                  # 1

    if egg breaks:                          # 1:
        find_floor_f(lower_range)               # Recursive Call
    else:                                   # 1:
        find_floor_f(upper_range)               # Recursive Call

