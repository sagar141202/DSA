# Sqrt(x)

## Problem Statement
Given a non-negative integer `x`, return the square root of `x` rounded down to the nearest integer. The square root of `x` is a number `y` such that `y * y` is less than or equal to `x` and `(y + 1) * (y + 1)` is greater than `x`. The input `x` is guaranteed to be a non-negative integer.

## Approach
The approach is to use binary search to find the largest number whose square is less than or equal to `x`. This is because the square root function is monotonically increasing, allowing us to use binary search. We start with a range of possible values and iteratively narrow it down until we find the correct square root.

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
            long long square = (long long)mid * mid;

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

        // Return the largest number whose square is less than x
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
- The problem can be solved using binary search, taking advantage of the monotonicity of the square root function.
- The time complexity is O(log n) due to the use of binary search.
- The space complexity is O(1) as we only use a constant amount of space to store the variables.