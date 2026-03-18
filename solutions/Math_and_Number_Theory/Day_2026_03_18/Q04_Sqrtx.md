# Sqrt(x)

## Problem Statement
Given a non-negative integer `x`, return the square root of `x` rounded down to the nearest integer. The square root of `x` is a number `y` such that `y * y <= x` and `(y + 1) * (y + 1) > x`. The input `x` is guaranteed to be a non-negative integer. Examples: `sqrt(4)` returns `2`, `sqrt(8)` returns `2`, `sqrt(9)` returns `3`.

## Approach
We can use binary search to find the square root of `x`. The idea is to maintain a search range `[low, high]` and check if the square of the middle element is less than or equal to `x`. If it is, we update `low` to `mid + 1`. Otherwise, we update `high` to `mid`.

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
        
        // Initialize search range
        int low = 1;
        int high = x / 2;
        
        // Perform binary search
        while (low <= high) {
            // Calculate mid
            int mid = low + (high - low) / 2;
            
            // Check if mid * mid is less than or equal to x
            if (mid * mid <= x) {
                // If (mid + 1) * (mid + 1) is greater than x, return mid
                if ((mid + 1) * (mid + 1) > x) {
                    return mid;
                }
                // Otherwise, update low to mid + 1
                low = mid + 1;
            } else {
                // Update high to mid - 1
                high = mid - 1;
            }
        }
        
        // If no square root is found, return -1
        return -1;
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
- Binary search can be used to find the square root of a number efficiently.
- The search range can be initialized to `[1, x / 2]` to reduce the number of iterations.
- The square root of `x` is the largest number `y` such that `y * y <= x`.