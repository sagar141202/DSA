# Pow(x,n)

## Problem Statement
Implement a function `myPow(x, n)` that calculates the value of `x` raised to the power of `n`. The function should handle both positive and negative values of `n`. The input `x` is a floating point number and `n` is an integer. For example, `myPow(2.0, 3)` should return `8.0` and `myPow(2.1, -3)` should return approximately `0.084`.

## Approach
The problem can be solved using the concept of exponentiation by squaring, which reduces the number of multiplications required to calculate the power. We will handle the case where `n` is negative by taking the reciprocal of `x` and making `n` positive.

## Complexity
- Time: O(log n)
- Space: O(1)

## C++ Solution
```cpp
#include <iostream>
using namespace std;

double myPow(double x, int n) {
    // handle the case where n is negative
    if (n < 0) {
        x = 1 / x;
        n = -n;
    }
    double result = 1.0;
    // use exponentiation by squaring
    while (n > 0) {
        // if n is odd, multiply the result by x
        if (n % 2 == 1) {
            result *= x;
        }
        // square x and divide n by 2
        x *= x;
        n /= 2;
    }
    return result;
}
```

## Test Cases
```
Input: x = 2.0, n = 3
Output: 8.0
Input: x = 2.1, n = -3
Output: 0.084
Input: x = 2.0, n = 0
Output: 1.0
```

## Key Takeaways
- Exponentiation by squaring reduces the time complexity to O(log n)
- Handling negative `n` by taking the reciprocal of `x` and making `n` positive simplifies the problem
- The solution uses a simple while loop and basic arithmetic operations to calculate the power.