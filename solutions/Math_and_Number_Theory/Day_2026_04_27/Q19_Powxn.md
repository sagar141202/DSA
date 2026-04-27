# Pow(x,n)

## Problem Statement
Implement a function `myPow(x, n)` that calculates the value of `x` raised to the power of `n`, where `x` is a floating-point number and `n` is an integer. The function should handle cases where `n` is negative and `x` is zero. The input ranges are `-100.0 < x < 100.0` and `-2^31 <= n <= 2^31 - 1`. For example, `myPow(2.0, 3)` should return `8.0`, and `myPow(2.1, -3)` should return approximately `0.084`.

## Approach
The solution uses the concept of exponentiation by squaring, which reduces the number of multiplications required to calculate the power. This approach takes advantage of the fact that `x^n = (x^(n/2))^2` when `n` is even, and `x^n = x * (x^((n-1)/2))^2` when `n` is odd.

## Complexity
- Time: O(log(n))
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

double myPow(double x, int n) {
    // Handle edge case where n is 0
    if (n == 0) return 1;
    
    // Handle edge case where x is 0
    if (x == 0) return 0;
    
    // If n is negative, invert x and make n positive
    if (n < 0) {
        x = 1 / x;
        n = -n;
    }
    
    // Initialize result
    double res = 1;
    
    // Perform exponentiation by squaring
    while (n > 0) {
        // If n is odd, multiply result by x
        if (n % 2 == 1) res *= x;
        
        // Square x and divide n by 2
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
Input: x = 0, n = 0
Output: 1
```

## Key Takeaways
- Use exponentiation by squaring to reduce the number of multiplications.
- Handle edge cases where `n` is 0 or `x` is 0 separately.
- Invert `x` and make `n` positive when `n` is negative to simplify the calculation.