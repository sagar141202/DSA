# Pow(x,n)

## Problem Statement
Implement the `Pow(x, n)` function, which calculates the value of `x` raised to the power of `n` (`x` to the power `n`). The function should handle both positive and negative values of `n`. The input `x` is a double, and `n` is an integer. For example, `Pow(2.0, 3)` should return `8.0`, and `Pow(2.1, -3)` should return approximately `0.084`.

## Approach
We can solve this problem using recursion and the property of exponents that states `x` to the power `n` equals `x` times `x` to the power `n-1`. We'll also handle the case when `n` is negative by using the property `x` to the power `-n` equals `1` divided by `x` to the power `n`. Additionally, we can optimize the solution using the property `x` to the power `2n` equals the square of `x` to the power `n`.

## Complexity
- Time: O(log n)
- Space: O(log n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

double myPow(double x, int n) {
    // handle edge case where n is 0
    if (n == 0) return 1;
    
    // handle negative n
    if (n < 0) {
        x = 1 / x;
        n = -n;
    }
    
    // recursive case
    if (n % 2 == 0) {
        double halfPow = myPow(x, n / 2);
        return halfPow * halfPow;
    } else {
        double halfPow = myPow(x, (n - 1) / 2);
        return x * halfPow * halfPow;
    }
}

// or using iteration
double myPowIterative(double x, int n) {
    double res = 1;
    if (n < 0) {
        x = 1 / x;
        n = -n;
    }
    while (n > 0) {
        if (n % 2 == 1) res *= x;
        x *= x;
        n /= 2;
    }
    return res;
}
```

## Test Cases
```
Input: x = 2.0, n = 3
Output: 8.0
Input: x = 2.1, n = -3
Output: 0.084
Input: x = 2.0, n = 0
Output: 1.0
```

## Key Takeaways
- Use the property of exponents to reduce the problem size.
- Handle negative `n` by using the property `x` to the power `-n` equals `1` divided by `x` to the power `n`.
- Optimize the solution using the property `x` to the power `2n` equals the square of `x` to the power `n`.