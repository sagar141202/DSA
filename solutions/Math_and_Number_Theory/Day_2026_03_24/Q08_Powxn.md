# Pow(x,n)

## Problem Statement
Implement the `pow(x, n)` function, which calculates the value of `x` raised to the power of `n` (`x` to the power `n`). The function should handle both positive and negative `n`, as well as `x` equal to 0. The constraints are: `-100.0 < x < 100.0` and `-2^31 <= n <= 2^31 - 1`. For example, `pow(2.0, 3)` should return `8.0`, and `pow(2.1, -3)` should return approximately `0.084`.

## Approach
The algorithm uses the concept of exponentiation by squaring, which reduces the number of multiplications required. This approach takes advantage of the fact that `x^n = (x^(n/2))^2` when `n` is even, and `x^n = x * (x^((n-1)/2))^2` when `n` is odd. This recursive approach allows for efficient calculation of `x` to the power of `n`.

## Complexity
- Time: O(log n)
- Space: O(log n)

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
Input: x = 2.1, n = -3
Output: 0.084
Input: x = 0, n = 0
Output: 1
```

## Key Takeaways
- Use exponentiation by squaring to reduce the number of multiplications.
- Handle negative `n` by taking the reciprocal of `x` and making `n` positive.
- Initialize the result to 1 and update it accordingly in the loop.