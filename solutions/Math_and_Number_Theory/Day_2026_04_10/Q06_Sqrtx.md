# Sqrt(x)

## Problem Statement
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The square root of x is a number y such that y * y <= x and (y + 1) * (y + 1) > x. For example, the square root of 4 is 2 because 2 * 2 = 4, and the square root of 8 is 2 because 2 * 2 = 4 < 8 < 9 = 3 * 3.

## Approach
We can use binary search to find the square root of x. The idea is to find the largest number y such that y * y is less than or equal to x. We start by initializing two pointers, low and high, to 0 and x, respectively. Then, we repeatedly calculate the mid value and check if mid * mid is less than or equal to x.

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

        int left = 2, right = x / 2;
        while (left <= right) {
            // Calculate mid
            int mid = left + (right - left) / 2;
            long long square = (long long)mid * mid;

            // Check if mid is the square root
            if (square == x) return mid;
            // If mid is too small, try larger numbers
            else if (square < x) left = mid + 1;
            // If mid is too large, try smaller numbers
            else right = mid - 1;
        }
        // Return the largest number whose square is less than or equal to x
        return right;
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
- Be careful with integer overflow when calculating the square of a number.
- The square root of a number can be rounded down to the nearest integer using this approach.