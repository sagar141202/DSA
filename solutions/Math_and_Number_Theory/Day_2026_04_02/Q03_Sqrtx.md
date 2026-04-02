# Sqrt(x)

## Problem Statement
Given a non-negative integer `x`, return the square root of `x` rounded down to the nearest integer. The input `x` is guaranteed to be a non-negative integer, and the output should be an integer. For example, if `x` is 4, the output should be 2 because 2^2 = 4. If `x` is 8, the output should be 2 because 2^2 = 4 and 3^2 = 9, so the largest integer whose square is less than or equal to 8 is 2.

## Approach
We can use binary search to find the square root of `x`. The idea is to find the largest integer `y` such that `y^2` is less than or equal to `x`. We can start with a range of possible values for `y` and repeatedly divide the range in half until we find the correct value.

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

        // Initialize the search range
        int left = 1, right = x / 2;

        // Perform binary search
        while (left <= right) {
            // Calculate the mid value
            int mid = left + (right - left) / 2;

            // Calculate the square of mid
            long long square = (long long)mid * mid;

            // If the square is equal to x, return mid
            if (square == x) return mid;

            // If the square is less than x, update the left boundary
            if (square < x) left = mid + 1;

            // If the square is greater than x, update the right boundary
            else right = mid - 1;
        }

        // Return the largest integer whose square is less than x
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
- Use binary search to find the square root of a number efficiently.
- Be careful with integer overflow when calculating the square of a number.
- The time complexity of the solution is O(log n), where n is the input number.