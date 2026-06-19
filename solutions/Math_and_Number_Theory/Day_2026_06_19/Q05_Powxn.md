# Pow(x,n)

## Problem Statement
Implement the `pow(x, n)` function, which calculates the value of `x` raised to the power of `n` (i.e., `x^n`). The function should be able to handle large inputs and should return the result as a double. The input `x` is a double, and `n` is a 32-bit integer. The function should handle cases where `n` is negative, zero, or positive. For example, `pow(2.0, 3)` should return `8.0`, and `pow(2.1, -3)` should return approximately `0.084`.

## Approach
The algorithm used to solve this problem is based on the concept of exponentiation by squaring, which reduces the number of multiplications required to calculate the power. The base case is when `n` is zero, in which case the result is `1`. For negative `n`, the result is the reciprocal of `x` raised to the power of the absolute value of `n`.

## Complexity
- Time: O(log(n))
- Space: O(1)

## C++ Solution
```cpp
#include <iostream>
using namespace std;

double myPow(double x, int n) {
    // handle edge case where n is zero
    if (n == 0) return 1;
    
    // handle negative n
    if (n < 0) {
        x = 1 / x;
        n = -n;
    }
    
    double result = 1;
    while (n > 0) {
        // if n is odd, multiply result by x
        if (n % 2 == 1) result *= x;
        
        // square x and divide n by 2
        x *= x;
        n /= 2;
    }
    
    return result;
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
Input: x = 2.1, n = -3
Output: 0.084
Input: x = 2.0, n = 0
Output: 1.0
```

## Key Takeaways
- The `pow(x, n)` function can be implemented using exponentiation by squaring to reduce the number of multiplications required.
- The function should handle cases where `n` is negative, zero, or positive.
- The time complexity of the solution is O(log(n)), and the space complexity is O(1).