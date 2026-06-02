# Sqrt(x)

## Problem Statement
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The square root of x is a number y such that y * y <= x and (y + 1) * (y + 1) > x. For example, the square root of 4 is 2 because 2 * 2 = 4, and the square root of 8 is 2 because 2 * 2 = 4 and 3 * 3 = 9.

## Approach
We can use a binary search approach to find the square root of x. The idea is to search for a number y such that y * y is closest to x. We can start with a range [0, x] and repeatedly divide the range in half until we find the largest number y such that y * y <= x.

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
            
            // Calculate the square of mid
            long long square = (long long)mid * mid;
            
            // If the square is equal to x, return mid
            if (square == x) return mid;
            // If the square is less than x, update the left boundary
            else if (square < x) left = mid + 1;
            // If the square is greater than x, update the right boundary
            else right = mid - 1;
        }
        
        // Return the largest number y such that y * y <= x
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
- Use binary search to find the square root of a number.
- Be careful with integer overflow when calculating the square of a number.
- The time complexity of the solution is O(log n) due to the binary search approach.