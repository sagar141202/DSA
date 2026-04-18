# Sqrt(x)

## Problem Statement
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The square root of x is a number y such that y * y <= x and (y + 1) * (y + 1) > x. The input is guaranteed to be a non-negative integer.

## Approach
We use binary search to find the largest number whose square is less than or equal to x. This approach allows us to efficiently find the square root in logarithmic time. We initialize two pointers, low and high, to 0 and x respectively, and iteratively update them until we find the square root.

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
        // handle edge case where x is 0 or 1
        if (x < 2) return x;
        
        // initialize binary search pointers
        int low = 1, high = x / 2;
        
        // perform binary search
        while (low <= high) {
            // calculate mid
            long mid = low + (high - low) / 2;
            
            // calculate square of mid
            long square = mid * mid;
            
            // update pointers
            if (square == x) return mid;
            else if (square < x) low = mid + 1;
            else high = mid - 1;
        }
        
        // return the largest number whose square is less than x
        return low - 1;
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
- Use binary search to efficiently find the square root in logarithmic time.
- Handle edge cases where x is 0 or 1.
- Be careful with integer overflow when calculating the square of mid.