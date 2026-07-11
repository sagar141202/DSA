# Largest Rectangle in Histogram

## Problem Statement
Given an array of integers `heights` representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram. The histogram is formed by stacking the bars on top of each other, and the area of the rectangle is calculated as the product of its width and height. For example, given `heights = [2,1,5,6,2,3]`, the output should be `10` because the largest rectangle has a width of 2 and a height of 5, and `2 * 5 = 10`. The constraints are `1 <= heights.length <= 1000` and `0 <= heights[i] <= 10^4`.

## Approach
The approach is to use a stack to keep track of the indices of the bars. We iterate over the heights array and push the index to the stack if the current bar is higher than the bar at the top of the stack. If the current bar is lower, we calculate the area of the rectangle with the bar at the top of the stack as the smallest bar.

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
        
        // Find the index of the first bar to the left that is lower than the current bar
        stack<int> s;
        for (int i = 0; i < n; i++) {
            while (!s.empty() && heights[s.top()] >= heights[i]) {
                s.pop();
            }
            left[i] = s.empty() ? 0 : s.top() + 1;
            s.push(i);
        }
        
        // Clear the stack for the next iteration
        while (!s.empty()) {
            s.pop();
        }
        
        // Find the index of the first bar to the right that is lower than the current bar
        for (int i = n - 1; i >= 0; i--) {
            while (!s.empty() && heights[s.top()] >= heights[i]) {
                s.pop();
            }
            right[i] = s.empty() ? n - 1 : s.top() - 1;
            s.push(i);
        }
        
        int maxArea = 0;
        for (int i = 0; i < n; i++) {
            // Calculate the area of the rectangle with the current bar as the smallest bar
            int area = heights[i] * (right[i] - left[i] + 1);
            maxArea = max(maxArea, area);
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
Output: 4
```

## Key Takeaways
- We use a stack to efficiently find the first bar to the left and right that is lower than the current bar.
- The area of the rectangle with the current bar as the smallest bar is calculated as the product of its width and height.
- We keep track of the maximum area found so far to return the largest rectangle area.