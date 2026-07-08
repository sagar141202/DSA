# Sqrt(x)

## Problem Statement
Given a non-negative integer `x`, return the square root of `x` rounded down to the nearest integer. The square root of `x` is a number `y` such that `y * y <= x` and `(y + 1) * (y + 1) > x`. For example, the square root of 4 is 2 because 2 * 2 = 4, and the square root of 8 is 2 because 2 * 2 = 4 and 3 * 3 = 9.

## Approach
We will use binary search to find the square root of `x`. The idea is to find a number `y` such that `y * y` is closest to `x` without exceeding it. We will start with a range of possible values for `y` and iteratively narrow down the range until we find the correct value.

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
        // Handle edge cases
        if (x < 2) return x;
        
        // Initialize the search range
        int left = 1, right = x / 2;
        
        // Perform binary search
        while (left <= right) {
            // Calculate the mid value
            int mid = left + (right - left) / 2;
            
            // Check if mid * mid is equal to x
            if (mid * mid == x) return mid;
            
            // If mid * mid is less than x, update the left boundary
            if (mid * mid < x) {
                left = mid + 1;
            } 
            // If mid * mid is greater than x, update the right boundary
            else {
                right = mid - 1;
            }
        }
        
        // Return the largest number whose square is less than or equal to x
        return right;
    }
};
```

## Test Cases
```
Input: x = 4
Output: 2
Input: x = 8
Output: 2
Input: x = 9
Output: 3
```

## Key Takeaways
- The binary search approach allows us to find the square root in logarithmic time.
- We need to handle edge cases where `x` is less than 2.
- The search range is initialized to `[1, x / 2]` because the square root of `x` cannot exceed `x / 2`.