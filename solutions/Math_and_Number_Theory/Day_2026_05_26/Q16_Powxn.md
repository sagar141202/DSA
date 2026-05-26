# Pow(x,n)

## Problem Statement
Implement the `pow(x, n)` function, which calculates the value of `x` raised to the power of `n` (i.e., `x^n`). The function should handle both positive and negative values of `n`. The input `x` is a floating-point number, and `n` is an integer. Return the result as a floating-point number. For example, `pow(2.0, 3)` should return `8.0`, and `pow(2.1, -2)` should return approximately `0.2244898`.

## Approach
The algorithm uses the divide and conquer approach to calculate the power in logarithmic time complexity. If `n` is even, we can calculate `pow(x, n)` as `(pow(x, n/2))^2`. If `n` is odd, we can calculate `pow(x, n)` as `x * (pow(x, (n-1)/2))^2`.

## Complexity
- Time: O(log n)
- Space: O(log n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

double myPow(double x, int n) {
    // Handle negative n
    if (n < 0) {
        x = 1 / x;
        n = -n;
    }
    
    // Base case
    if (n == 0) return 1;
    
    // Recursive case
    double halfPow = myPow(x, n / 2);
    if (n % 2 == 0) {
        return halfPow * halfPow;
    } else {
        return x * halfPow * halfPow;
    }
}
```

## Test Cases
```
Input: x = 2.0, n = 3
Output: 8.0
Input: x = 2.1, n = -2
Output: 0.2244898
Input: x = 2.0, n = 0
Output: 1.0
```

## Key Takeaways
- Use the divide and conquer approach to calculate the power in logarithmic time complexity.
- Handle negative `n` by taking the reciprocal of `x` and changing the sign of `n`.
- Use recursion to calculate the power for both even and odd `n`.