# Sqrt(x)

## Problem Statement
Given a non-negative integer `x`, return the square root of `x` rounded down to the nearest integer. The square root of `x` is a number `y` such that `y * y <= x` and `(y + 1) * (y + 1) > x`. The input `x` is guaranteed to be a non-negative integer.

## Approach
We will use a binary search approach to find the square root of `x`. The idea is to find a number `y` such that `y * y` is closest to `x` but not greater than `x`. We will maintain a search range `[low, high]` and iteratively narrow it down until we find the desired `y`.

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
        // handle edge cases
        if (x < 2) return x;
        
        // initialize search range
        int low = 2, high = x / 2;
        
        // binary search
        while (low <= high) {
            // calculate mid
            long long mid = low + (high - low) / 2;
            
            // calculate mid * mid
            long long square = mid * mid;
            
            // if mid * mid is equal to x, return mid
            if (square == x) return mid;
            
            // if mid * mid is less than x, update low
            else if (square < x) low = mid + 1;
            
            // if mid * mid is greater than x, update high
            else high = mid - 1;
        }
        
        // return the largest number whose square is less than or equal to x
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
- The search range can be narrowed down by checking if the square of the mid is less than or equal to the target number.