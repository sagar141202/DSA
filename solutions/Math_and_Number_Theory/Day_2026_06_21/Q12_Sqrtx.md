# Sqrt(x)

## Problem Statement
Given a non-negative integer `x`, return the square root of `x` rounded down to the nearest integer. The square root of `x` is a number `y` such that `y * y <= x` and `(y + 1) * (y + 1) > x`. For example, the square root of 4 is 2 because 2 * 2 = 4, and the square root of 8 is 2 because 2 * 2 = 4 and 3 * 3 = 9.

## Approach
We can use binary search to find the square root of `x`. The idea is to find the largest number `y` such that `y * y <= x`. We can start with a range of 0 to `x` and repeatedly divide the range in half until we find the largest `y` that satisfies the condition.

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
        if (x < 2) return x;
        int left = 1, right = x / 2;
        while (left <= right) {
            long long mid = left + (right - left) / 2;
            long long square = mid * mid;
            if (square == x) return mid;
            if (square < x) left = mid + 1;
            else right = mid - 1;
        }
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
- We use binary search to find the square root of `x` in O(log n) time complexity.
- We need to handle the case where `x` is less than 2 separately.
- We use `long long` to avoid integer overflow when calculating the square of `mid`.