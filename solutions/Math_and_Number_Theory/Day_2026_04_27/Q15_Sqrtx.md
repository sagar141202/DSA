# Sqrt(x)

## Problem Statement
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The input is guaranteed to be a non-negative integer. For example, if x = 4, the output should be 2 because 2^2 = 4. If x = 8, the output should be 2 because 2^2 = 4 and 3^2 = 9, so the largest perfect square less than or equal to 8 is 4.

## Approach
The approach to solve this problem is to use a binary search algorithm to find the largest perfect square less than or equal to x. We can start by initializing two pointers, low and high, to 0 and x respectively. Then, we calculate the mid value and check if mid^2 is less than or equal to x.

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
        // Initialize two pointers, low and high
        int low = 0;
        int high = x;
        
        // Continue the loop until low is less than or equal to high
        while (low <= high) {
            // Calculate the mid value
            int mid = low + (high - low) / 2;
            
            // Check if mid^2 is less than or equal to x
            if ((long long)mid * mid <= x) {
                // If mid^2 is less than or equal to x, update low to mid + 1
                low = mid + 1;
            } else {
                // If mid^2 is greater than x, update high to mid - 1
                high = mid - 1;
            }
        }
        
        // The largest perfect square less than or equal to x is low - 1
        return low - 1;
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
- We use binary search to find the largest perfect square less than or equal to x.
- We need to cast mid to long long to avoid overflow when calculating mid^2.
- The time complexity of the solution is O(log n) due to the binary search algorithm.