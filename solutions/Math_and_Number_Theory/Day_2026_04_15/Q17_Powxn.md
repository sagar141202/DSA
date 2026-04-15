# Pow(x,n)

## Problem Statement
Implement a function `myPow(x, n)` that calculates the value of `x` raised to the power of `n`, where `x` is a floating-point number and `n` is an integer. The function should handle cases where `n` is negative, zero, or positive. The input range is `−2^31 <= n <= 2^31 − 1` and `−10^4 <= x <= 10^4`. The output should be accurate to within `10^-5` of the actual result.

## Approach
The algorithm uses the concept of exponentiation by squaring to reduce the number of multiplications required. This approach takes advantage of the property `x^(2n) = (x^n)^2` to calculate the power in logarithmic time complexity. The base case is when `n` is zero, at which point the function returns 1.

## Complexity
- Time: O(log|n|)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

double myPow(double x, int n) {
    // handle edge case where n is zero
    if (n == 0) return 1;
    
    // handle negative exponent by converting to positive and taking reciprocal
    if (n < 0) {
        x = 1 / x;
        n = -n;
    }
    
    // initialize result to 1
    double res = 1;
    
    // use exponentiation by squaring to calculate power
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
- Exponentiation by squaring reduces the time complexity to logarithmic.
- Handling negative exponents requires taking the reciprocal of the base and converting the exponent to positive.
- The algorithm uses a while loop to repeatedly square the base and divide the exponent by 2, making it efficient for large inputs.