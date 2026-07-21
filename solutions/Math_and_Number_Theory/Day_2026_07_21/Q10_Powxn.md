# Pow(x,n)

## Problem Statement
Implement a function `myPow(x, n)` that calculates the value of `x` raised to the power of `n`, where `x` is a floating-point number and `n` is an integer. The function should handle cases where `n` is negative and `x` is zero. For example, `myPow(2.0, 3)` should return `8.0`, and `myPow(2.1, -4)` should return approximately `0.079056`.

## Approach
The algorithm uses a divide-and-conquer approach to calculate the power in logarithmic time complexity. It checks if `n` is negative and adjusts the calculation accordingly. The base case is when `n` is zero, at which point the function returns `1`. The recursive case divides `n` by `2` and squares the result of the recursive call.

## Complexity
- Time: O(log n)
- Space: O(log n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

double myPow(double x, int n) {
    // Handle the case where n is negative
    if (n < 0) {
        x = 1 / x;
        n = -n;
    }
    // Base case: anything to the power of 0 is 1
    if (n == 0) return 1;
    // Recursive case: divide n by 2 and square the result
    if (n % 2 == 0) {
        double halfPow = myPow(x, n / 2);
        return halfPow * halfPow;
    } else {
        double halfPow = myPow(x, n / 2);
        return x * halfPow * halfPow;
    }
}
```

## Test Cases
```
Input: x = 2.0, n = 3
Output: 8.0
Input: x = 2.1, n = -4
Output: approximately 0.079056
Input: x = 0.0, n = 0
Output: 1.0
```

## Key Takeaways
- The divide-and-conquer approach reduces the time complexity to logarithmic.
- Handling the case where `n` is negative is crucial for correct results.
- The recursive case must handle both even and odd values of `n` correctly.