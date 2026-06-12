# Sqrt(x)

## Problem Statement
Given a non-negative integer `x`, return the integer part of the square root of `x`. The integer part is the largest integer whose square is less than or equal to `x`. For example, the integer part of the square root of 9 is 3, and the integer part of the square root of 10 is 3.

## Approach
We can use a binary search approach to find the integer part of the square root. The idea is to find the largest number whose square is less than or equal to `x`. We start with a range of 0 to `x` and repeatedly divide the range in half until we find the desired number.

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
        int left = 2;
        int right = x / 2;

        // Perform binary search
        while (left <= right) {
            int mid = left + (right - left) / 2;
            long long square = (long long)mid * mid;

            // Check if mid is the largest number whose square is less than or equal to x
            if (square == x) return mid;
            if (square < x) {
                // If mid's square is less than x, update the left boundary
                left = mid + 1;
            } else {
                // If mid's square is greater than x, update the right boundary
                right = mid - 1;
            }
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
- We use a binary search approach to find the integer part of the square root in O(log n) time complexity.
- We handle edge cases where `x` is less than 2 separately.
- We use a `long long` data type to avoid integer overflow when calculating the square of `mid`.