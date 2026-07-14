# Sqrt(x)

## Problem Statement
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The square root of x is a number y such that y*y <= x and (y+1)*(y+1) > x. For example, the square root of 4 is 2 because 2*2 = 4, and the square root of 8 is 2 because 2*2 = 4 and 3*3 = 9.

## Approach
The algorithm uses binary search to find the largest number whose square is less than or equal to x. This is because the square root function is monotonically increasing, so we can use binary search to find the correct value. We initialize two pointers, low and high, to 0 and x, and then repeatedly calculate the midpoint and check if its square is less than or equal to x.

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
        
        // initialize low and high pointers
        int low = 2;
        int high = x / 2;
        
        // perform binary search
        while (low <= high) {
            // calculate midpoint
            long long mid = low + (high - low) / 2;
            
            // calculate square of midpoint
            long long square = mid * mid;
            
            // if square is equal to x, return midpoint
            if (square == x) return mid;
            
            // if square is less than x, update low pointer
            else if (square < x) low = mid + 1;
            
            // if square is greater than x, update high pointer
            else high = mid - 1;
        }
        
        // return low - 1 because we want the largest number whose square is less than or equal to x
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
- Use binary search to find the square root of a number.
- Be careful with integer overflow when calculating the square of a number.
- The time complexity of this solution is O(log n), where n is the input number.