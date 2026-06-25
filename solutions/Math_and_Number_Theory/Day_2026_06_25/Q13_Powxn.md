# Pow(x,n)

## Problem Statement
Implement a function `myPow(x, n)` that calculates the value of `x` raised to the power of `n`, where `x` is a floating-point number and `n` is an integer. The function should handle both positive and negative values of `n`. The input range for `x` is `-100.0 < x < 100.0`, and the input range for `n` is `-2^31 <= n <= 2^31-1`. The function should return the result of `x` raised to the power of `n`.

## Approach
The approach is to use a recursive division method to calculate the power. If `n` is even, we can divide `n` by 2 and calculate `x` raised to the power of `n/2`. If `n` is odd, we can divide `n-1` by 2 and calculate `x` raised to the power of `(n-1)/2`, then multiply the result by `x`.

## Complexity
- Time: O(log(n))
- Space: O(log(n))

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    double myPow(double x, int n) {
        // Handle negative n
        if (n < 0) {
            x = 1 / x;
            n = -n;
        }
        
        // Base case
        if (n == 0) return 1;
        
        // Recursive case
        if (n % 2 == 0) {
            double halfPow = myPow(x, n / 2);
            return halfPow * halfPow;
        } else {
            double halfPow = myPow(x, (n - 1) / 2);
            return x * halfPow * halfPow;
        }
    }
};
```

## Test Cases
```
Input: x = 2.0, n = 3
Output: 8.0
Input: x = 2.1, n = 3
Output: 9.261
Input: x = 2.0, n = -3
Output: 0.125
```

## Key Takeaways
- Use a recursive division method to calculate the power.
- Handle negative `n` by taking the reciprocal of `x` and making `n` positive.
- Use a base case to stop the recursion when `n` is 0.