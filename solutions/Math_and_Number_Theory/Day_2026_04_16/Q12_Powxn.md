# Pow(x,n)

## Problem Statement
Implement the `pow(x, n)` function, which calculates the value of `x` raised to the power of `n` (i.e., `x^n`). The function should handle both positive and negative values of `x` and `n`. The input `x` is a double, and `n` is a 32-bit integer. The function should return a double as the result.

## Approach
We use the divide-and-conquer approach to solve this problem by dividing `n` into two smaller sub-problems of size `n/2`. This approach allows us to calculate `x^n` in logarithmic time. We also handle the special cases when `n` is 0 or negative.

## Complexity
- Time: O(log n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    double myPow(double x, int n) {
        // Handle the special case when n is 0
        if (n == 0) return 1;
        
        // Handle the case when n is negative
        if (n < 0) {
            x = 1 / x;
            n = -n;
        }
        
        // Use the divide-and-conquer approach to calculate x^n
        return n % 2 == 0 ? myPow(x * x, n / 2) : x * myPow(x * x, n / 2);
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
- Use the divide-and-conquer approach to calculate `x^n` in logarithmic time.
- Handle the special cases when `n` is 0 or negative.
- Use recursion to solve the problem, but be aware of potential stack overflow issues for large inputs.