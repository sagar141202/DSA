# Pow(x,n)

## Problem Statement
Implement a function `myPow(x, n)` that calculates the value of `x` raised to the power of `n`, where `x` is a floating-point number and `n` is an integer. The function should handle cases where `n` is negative and where `x` is zero. The input ranges are `-100.0 < x < 100.0` and `-2^31 <= n <= 2^31 - 1`. For example, `myPow(2.0, 3)` returns `8.0`, and `myPow(2.1, -4)` returns `0.002617` (rounded to six decimal places).

## Approach
The algorithm uses the concept of exponentiation by squaring to efficiently calculate the power. It handles negative exponents by taking the reciprocal of the base. The solution iteratively squares the base and reduces the exponent by half until the exponent becomes zero.

## Complexity
- Time: O(log n)
- Space: O(1)

## C++ Solution
```cpp
#include <iostream>

double myPow(double x, int n) {
    // Handle edge case where n is negative
    if (n < 0) {
        x = 1 / x;
        n = -n;
    }
    double result = 1.0;
    // Exponentiation by squaring
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

int main() {
    double x = 2.1;
    int n = -4;
    std::cout << "Result: " << myPow(x, n) << std::endl;
    return 0;
}
```

## Test Cases
```
Input: x = 2.0, n = 3
Output: 8.0
Input: x = 2.1, n = -4
Output: 0.002617 (rounded to six decimal places)
```

## Key Takeaways
- Exponentiation by squaring can efficiently calculate powers with a time complexity of O(log n).
- Handling negative exponents requires taking the reciprocal of the base and changing the sign of the exponent.
- Iterative solutions can be more efficient than recursive ones for large inputs.