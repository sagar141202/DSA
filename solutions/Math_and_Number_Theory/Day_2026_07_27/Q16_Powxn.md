# Pow(x,n)
## Problem Statement
Implement a function `myPow(x, n)` that calculates the value of `x` raised to the power of `n`, where `x` is a floating-point number and `n` is an integer. The function should handle cases where `n` is negative and `x` is zero. The constraints are: `-100.0 < x < 100.0`, `-2^31 <= n <= 2^31 - 1`, and `-10^4 <= x^n <= 10^4`.

## Approach
We can use a recursive approach with exponentiation by squaring to solve this problem efficiently. This method reduces the number of multiplications required to calculate the power. If `n` is negative, we can use the property `x^-n = 1/x^n`.

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
        // Handle edge case where n is negative
        if (n < 0) {
            x = 1 / x;
            n = -n;
        }
        // Initialize result to 1
        double res = 1;
        // Use exponentiation by squaring
        while (n > 0) {
            // If n is odd, multiply result by x
            if (n % 2 == 1) res *= x;
            // Square x and divide n by 2
            x *= x;
            n /= 2;
        }
        return res;
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
- Exponentiation by squaring reduces the time complexity to O(log(n)).
- Handling negative `n` requires using the property `x^-n = 1/x^n`.
- The recursive approach with memoization can also be used, but it may cause a stack overflow for large `n`.