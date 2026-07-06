# Pow(x,n)

## Problem Statement
Implement a function `myPow(x, n)` that calculates the value of `x` raised to the power of `n`, where `x` is a floating-point number and `n` is an integer. The function should handle cases where `n` is negative, zero, or positive. The input ranges are `-100.0 < x < 100.0` and `-2^31 <= n <= 2^31 - 1`. For example, `myPow(2.0, 3)` should return `8.0`, and `myPow(2.1, -3)` should return approximately `0.084` (which is `1 / (2.1 * 2.1 * 2.1)`).

## Approach
The algorithm uses the concept of exponentiation by squaring to efficiently calculate the power. This approach reduces the number of multiplications required by using the fact that `x^n = (x^2)^(n/2)` when `n` is even, and `x^n = x * (x^2)^((n-1)/2)` when `n` is odd.

## Complexity
- Time: O(log(n))
- Space: O(1)

## C++ Solution
```cpp
#include <iostream>
using namespace std;

double myPow(double x, int n) {
    // Handle edge case where n is zero
    if (n == 0) return 1;
    
    // If n is negative, calculate the reciprocal
    if (n < 0) {
        x = 1 / x;
        n = -n;
    }
    
    double result = 1;
    while (n > 0) {
        // If n is odd, multiply the result by x
        if (n % 2 == 1) result *= x;
        
        // Square x and divide n by 2
        x *= x;
        n /= 2;
    }
    
    return result;
}

int main() {
    cout << myPow(2.0, 3) << endl;  // Output: 8
    cout << myPow(2.1, -3) << endl; // Output: approximately 0.084
    return 0;
}
```

## Test Cases
```
Input: x = 2.0, n = 3
Output: 8.0
Input: x = 2.1, n = -3
Output: approximately 0.084
Input: x = 0.0, n = 0
Output: 1.0
```

## Key Takeaways
- Use exponentiation by squaring to reduce the number of multiplications.
- Handle negative `n` by calculating the reciprocal of `x` and changing `n` to positive.
- Initialize `result` to 1 and update it based on whether `n` is odd or even in each iteration.