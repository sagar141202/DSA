# Largest Rectangle in Histogram

## Problem Statement
Given an array of integers `heights` representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram. The input array will contain at least one element and at most 10,000 elements, with each element being a non-negative integer not exceeding 10,000. For example, if `heights = [2,1,5,6,2,3]`, the output should be `10` because the largest rectangle has an area of `10` (formed by the bars of height `5` and `6` with a width of `2` and the bars of height `2` and `3` with a width of `1` and then extended to the left by `1` unit and to the right by `1` unit, but the maximum area that can be obtained is `10`).

## Approach
We can use a stack-based approach to solve this problem efficiently. The idea is to maintain a stack of indices of the histogram bars and calculate the area of the rectangle with the bar at the top of the stack as the smallest bar. We iterate through the histogram, pushing indices onto the stack when the current bar is higher than the bar at the top of the stack, and popping indices when the current bar is lower.

## Complexity
- Time: O(n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        int n = heights.size();
        vector<int> left(n), right(n);
        
        // Initialize stack for left and right boundary
        stack<int> s;
        
        // Calculate left boundary
        for (int i = 0; i < n; i++) {
            while (!s.empty() && heights[s.top()] >= heights[i]) {
                s.pop();
            }
            left[i] = s.empty() ? 0 : s.top() + 1;
            s.push(i);
        }
        
        // Clear stack for right boundary calculation
        while (!s.empty()) {
            s.pop();
        }
        
        // Calculate right boundary
        for (int i = n - 1; i >= 0; i--) {
            while (!s.empty() && heights[s.top()] >= heights[i]) {
                s.pop();
            }
            right[i] = s.empty() ? n - 1 : s.top() - 1;
            s.push(i);
        }
        
        // Calculate maximum area
        int maxArea = 0;
        for (int i = 0; i < n; i++) {
            maxArea = max(maxArea, (right[i] - left[i] + 1) * heights[i]);
        }
        
        return maxArea;
    }
};
```

## Test Cases
```
Input: heights = [2,1,5,6,2,3]
Output: 10
Input: heights = [2,4]
Output: 2
```

## Key Takeaways
- The stack-based approach allows us to efficiently calculate the left and right boundaries for each bar in the histogram.
- The time complexity of O(n) is achieved because each bar is pushed and popped from the stack exactly once.
- The space complexity of O(n) is due to the use of the stack and the left and right boundary arrays.