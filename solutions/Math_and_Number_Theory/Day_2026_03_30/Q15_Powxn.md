# Pow(x,n)

## Problem Statement
Implement the `myPow` function, which calculates the value of `x` raised to the power of `n` (`x^n`). The function should handle both positive and negative values of `x` and `n`. The input is a double `x` and an integer `n`, and the output should be a double. The constraints are: `-100.0 < x < 100.0` and `-2^31 <= n <= 2^31 - 1`. For example, `myPow(2.0, 3)` should return `8.0`, and `myPow(2.1, 3)` should return `9.261`. 

## Approach
We can solve this problem using the concept of exponentiation by squaring, which reduces the number of multiplications required. This approach takes advantage of the fact that `x^n = (x^2)^(n/2)` when `n` is even, and `x^n = x * (x^2)^((n-1)/2)` when `n` is odd. 

## Complexity
- Time: O(log(n))
- Space: O(1)

## C++ Solution
```cpp
class Solution {
public:
    double myPow(double x, int n) {
        // Handle the case where n is negative
        if (n < 0) {
            x = 1 / x;
            n = -n;
        }
        
        // Initialize the result to 1
        double res = 1.0;
        
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
};
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
- The key to solving this problem efficiently is to use exponentiation by squaring, which reduces the time complexity to O(log(n)).
- We need to handle the case where `n` is negative by taking the reciprocal of `x` and changing the sign of `n`.
- The space complexity is O(1) because we only use a constant amount of space to store the result and the input values.