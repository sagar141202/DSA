# Pow(x,n)
## Problem Statement
Implement the `pow(x, n)` function, which calculates the value of `x` raised to the power of `n` (i.e., `x^n`). The function should handle both positive and negative `n` values, and `x` can be any real number. For example, `pow(2.0, 3)` should return `8.0`, and `pow(2.1, 3)` should return `9.261`. The input `x` is a double, and `n` is an integer. If `n` is negative, the function should return the reciprocal of `x` raised to the power of the absolute value of `n`.

## Approach
We can use the property of exponents that states `x^n = (x^(n/2))^2` to reduce the number of multiplications required. This approach is known as exponentiation by squaring. We will also handle the case where `n` is negative by taking the reciprocal of `x` raised to the power of the absolute value of `n`.

## Complexity
- Time: O(log n)
- Space: O(1)

## C++ Solution
```cpp
#include <iostream>

double myPow(double x, int n) {
    // Handle negative n
    if (n < 0) {
        x = 1 / x;
        n = -n;
    }
    // Initialize result
    double res = 1;
    // Exponentiation by squaring
    while (n > 0) {
        // If n is odd, multiply result by x
        if (n % 2 == 1) {
            res *= x;
        }
        // Square x and divide n by 2
        x *= x;
        n /= 2;
    }
    return res;
}

int main() {
    double x = 2.0;
    int n = 3;
    std::cout << myPow(x, n) << std::endl;
    return 0;
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
- Exponentiation by squaring reduces the time complexity to O(log n).
- Handling negative `n` values requires taking the reciprocal of `x` raised to the power of the absolute value of `n`.
- This solution assumes that the input `x` is a double and `n` is an integer.