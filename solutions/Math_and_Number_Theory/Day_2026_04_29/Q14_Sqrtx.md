# Sqrt(x)

## Problem Statement
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The square root of x is a number y such that y * y <= x and (y + 1) * (y + 1) > x. The input is guaranteed to be a non-negative integer.

## Approach
The approach is to use binary search to find the largest number whose square is less than or equal to x. This is because the square root function is monotonically increasing, allowing us to apply binary search. We start with a range of possible values and repeatedly narrow it down until we find the correct answer.

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
        
        int left = 1, right = x / 2;
        while (left <= right) {
            // Calculate the middle value
            long long mid = left + (right - left) / 2;
            
            // Check if mid is the square root
            if (mid * mid <= x && (mid + 1) * (mid + 1) > x) {
                return mid;
            } 
            // If mid is too small, move to the right half
            else if (mid * mid < x) {
                left = mid + 1;
            } 
            // If mid is too large, move to the left half
            else {
                right = mid - 1;
            }
        }
        return -1; // Should not reach here
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
- Use binary search to efficiently find the square root.
- Be careful with integer overflow when calculating the square of a number.
- The time complexity of this solution is O(log n) due to the binary search.