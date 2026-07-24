# Sqrt(x)

## Problem Statement
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The square root of x is a number y such that y * y <= x and (y + 1) * (y + 1) > x. For example, the square root of 4 is 2 because 2 * 2 = 4, and the square root of 8 is 2 because 2 * 2 = 4 <= 8 and (2 + 1) * (2 + 1) = 9 > 8.

## Approach
We can use binary search to find the largest number y such that y * y <= x. This approach works because the square root function is monotonically increasing. We start with a range [0, x] and repeatedly divide it in half until we find the largest y such that y * y <= x.

## Complexity
- Time: O(log n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int mySqrt(int x) {
        // Handle edge case where x is 0 or 1
        if (x < 2) {
            return x;
        }
        
        // Initialize binary search range
        int left = 1;
        int right = x / 2;
        
        // Perform binary search
        while (left <= right) {
            // Calculate mid value
            int mid = left + (right - left) / 2;
            
            // Calculate square of mid value
            long long midSquared = (long long) mid * mid;
            
            // If midSquared is equal to x, return mid
            if (midSquared == x) {
                return mid;
            }
            // If midSquared is less than x, update left
            else if (midSquared < x) {
                left = mid + 1;
            }
            // If midSquared is greater than x, update right
            else {
                right = mid - 1;
            }
        }
        
        // Return the largest y such that y * y <= x
        return right;
    }
};
```

## Test Cases
```
Input: 4
Output: 2
Input: 8
Output: 2
Input: 9
Output: 3
```

## Key Takeaways
- Use binary search to find the largest number y such that y * y <= x.
- Be careful with integer overflow when calculating the square of a number.
- Handle edge cases where x is 0 or 1 separately.