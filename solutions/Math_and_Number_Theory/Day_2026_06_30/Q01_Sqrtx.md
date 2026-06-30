# Sqrt(x)

## Problem Statement
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The square root of x is a number y such that y * y <= x and (y + 1) * (y + 1) > x. For example, the square root of 4 is 2 because 2 * 2 = 4, and the square root of 8 is 2 because 2 * 2 = 4 and 3 * 3 = 9, which is greater than 8.

## Approach
We can use a binary search approach to find the square root of x. We start with a range of possible values for the square root, and repeatedly divide the range in half until we find the largest number whose square is less than or equal to x.

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
        
        // Initialize the search range
        int left = 2;
        int right = x / 2;
        
        // Perform binary search
        while (left <= right) {
            // Calculate the midpoint of the range
            int mid = left + (right - left) / 2;
            
            // Calculate the square of the midpoint
            long long midSquared = (long long)mid * mid;
            
            // If the square of the midpoint is equal to x, return the midpoint
            if (midSquared == x) {
                return mid;
            }
            // If the square of the midpoint is greater than x, update the right boundary
            else if (midSquared > x) {
                right = mid - 1;
            }
            // If the square of the midpoint is less than x, update the left boundary
            else {
                left = mid + 1;
            }
        }
        
        // Return the largest number whose square is less than or equal to x
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
- Use binary search to efficiently find the square root of a number.
- Be careful when calculating the square of a number to avoid integer overflow.
- Handle edge cases where the input number is 0 or 1.