#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) Given that `n` is fixed, this block of code is quite inefficient.
Every time the condition of the `while` loop is checked, n^3 is calculated.
Everytime `a` is altered within the `while` loop, n^2 is calculated.
Saving n^2 and n^3 as variables should reduce runtime.

The runtime of this code is dependent on the difference between n^3 and n^2.
With `a=0` this loop will run on the order of `n` times as shown below:


Take `i` as the number of iterations, and the simple case where a_0 = 0:

The `while` condition is met when:
  a = n^3 --> but a_0 = 0  and a_i = i * n^2
    Therefore...

i * n^2 = n^3
  Therefore...

i = n

``` a = 0                       # 1
    while (a < n * n * n):      # 1:
      a = a + n * n                 # 1
```


b) This block of code is O(n) because it iterates through `range(n)` once.
For each `i` in `range(n)` the `while` loop figures out how many times `j=1` must
be doubled to be greater than `i`. The `sum` variable keeps track of the amount of
times `j` is doubled throughout the `while` loop.

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

```
def find_floor_f(floors, range=None):
    lower_range = midpoint = floors // 2    # 1            
    upper_range = midpoint + floors         # 1

    drop egg from midpoint                  # 1

    if egg breaks:                          # 1:
        find_floor_f(lower_range)               # O(n/2), O(n/4), O(n/8)
    else:                                   # 1:
        find_floor_f(upper_range)               # O(n/2), O(n/4), O(n/8)
```

The order of the recursive calls looks like a convergent geometric series.
For each recursive call, the sum converges to O(2n) ~ O(n). Since only one
call can be made for each prior call (because of the if/elif structure) this
entire function is also O(n).
