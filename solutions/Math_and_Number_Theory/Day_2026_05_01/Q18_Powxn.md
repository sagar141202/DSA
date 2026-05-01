# Pow(x,n)

## Problem Statement
Implement a function `myPow(x, n)` that calculates the value of `x` raised to the power of `n`, where `x` is a floating-point number and `n` is an integer. The function should handle cases where `n` is negative and `x` is zero. The input constraints are: `-100.0 < x < 100.0` and `-2^31 <= n <= 2^31 - 1`. For example, `myPow(2.0, 3)` should return `8.0`, and `myPow(2.1, -3)` should return approximately `0.084`.

## Approach
The solution uses a divide-and-conquer approach to calculate the power in logarithmic time complexity. It handles the base cases where `n` is zero or `x` is zero, and then recursively calculates the power for positive and negative `n`. The key idea is to use the property `x^n = (x^(n/2))^2` for even `n` and `x^n = x * (x^((n-1)/2))^2` for odd `n`.

## Complexity
- Time: O(log(n))
- Space: O(log(n))

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

double myPow(double x, int n) {
    // Base case: anything raised to the power of 0 is 1
    if (n == 0) return 1;
    
    // If n is negative, calculate the reciprocal
    if (n < 0) {
        x = 1 / x;
        n = -n;
    }
    
    // Recursive case: calculate the power using divide-and-conquer
    return (n % 2 == 0) ? myPow(x * x, n / 2) : x * myPow(x * x, n / 2);
}
```

## Test Cases
```
Input: x = 2.0, n = 3
Output: 8.0
Input: x = 2.1, n = -3
Output: 0.084
Input: x = 0.0, n = 0
Output: 1.0
```

## Key Takeaways
- Use a divide-and-conquer approach to calculate the power in logarithmic time complexity.
- Handle base cases where `n` is zero or `x` is zero.
- Use the property `x^n = (x^(n/2))^2` for even `n` and `x^n = x * (x^((n-1)/2))^2` for odd `n` to reduce the problem size.