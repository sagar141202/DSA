# Sqrt(x)

## Problem Statement
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The square root of x is a number y such that y * y <= x and (y + 1) * (y + 1) > x. The input is guaranteed to be a non-negative integer, and the output will be in the range [0, 2^31 - 1]. For example, the input 4 will return 2 because 2 * 2 = 4, and the input 8 will return 2 because 2 * 2 = 4 and 3 * 3 = 9, which is greater than 8.

## Approach
We can use binary search to find the square root of x. The algorithm starts by initializing two pointers, low and high, to 0 and x respectively. Then, we calculate the mid value and check if mid * mid is less than or equal to x. If it is, we update low to mid + 1. Otherwise, we update high to mid. We repeat this process until low is greater than high.

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
- We use binary search to find the square root of x, which reduces the time complexity to O(log n).
- We use long long data type to handle the case where mid * mid is greater than INT_MAX.
- The algorithm is efficient and accurate, and it handles edge cases correctly.