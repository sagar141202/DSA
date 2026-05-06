# Sqrt(x)

## Problem Statement
Given a non-negative integer `x`, return the square root of `x` rounded down to the nearest integer. The input `x` is guaranteed to be a non-negative integer. The square root of `x` should be returned as an integer, without decimal places. For example, if `x` is 4, the function should return 2 because 2^2 = 4. If `x` is 8, the function should return 2 because 2^2 = 4, which is less than 8, and 3^2 = 9, which is greater than 8.

## Approach
We can use a binary search approach to find the square root of `x`. The idea is to find the largest number `y` such that `y^2` is less than or equal to `x`. This can be achieved by maintaining a search range `[low, high]` and iteratively narrowing it down until `low` and `high` converge.

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
        
        // Initialize search range
        int low = 1;
        int high = x / 2;
        
        // Perform binary search
        while (low <= high) {
            // Calculate mid value
            int mid = low + (high - low) / 2;
            
            // Calculate square of mid
            long long midSquared = (long long) mid * mid;
            
            // If midSquared is equal to x, return mid
            if (midSquared == x) return mid;
            
            // If midSquared is less than x, update low
            else if (midSquared < x) low = mid + 1;
            
            // If midSquared is greater than x, update high
            else high = mid - 1;
        }
        
        // Return the largest number whose square is less than x
        return low - 1;
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
- Use binary search to efficiently find the square root of a number.
- Handle edge cases where `x` is less than 2.
- Use a `long long` data type to avoid overflow when calculating the square of `mid`.