# Sqrt(x)

## Problem Statement
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The square root of x is a number y such that y * y <= x and (y + 1) * (y + 1) > x. For example, the square root of 4 is 2 because 2 * 2 = 4, and the square root of 8 is 2 because 2 * 2 = 4 <= 8 and (2 + 1) * (2 + 1) = 9 > 8.

## Approach
The approach is to use binary search to find the largest number whose square is less than or equal to x. We start by initializing two pointers, low and high, to 0 and x respectively. Then we calculate the mid value and check if its square is less than or equal to x.

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
        int low = 1, high = x / 2;
        while (low <= high) {
            long long mid = low + (high - low) / 2;
            long long square = mid * mid;
            if (square == x) return mid;
            if (square < x) low = mid + 1;
            else high = mid - 1;
        }
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
- We use binary search to find the square root efficiently.
- We need to handle the case where x is less than 2 separately.
- We use long long to avoid integer overflow when calculating the square of mid.