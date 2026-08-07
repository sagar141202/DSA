# Sqrt(x)

## Problem Statement
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The square root of x is a number y such that y * y <= x and (y + 1) * (y + 1) > x. For example, the square root of 4 is 2 because 2 * 2 = 4, and the square root of 8 is 2 because 2 * 2 = 4 < 8 < 9 = 3 * 3.

## Approach
We can use binary search to find the square root of x. We start with a range [0, x] and repeatedly divide the range in half until we find the largest number y such that y * y <= x.

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
        if (x < 2) return x; // 0 and 1 are perfect squares
        int left = 2, right = x / 2;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            long long square = (long long)mid * mid; // use long long to avoid overflow
            if (square == x) return mid;
            if (square < x) left = mid + 1;
            else right = mid - 1;
        }
        return right; // return the largest number y such that y * y <= x
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
- Be careful with integer overflow when calculating the square of a number.
- The square root of a number x is the largest number y such that y * y <= x.