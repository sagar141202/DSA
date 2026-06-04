# Pow(x,n)

## Problem Statement
Implement a function `myPow(x, n)` that calculates the value of `x` raised to the power of `n`, where `x` is a floating point number and `n` is an integer. The function should handle cases where `n` is negative, and the result should be a double precision floating point number. For example, `myPow(2.0, 3)` should return `8.0`, and `myPow(2.1, -3)` should return approximately `0.084`.

## Approach
The algorithm uses the concept of exponentiation by squaring to achieve efficient calculation of `x` raised to the power of `n`. This method reduces the number of multiplications required by using the property that `x^(2n) = (x^n)^2`. The function also handles negative `n` by calculating the reciprocal of `x` raised to the power of the absolute value of `n`.

## Complexity
- Time: O(log n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

double myPow(double x, int n) {
    // Handle negative n by calculating the reciprocal
    if (n < 0) {
        x = 1 / x;
        n = -n;
    }
    // Initialize result to 1
    double result = 1;
    // Use exponentiation by squaring
    while (n > 0) {
        // If n is odd, multiply result by x
        if (n % 2 == 1) {
            result *= x;
        }
        // Square x and divide n by 2
        x *= x;
        n /= 2;
    }
    return result;
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
- Exponentiation by squaring reduces the time complexity to O(log n)
- Handling negative `n` requires calculating the reciprocal of `x` raised to the power of the absolute value of `n`
- The function should return a double precision floating point number to handle decimal results