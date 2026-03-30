# Sqrt(x)

## Problem Statement
Given a non-negative integer `x`, return the square root of `x` rounded down to the nearest integer. The input `x` is guaranteed to be a non-negative integer. The square root of `x` is an integer `y` such that `y * y` is less than or equal to `x` and `(y + 1) * (y + 1)` is greater than `x`. For example, the square root of `4` is `2` because `2 * 2 = 4`, and the square root of `8` is `2` because `2 * 2 = 4` which is less than `8` and `3 * 3 = 9` which is greater than `8`.

## Approach
The approach is to use binary search to find the largest integer whose square is less than or equal to `x`. This is done by maintaining a search range `[low, high]` and iteratively narrowing it down until `low` and `high` converge. The final result is the value of `low` when the search range converges.

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
        
        // initialize search range
        int low = 1, high = x / 2;
        
        // perform binary search
        while (low <= high) {
            // calculate mid value
            long long mid = low + (high - low) / 2;
            
            // calculate square of mid
            long long square = mid * mid;
            
            // update search range
            if (square == x) return mid;
            else if (square < x) low = mid + 1;
            else high = mid - 1;
        }
        
        // return result
        return low - 1;
    }
};
```

## Test Cases
```
Input: x = 4
Output: 2
Input: x = 8
Output: 2
Input: x = 9
Output: 3
```

## Key Takeaways
- The binary search approach is efficient for finding the square root of a number.
- The search range is initialized to `[1, x / 2]` to avoid unnecessary searches.
- The final result is the value of `low - 1` when the search range converges.