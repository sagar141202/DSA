# Sqrt(x)

## Problem Statement
Given a non-negative integer `x`, return the square root of `x` rounded down to the nearest integer. The square root of `x` is a number `y` such that `y * y <= x` and `(y + 1) * (y + 1) > x`. The input `x` is guaranteed to be a non-negative integer.

## Approach
We can use a binary search approach to find the square root of `x`. The idea is to find the largest number `y` such that `y * y <= x`. We can start with a range of `[0, x]` and repeatedly divide the range in half until we find the largest `y` that satisfies the condition.

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
        // handle edge case
        if (x < 2) return x;
        
        int left = 2, right = x / 2;
        while (left <= right) {
            // calculate mid
            int mid = left + (right - left) / 2;
            long long square = (long long)mid * mid;
            
            // if mid * mid is equal to x, return mid
            if (square == x) return mid;
            // if mid * mid is less than x, update left
            else if (square < x) left = mid + 1;
            // if mid * mid is greater than x, update right
            else right = mid - 1;
        }
        // after the loop, right is the largest number such that right * right <= x
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
- We use a binary search approach to find the square root of `x`.
- We handle the edge case where `x` is less than 2 separately.
- We use a `long long` to calculate the square of `mid` to avoid overflow.