# Pow(x,n)

## Problem Statement
Implement a function `myPow(x, n)` that calculates the value of `x` raised to the power of `n`. The function should take two parameters: `x` (a double precision floating point number) and `n` (an integer). The function should return the result of `x` raised to the power of `n`. If `n` is negative, the function should calculate the reciprocal of `x` raised to the power of the absolute value of `n`. The input range is `−2^31 <= n <= 2^31 − 1` and `−2^31 <= x <= 2^31 − 1`. For example, `myPow(2.0, 3)` should return `8.0` and `myPow(2.1, -3)` should return approximately `0.084027`.

## Approach
The algorithm uses the concept of exponentiation by squaring to reduce the number of multiplications required. This approach involves recursively squaring `x` and reducing `n` by a factor of 2 until `n` becomes 0. If `n` is negative, the function calculates the reciprocal of `x` raised to the power of the absolute value of `n`.

## Complexity
- Time: O(log n)
- Space: O(log n)

## C++ Solution
```cpp
class Solution {
public:
    double myPow(double x, int n) {
        // handle negative exponent
        if (n < 0) {
            x = 1 / x;
            n = -n;
        }
        // initialize result
        double res = 1;
        // exponentiation by squaring
        while (n > 0) {
            // if n is odd, multiply result by x
            if (n % 2 == 1) {
                res *= x;
            }
            // square x and divide n by 2
            x *= x;
            n /= 2;
        }
        return res;
    }
};
```

## Test Cases
```
Input: x = 2.0, n = 3
Output: 8.0
Input: x = 2.1, n = -3
Output: approximately 0.084027
Input: x = 2.0, n = 0
Output: 1.0
```

## Key Takeaways
- Use exponentiation by squaring to reduce the number of multiplications required.
- Handle negative exponents by calculating the reciprocal of `x` raised to the power of the absolute value of `n`.
- Use a recursive or iterative approach to calculate the result.