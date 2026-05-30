# Sqrt(x)

## Problem Statement
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The square root of x is a number y such that y * y <= x and (y + 1) * (y + 1) > x. The input x is guaranteed to be a non-negative integer. For example, if x = 4, the output should be 2 because 2 * 2 = 4. If x = 8, the output should be 2 because 2 * 2 = 4 and 3 * 3 = 9, which is greater than 8.

## Approach
We can use binary search to find the square root of x. The idea is to find a number y such that y * y is closest to x. We can start with a range [0, x] and keep dividing the range in half until we find the correct value.

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
        
        // initialize the range for binary search
        int left = 1, right = x / 2;
        
        // perform binary search
        while (left <= right) {
            // calculate the mid value
            long long mid = left + (right - left) / 2;
            
            // calculate the square of mid
            long long square = mid * mid;
            
            // if the square is equal to x, return mid
            if (square == x) return mid;
            
            // if the square is less than x, update the left pointer
            if (square < x) left = mid + 1;
            
            // if the square is greater than x, update the right pointer
            else right = mid - 1;
        }
        
        // return the square root rounded down to the nearest integer
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
- Handle edge cases where x is less than 2.
- Use a long long data type to avoid overflow when calculating the square of mid.