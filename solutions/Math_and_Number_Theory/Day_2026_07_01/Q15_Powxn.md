# Pow(x,n)

## Problem Statement
Implement a function `myPow(x, n)` that calculates the value of `x` raised to the power of `n`, where `x` is a floating-point number and `n` is an integer. The function should handle cases where `n` is negative and where `x` is zero. The constraints are: `-100.0 < x < 100.0`, `-2^31 <= n <= 2^31-1`, and `-10^4 <= x^n <= 10^4`. For example, `myPow(2.0, 3)` should return `8.0`, and `myPow(2.1, -3)` should return approximately `0.084`.

## Approach
The approach is to use the divide-and-conquer technique to efficiently calculate the power. If `n` is even, we can calculate `myPow(x, n/2)` and then square the result. If `n` is odd, we can calculate `myPow(x, (n-1)/2)`, square the result, and then multiply it by `x`. This way, we reduce the number of multiplications required.

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
        // Handle the case where n is negative
        if (n < 0) {
            x = 1 / x;
            n = -n;
        }
        
        // Initialize the result
        double res = 1;
        
        // Use the divide-and-conquer technique
        while (n > 0) {
            // If n is odd, multiply the result by x
            if (n % 2 == 1) {
                res *= x;
            }
            
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
Input: x = 2.1, n = -3
Output: 0.084
Input: x = 0, n = 0
Output: 1
```

## Key Takeaways
- Use the divide-and-conquer technique to efficiently calculate the power.
- Handle the case where `n` is negative by taking the reciprocal of `x` and changing the sign of `n`.
- Use a while loop to repeatedly square `x` and divide `n` by 2 until `n` becomes 0.