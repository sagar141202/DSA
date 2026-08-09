# Pow(x,n)

## Problem Statement
Implement a function `myPow(x, n)` that calculates the value of `x` raised to the power of `n`, where `x` is a floating-point number and `n` is an integer. The function should handle cases where `n` is negative and where `x` is 0. The input range is `-100.0 < x < 100.0` and `-2^31 <= n <= 2^31-1`. The output should be a double precision floating point number. For example, `myPow(2.0, 3)` should return `8.0`, and `myPow(2.1, -3)` should return approximately `0.084`.

## Approach
The algorithm uses the concept of exponentiation by squaring to reduce the power by half in each recursive step. This is done by checking if the power is even or odd and using the properties of exponentiation to simplify the calculation. The base case is when the power is 0, at which point the function returns 1.

## Complexity
- Time: O(log(n))
- Space: O(log(n))

## C++ Solution
```cpp
#include <iostream>
using namespace std;

class Solution {
public:
    double myPow(double x, int n) {
        // Handle edge case where n is 0
        if (n == 0) return 1;
        
        // Handle negative n by converting to positive and taking reciprocal at the end
        if (n < 0) {
            x = 1 / x;
            n = -n;
        }
        
        // Recursive function to calculate x^n
        return helper(x, n);
    }
    
    double helper(double x, int n) {
        // Base case: anything to the power of 0 is 1
        if (n == 0) return 1;
        
        // If n is even, calculate x^(n/2) and square it
        if (n % 2 == 0) {
            double halfPow = helper(x, n / 2);
            return halfPow * halfPow;
        }
        
        // If n is odd, calculate x^((n-1)/2), square it, and multiply by x
        double halfPow = helper(x, (n - 1) / 2);
        return x * halfPow * halfPow;
    }
};

int main() {
    Solution solution;
    cout << solution.myPow(2.0, 3) << endl;  // Output: 8
    cout << solution.myPow(2.1, -3) << endl;  // Output: approximately 0.084
    return 0;
}
```

## Test Cases
```
Input: x = 2.0, n = 3
Output: 8.0
Input: x = 2.1, n = -3
Output: approximately 0.084
Input: x = 0, n = 0
Output: 1.0
```

## Key Takeaways
- The use of exponentiation by squaring reduces the time complexity to O(log(n)).
- Handling negative `n` by converting to positive and taking the reciprocal at the end simplifies the calculation.
- Recursive functions can be used to implement the exponentiation by squaring approach.