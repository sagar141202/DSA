# Pow(x,n)

## Problem Statement
Implement a function `myPow(x, n)` that calculates the value of `x` raised to the power of `n`, where `x` is a real number and `n` is a 32-bit signed integer. The function should handle cases where `n` is negative, zero, or positive. The input range is `-2^31 <= n <= 2^31-1` and `-10^4 <= x <= 10^4`. The output should be a double precision floating point number. For example, `myPow(2.0, 3)` returns `8.0`, `myPow(2.1, 3)` returns `9.261`, and `myPow(2.0, -3)` returns `0.125`.

## Approach
Use the divide and conquer approach to calculate the power in logarithmic time complexity. If `n` is even, calculate `myPow(x, n/2)` and square the result. If `n` is odd, calculate `myPow(x, (n-1)/2)`, square the result, and multiply by `x`.

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
        // handle edge case where n is negative
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
- Use the divide and conquer approach to calculate the power in logarithmic time complexity.
- Handle edge cases where `n` is negative by inverting `x` and making `n` positive.
- Use recursive function calls to calculate the power for even and odd cases.