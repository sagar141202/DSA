# Sqrt(x)

## Problem Statement
Given a non-negative integer `x`, return the square root of `x` rounded down to the nearest integer. The function should take an integer `x` as input and return an integer as output. For example, if `x` is 4, the function should return 2 because 2^2 = 4. If `x` is 8, the function should return 2 because 2^2 = 4 < 8 < 3^2 = 9.

## Approach
We can use a binary search approach to find the square root of `x`. The idea is to find the largest number whose square is less than or equal to `x`. We can initialize two pointers, `low` and `high`, to 0 and `x` respectively, and then perform a binary search to find the square root.

## Complexity
- Time: O(log n)
- Space: O(1)

## C++ Solution
```cpp
#include <iostream>
using namespace std;

class Solution {
public:
    int mySqrt(int x) {
        // Handle edge case where x is 0 or 1
        if (x < 2) {
            return x;
        }
        
        // Initialize low and high pointers
        int low = 2;
        int high = x / 2;
        
        // Perform binary search
        while (low <= high) {
            // Calculate mid value
            int mid = low + (high - low) / 2;
            
            // Calculate square of mid
            long long square = (long long)mid * mid;
            
            // If square is equal to x, return mid
            if (square == x) {
                return mid;
            }
            // If square is less than x, update low pointer
            else if (square < x) {
                low = mid + 1;
            }
            // If square is greater than x, update high pointer
            else {
                high = mid - 1;
            }
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
- We use a binary search approach to find the square root of `x`.
- We handle edge cases where `x` is 0 or 1 separately.
- We use a `long long` data type to avoid overflow when calculating the square of `mid`.