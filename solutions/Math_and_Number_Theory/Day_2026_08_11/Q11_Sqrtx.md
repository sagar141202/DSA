# Sqrt(x)

## Problem Statement
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The square root of x is a number y such that y * y <= x and (y + 1) * (y + 1) > x. The input x is guaranteed to be a non-negative integer, and the output should be an integer. For example, if x = 4, the output should be 2 because 2 * 2 = 4. If x = 8, the output should be 2 because 2 * 2 = 4 < 8 and 3 * 3 = 9 > 8.

## Approach
The algorithm uses binary search to find the largest number y such that y * y <= x. This is because the square root function is monotonically increasing, so we can use binary search to find the largest number that satisfies the condition. We start with a range [0, x] and repeatedly divide the range in half until we find the largest number y that satisfies the condition.

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
        int left = 1;
        int right = x / 2;
        
        // Perform binary search
        while (left <= right) {
            // Calculate the mid value
            int mid = left + (right - left) / 2;
            
            // Calculate the square of mid
            long long square = (long long)mid * mid;
            
            // If the square is equal to x, return mid
            if (square == x) return mid;
            // If the square is less than x, update the left boundary
            else if (square < x) left = mid + 1;
            // If the square is greater than x, update the right boundary
            else right = mid - 1;
        }
        
        // The largest number y such that y * y <= x is the right boundary
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
- The square root function is monotonically increasing, so we can use binary search to find the largest number y such that y * y <= x.
- We need to handle edge cases where x is less than 2.
- We need to use a long long data type to calculate the square of mid to avoid overflow.