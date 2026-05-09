# Pow(x,n)

## Problem Statement
Implement a function `myPow(x, n)` that calculates the value of `x` raised to the power of `n`, where `x` is a floating-point number and `n` is an integer. The function should handle cases where `n` is negative and `x` is zero. The constraints are: `-100.0 < x < 100.0`, `-2^31 <= n <= 2^31 - 1`, and `-10^4 <= x^n <= 10^4`.

## Approach
The algorithm uses the concept of exponentiation by squaring to reduce the number of multiplications required. If `n` is negative, the function calculates `1 / myPow(x, -n)`. The base case is when `n` is 0, in which case the function returns 1.

## Complexity
- Time: O(log(n))
- Space: O(1)

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
    
    // initialize result
    double res = 1;
    
    // exponentiation by squaring
    while (n > 0) {
        // if n is odd, multiply result by x
        if (n % 2 == 1) res *= x;
        
        // square x and divide n by 2
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
Input: x = 2.1, n = 3
Output: 9.261
Input: x = 2.0, n = -3
Output: 0.125
```

## Key Takeaways
- Use exponentiation by squaring to reduce the number of multiplications.
- Handle negative `n` by calculating `1 / myPow(x, -n)`.
- Be mindful of edge cases, such as `n` being 0 or `x` being zero.