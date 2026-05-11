# Sqrt(x)

## Problem Statement
Given a non-negative integer `x`, return the integer part of the square root of `x`. The integer part of the square root of `x` is the largest integer whose square is less than or equal to `x`. For example, the integer part of the square root of 8 is 2 because 2^2 = 4, which is less than 8, and 3^2 = 9, which is greater than 8. The function should take an integer `x` as input and return an integer as output.

## Approach
We will use binary search to find the integer part of the square root of `x`. The idea is to find the largest number whose square is less than or equal to `x`. We will start with a range of possible values and repeatedly divide the range in half until we find the correct value.

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
        int left = 1;
        int right = x / 2;

        // Perform binary search
        while (left <= right) {
            // Calculate the mid value
            int mid = left + (right - left) / 2;

            // Calculate the square of the mid value
            long long midSquared = (long long)mid * mid;

            // If the square of the mid value is equal to x, return mid
            if (midSquared == x) return mid;
            // If the square of the mid value is less than x, update the left pointer
            else if (midSquared < x) left = mid + 1;
            // If the square of the mid value is greater than x, update the right pointer
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
- The binary search approach is used to find the integer part of the square root of a given number.
- The time complexity of the solution is O(log n) due to the binary search.
- The space complexity of the solution is O(1) as it only uses a constant amount of space.