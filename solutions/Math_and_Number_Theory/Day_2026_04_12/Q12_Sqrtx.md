# Sqrt(x)

## Problem Statement
Given a non-negative integer `x`, return the integer part of the square root of `x`. The integer part is the largest integer whose square is less than or equal to `x`. For example, the integer part of the square root of `9` is `3` and the integer part of the square root of `8` is `2`. The input `x` is guaranteed to be a non-negative integer, and the output should be an integer.

## Approach
We can use a binary search approach to find the integer part of the square root. The idea is to find the largest number whose square is less than or equal to `x`. We initialize two pointers, `low` and `high`, to `0` and `x`, respectively, and then perform a binary search.

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

        int low = 1, high = x / 2;
        while (low <= high) {
            // calculate mid
            long mid = low + (high - low) / 2;
            // calculate mid squared
            long midSquared = mid * mid;
            // if mid squared is equal to x, return mid
            if (midSquared == x) return mid;
            // if mid squared is less than x, update low
            else if (midSquared < x) low = mid + 1;
            // if mid squared is greater than x, update high
            else high = mid - 1;
        }
        // return the largest integer whose square is less than or equal to x
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
- The binary search approach is used to find the integer part of the square root.
- The time complexity is O(log n) because we divide the search space in half at each step.
- The space complexity is O(1) because we only use a constant amount of space to store the pointers and the mid value.