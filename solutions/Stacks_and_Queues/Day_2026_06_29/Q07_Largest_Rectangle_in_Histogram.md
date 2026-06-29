# Largest Rectangle in Histogram

## Problem Statement
Given an array of integers `heights` representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram. The input array `heights` will contain at least one element and at most 10^5 elements, with each element being between 0 and 10^5. For example, given `heights = [2,1,5,6,2,3]`, the output should be `10` because the largest rectangle has an area of `10` (with a width of `5` and a height of `2`).

## Approach
We will use a stack-based approach to solve this problem, where we maintain a stack of indices of the histogram bars. We iterate through the histogram, popping bars from the stack when we encounter a bar that is shorter than the bar at the top of the stack, and calculating the area of the rectangle that can be formed with the popped bar as the smallest bar.

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
        
        // Initialize stack for left boundary
        stack<int> s;
        for (int i = 0; i < n; i++) {
            while (!s.empty() && heights[s.top()] >= heights[i]) {
                s.pop();
            }
            left[i] = s.empty() ? 0 : s.top() + 1;
            s.push(i);
        }
        
        // Clear stack for right boundary
        while (!s.empty()) {
            s.pop();
        }
        
        for (int i = n - 1; i >= 0; i--) {
            while (!s.empty() && heights[s.top()] >= heights[i]) {
                s.pop();
            }
            right[i] = s.empty() ? n - 1 : s.top() - 1;
            s.push(i);
        }
        
        int maxArea = 0;
        for (int i = 0; i < n; i++) {
            maxArea = max(maxArea, heights[i] * (right[i] - left[i] + 1));
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
- Use a stack to keep track of the indices of the histogram bars.
- Calculate the left and right boundaries for each bar by popping bars from the stack when a smaller bar is encountered.
- Calculate the area of the rectangle that can be formed with each bar as the smallest bar.