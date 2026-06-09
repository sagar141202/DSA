# Sqrt(x)

## Problem Statement
Given a non-negative integer `x`, return the square root of `x` rounded down to the nearest integer. The square root of `x` is a number `y` such that `y * y <= x` and `(y + 1) * (y + 1) > x`. The input `x` is guaranteed to be a non-negative integer, and the output should be an integer.

## Approach
We can use binary search to find the largest number `y` such that `y * y <= x`. This approach works by maintaining a search range `[left, right]` and iteratively narrowing it down until `left` and `right` converge. The final result will be the largest `y` such that `y * y <= x`.

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
        int left = 1, right = x / 2;

        // Perform binary search
        while (left <= right) {
            // Calculate mid value
            int mid = left + (right - left) / 2;

            // Calculate mid squared
            long midSquared = (long) mid * mid;

            // Update search range
            if (midSquared == x) return mid;
            else if (midSquared < x) left = mid + 1;
            else right = mid - 1;
        }

        // Return the largest y such that y * y <= x
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
- Use binary search to efficiently find the square root of a number.
- Be careful with integer overflow when calculating the square of a number.
- The search range can be narrowed down by maintaining a `[left, right]` range and iteratively updating it based on the comparison of `midSquared` and `x`.