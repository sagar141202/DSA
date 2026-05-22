# Sqrt(x)

## Problem Statement
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The square root of x is a number y such that y * y <= x and (y + 1) * (y + 1) > x. The input x is guaranteed to be a non-negative integer, and the output should be an integer. For example, if x = 4, the output should be 2 because 2 * 2 = 4. If x = 8, the output should be 2 because 2 * 2 = 4 and 3 * 3 = 9, so the largest integer whose square is less than or equal to 8 is 2.

## Approach
We will use binary search to find the square root of x. The idea is to find the largest number y such that y * y is less than or equal to x. We will start with a range [0, x] and repeatedly divide the range in half until we find the correct value.

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
            // Calculate the middle value
            int mid = left + (right - left) / 2;
            
            // Calculate the square of the middle value
            long long square = (long long)mid * mid;
            
            // If the square is equal to x, return the middle value
            if (square == x) return mid;
            
            // If the square is less than x, update the left boundary
            if (square < x) {
                left = mid + 1;
            } 
            // If the square is greater than x, update the right boundary
            else {
                right = mid - 1;
            }
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
- The binary search approach is efficient for finding the square root of a number.
- We need to handle edge cases where x is less than 2.
- The time complexity of the solution is O(log n), where n is the input number x.