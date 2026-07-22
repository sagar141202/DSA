# Pow(x,n)

## Problem Statement
Implement a function `myPow(x, n)` that calculates the value of `x` raised to the power of `n`, where `x` is a floating-point number and `n` is an integer. The function should handle cases where `n` is negative and where `x` is zero. For example, `myPow(2.0, 3)` should return `8.0`, and `myPow(2.1, -3)` should return approximately `0.084`.

## Approach
We use the concept of exponentiation by squaring to efficiently calculate the power. The idea is to divide the problem into smaller sub-problems and solve them recursively. If `n` is negative, we calculate the reciprocal of `x` raised to the power of the absolute value of `n`.

## Complexity
- Time: O(log(n))
- Space: O(log(n))

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

double myPow(double x, int n) {
    // handle edge case where n is 0
    if (n == 0) return 1;
    
    // handle negative n
    if (n < 0) {
        x = 1 / x;
        n = -n;
    }
    
    // recursive case
    if (n % 2 == 0) {
        double temp = myPow(x, n / 2);
        return temp * temp;
    } else {
        double temp = myPow(x, n / 2);
        return x * temp * temp;
    }
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
- Use exponentiation by squaring to reduce the time complexity to O(log(n)).
- Handle edge cases where `n` is 0 or negative.
- Use recursion to divide the problem into smaller sub-problems.