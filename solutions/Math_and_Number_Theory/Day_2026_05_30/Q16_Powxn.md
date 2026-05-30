# Pow(x,n)

## Problem Statement
Implement the `pow(x, n)` function, which calculates the value of `x` raised to the power of `n` (i.e., `x^n`). The function should handle both positive and negative values of `n`. The input `x` is a double, and `n` is an integer. For example, `pow(2.0, 3)` should return `8.0`, and `pow(2.0, -3)` should return `0.125`. The constraints are: `-100.0 < x < 100.0` and `-2^31 <= n <= 2^31 - 1`.

## Approach
The algorithm uses the divide and conquer approach to reduce the number of multiplications required. If `n` is even, `x^n` is calculated as `(x^(n/2))^2`. If `n` is odd, `x^n` is calculated as `x * (x^((n-1)/2))^2`. This approach reduces the time complexity to logarithmic.

## Complexity
- Time: O(log(n))
- Space: O(log(n))

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

double myPow(double x, int n) {
    // handle negative n
    if (n < 0) {
        x = 1 / x;
        n = -n;
    }
    // base case
    if (n == 0) return 1;
    // recursive case
    if (n % 2 == 0) {
        double halfPow = myPow(x, n / 2);
        return halfPow * halfPow;
    } else {
        double halfPow = myPow(x, (n - 1) / 2);
        return x * halfPow * halfPow;
    }
}
```

## Test Cases
```
Input: x = 2.0, n = 3
Output: 8.0
Input: x = 2.0, n = -3
Output: 0.125
Input: x = 2.1, n = 3
Output: 9.261
```

## Key Takeaways
- Use the divide and conquer approach to reduce the number of multiplications required.
- Handle negative `n` by inverting `x` and making `n` positive.
- Use recursion to calculate `x^n` for both even and odd `n`.