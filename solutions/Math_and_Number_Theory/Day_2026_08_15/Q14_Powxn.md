# Pow(x,n)

## Problem Statement
Implement the pow(x, n) function, which calculates the value of x raised to the power of n (i.e., x^n). The function should be able to handle large values of n and negative values of x. The constraints are: -100.0 < x < 100.0 and -2^31 <= n <= 2^31 - 1. For example, pow(2.0, 3) = 8, pow(2.1, 3) = 9.261, and pow(2.0, -3) = 0.125.

## Approach
The algorithm uses the concept of exponentiation by squaring to reduce the time complexity. If n is even, x^n can be calculated as (x^(n/2))^2. If n is odd, x^n can be calculated as x * (x^((n-1)/2))^2. This approach allows us to calculate x^n in logarithmic time.

## Complexity
- Time: O(log(n))
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    double myPow(double x, int n) {
        // Handle negative n
        if (n < 0) {
            x = 1 / x;
            n = -n;
        }
        
        // Initialize result
        double res = 1.0;
        
        // Calculate x^n using exponentiation by squaring
        while (n > 0) {
            // If n is odd, multiply res by x
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
Input: x = 2.1, n = 3
Output: 9.261
Input: x = 2.0, n = -3
Output: 0.125
```

## Key Takeaways
- Exponentiation by squaring can be used to calculate x^n in logarithmic time.
- The algorithm should handle negative values of n by converting the problem to a positive n and inverting x.
- The algorithm should handle large values of n by using integer division and modulo operations to reduce the number of iterations.