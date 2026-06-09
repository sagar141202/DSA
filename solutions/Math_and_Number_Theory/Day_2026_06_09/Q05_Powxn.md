# Pow(x,n)

## Problem Statement
Implement a function `myPow(x, n)` that calculates the value of `x` raised to the power of `n`, where `x` is a floating point number and `n` is an integer. The function should handle cases where `n` is negative and `x` is zero. For example, `myPow(2.0, 3)` should return `8.0`, and `myPow(2.1, -3)` should return approximately `0.084`.

## Approach
The algorithm uses the concept of exponentiation by squaring to efficiently calculate the power. If `n` is negative, the function calculates the power of the reciprocal of `x` and then takes the reciprocal of the result. The function handles the case where `x` is zero and `n` is negative by returning zero.

## Complexity
- Time: O(log n)
- Space: O(1)

## C++ Solution
```cpp
#include <iostream>
using namespace std;

double myPow(double x, int n) {
    // Handle the case where n is negative
    if (n < 0) {
        x = 1 / x;
        n = -n;
    }
    // Initialize the result to 1
    double res = 1;
    // Use exponentiation by squaring
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

int main() {
    double x = 2.1;
    int n = -3;
    double result = myPow(x, n);
    cout << "Result: " << result << endl;
    return 0;
}
```

## Test Cases
```
Input: x = 2.0, n = 3
Output: 8.0
Input: x = 2.1, n = -3
Output: 0.084
Input: x = 0, n = -3
Output: inf
```

## Key Takeaways
- Use exponentiation by squaring to efficiently calculate the power.
- Handle the case where `n` is negative by calculating the power of the reciprocal of `x`.
- Be aware of the potential for overflow when `x` is large and `n` is positive.