# Sqrt(x)

## Problem Statement
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The square root of x is a number y such that y * y <= x and (y + 1) * (y + 1) > x. The input x is guaranteed to be a non-negative integer, and the output should be an integer.

## Approach
The approach is to use binary search to find the largest number whose square is less than or equal to x. We start by initializing two pointers, low and high, to 0 and x respectively. Then, we calculate the mid value and check if its square is less than or equal to x.

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
        // Handle edge case
        if (x < 2) return x;
        
        int low = 2;
        int high = x / 2;
        
        // Binary search
        while (low <= high) {
            long long mid = low + (high - low) / 2;
            long long square = mid * mid;
            
            // If mid * mid is equal to x, return mid
            if (square == x) return mid;
            // If mid * mid is greater than x, update high
            else if (square > x) high = mid - 1;
            // If mid * mid is less than x, update low
            else low = mid + 1;
        }
        
        // Return the largest number whose square is less than x
        return high;
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
- The time complexity of this solution is O(log n) due to the binary search.