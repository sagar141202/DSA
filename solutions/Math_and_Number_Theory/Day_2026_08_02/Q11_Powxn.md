# Pow(x,n)

## Problem Statement
Implement a function `myPow(x, n)` that calculates the value of `x` raised to the power of `n`, where `x` is a floating-point number and `n` is an integer. The function should handle cases where `n` is negative, zero, or positive. The input range is `-100.0 < x < 100.0` and `−2^31 <= n <= 2^31 − 1`. The output should be a double-precision floating-point number.

## Approach
We can use a divide-and-conquer approach to solve this problem, utilizing the property of exponentiation that states `x^n = (x^(n/2))^2` when `n` is even, and `x^n = x * (x^((n-1)/2))^2` when `n` is odd. This approach reduces the number of multiplications required to calculate the power.

## Complexity
- Time: O(log n)
- Space: O(log n)

## C++ Solution
```cpp
#include <iostream>
using namespace std;

double myPow(double x, int n) {
    // Handle edge case where n is 0
    if (n == 0) return 1;
    
    // Handle negative n
    if (n < 0) {
        x = 1 / x;
        n = -n;
    }
    
    // Initialize result
    double res = 1;
    
    // Use divide-and-conquer approach
    while (n > 0) {
        // If n is odd, multiply result by x
        if (n % 2 == 1) res *= x;
        
        // Square x and divide n by 2
        x *= x;
        n /= 2;
    }
    
    return res;
}

int main() {
    double x = 2.0;
    int n = 3;
    cout << myPow(x, n) << endl;
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
- Use a divide-and-conquer approach to reduce the number of multiplications required.
- Handle edge cases where `n` is 0 or negative.
- Use bit manipulation to check if `n` is odd or even.