# Factorial Trailing Zeroes

## Problem Statement
The problem requires finding the number of trailing zeroes in the factorial of a given number `n`. The factorial of a number `n` (denoted as `n!`) is the product of all positive integers less than or equal to `n`. A trailing zero is a zero at the end of the number. For example, the factorial of 5 is `5! = 5 * 4 * 3 * 2 * 1 = 120`, which has 1 trailing zero. The input `n` will be a positive integer, and the output should be the number of trailing zeroes in `n!`. The constraints are `1 <= n <= 10^4`.

## Approach
The algorithm is based on the fact that trailing zeroes in `n!` are caused by the multiplication of 2 and 5. Since there are more factors of 2 than 5 in `n!`, we only need to count the factors of 5. We can use a loop to count the factors of 5 in `n!` by dividing `n` by powers of 5.

## Complexity
- Time: O(log n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int trailingZeroes(int n) {
        int count = 0;
        // count the factors of 5 in n!
        while (n > 0) {
            n /= 5;
            count += n;
        }
        return count;
    }
};
```

## Test Cases
```
Input: n = 5
Output: 1
Input: n = 10
Output: 2
```

## Key Takeaways
- The number of trailing zeroes in `n!` is determined by the number of factors of 5 in `n!`.
- We can use a loop to count the factors of 5 in `n!` by dividing `n` by powers of 5.
- The time complexity of the algorithm is O(log n) because we are dividing `n` by a constant factor (5) in each iteration.