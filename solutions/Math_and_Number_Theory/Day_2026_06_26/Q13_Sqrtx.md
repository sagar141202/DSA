# Sqrt(x)

## Problem Statement
Given a non-negative integer `x`, return the square root of `x` rounded down to the nearest integer. The square root of `x` is a number `y` such that `y * y <= x` and `(y + 1) * (y + 1) > x`. The input `x` is guaranteed to be a non-negative integer.

## Approach
We can use binary search to find the square root of `x`. Start with a range `[0, x]` and repeatedly divide the range in half until we find the largest number `y` such that `y * y <= x`. This approach takes advantage of the fact that the square root function is monotonically increasing.

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
        // Handle edge case where x is 0 or 1
        if (x < 2) {
            return x;
        }

        // Initialize binary search range
        int left = 1;
        int right = x / 2;

        // Perform binary search
        while (left <= right) {
            // Calculate mid value
            int mid = left + (right - left) / 2;

            // Calculate square of mid value
            long long square = (long long) mid * mid;

            // If square is equal to x, return mid
            if (square == x) {
                return mid;
            }
            // If square is less than x, update left boundary
            else if (square < x) {
                left = mid + 1;
            }
            // If square is greater than x, update right boundary
            else {
                right = mid - 1;
            }
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
- The binary search approach is efficient for finding the square root of a number.
- We need to handle edge cases where the input is 0 or 1.
- The use of `long long` is necessary to avoid overflow when calculating the square of the mid value.