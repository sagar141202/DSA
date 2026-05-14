# Pow(x,n)

## Problem Statement
Implement a function `myPow(x, n)` that calculates the value of `x` raised to the power of `n`, where `x` is a floating-point number and `n` is an integer. The function should handle cases where `n` is negative, zero, or positive. The input range is $-2^{31} \leq n \leq 2^{31}-1$ and $-2^{31} \leq x \leq 2^{31}-1$. For example, `myPow(2.0, 3)` should return `8.0`, `myPow(2.1, 3)` should return `9.261`, and `myPow(2.0, -3)` should return `0.125`.

## Approach
The solution uses the concept of exponentiation by squaring, which reduces the number of multiplications required. The idea is to break down the power into smaller sub-problems and solve them recursively. If `n` is negative, the function calculates `1 / myPow(x, -n)`.

## Complexity
- Time: O(log n)
- Space: O(log n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

double myPow(double x, int n) {
    // Handle edge case where n is zero
    if (n == 0) return 1;
    
    // If n is negative, calculate 1 / myPow(x, -n)
    if (n < 0) {
        x = 1 / x;
        n = -n;
    }
    
    // Initialize result
    double res = 1;
    
    // Perform exponentiation by squaring
    while (n > 0) {
        // If n is odd, multiply result by x
        if (n % 2 == 1) res *= x;
        
        // Square x and divide n by 2
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
- Use a recursive approach or a loop to perform the exponentiation.