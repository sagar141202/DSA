# Sqrt(x)

## Problem Statement
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The square root of x is a number y such that y * y <= x and (y + 1) * (y + 1) > x. For example, the square root of 4 is 2 because 2 * 2 = 4, and the square root of 8 is 2 because 2 * 2 = 4 < 8 and 3 * 3 = 9 > 8.

## Approach
We will use binary search to find the square root of x. The idea is to find a number y such that y * y is closest to x. We will start with a range [0, x] and keep narrowing it down until we find the correct value of y.

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

        int left = 2;
        int right = x / 2;

        // perform binary search
        while (left <= right) {
            long long mid = left + (right - left) / 2;
            long long square = mid * mid;

            // if mid * mid is equal to x, return mid
            if (square == x) return mid;

            // if mid * mid is less than x, update left
            if (square < x) left = mid + 1;

            // if mid * mid is greater than x, update right
            else right = mid - 1;
        }

        // return the largest number whose square is less than or equal to x
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
- Be careful with integer overflow when calculating the square of a number.
- The time complexity of the binary search approach is O(log n), where n is the input number.