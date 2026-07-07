# Largest Rectangle in Histogram

## Problem Statement
Given an array of integers representing the heights of bars in a histogram, find the area of the largest rectangle that can be formed using these bars. The histogram is represented as an array of integers, where each integer corresponds to the height of a bar. The width of each bar is 1 unit. The task is to find the maximum area of a rectangle that can be formed using these bars, where the height of the rectangle is determined by the minimum height of the bars included, and the width is determined by the number of bars included. For example, given the array [2, 1, 5, 6, 2, 3], the largest rectangle that can be formed has an area of 10 units.

## Approach
The approach to solve this problem is to use a stack-based solution, where we maintain a stack of indices of the bars. We iterate through the array, and for each bar, we keep popping the stack until we find a bar that is smaller than the current bar or the stack is empty. The area of the rectangle that can be formed using the popped bar as the smallest bar is calculated and updated as the maximum area if necessary.

## Complexity
- Time: O(n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

int largestRectangleArea(vector<int>& heights) {
    int n = heights.size();
    stack<int> s;
    int maxArea = 0;
    for (int i = 0; i <= n; i++) {
        // If the stack is empty or the current bar is higher than the bar at the top of the stack, push the current index to the stack
        if (s.empty() || (i < n && heights[i] >= heights[s.top()])) {
            s.push(i);
        } else {
            // If the current bar is smaller than the bar at the top of the stack, pop the stack and calculate the area
            while (!s.empty() && (i == n || heights[i] < heights[s.top()])) {
                int top = s.top();
                s.pop();
                int width = s.empty() ? i : i - s.top() - 1;
                int area = heights[top] * width;
                maxArea = max(maxArea, area);
            }
            s.push(i);
        }
    }
    return maxArea;
}
```

## Test Cases
```
Input: [2, 1, 5, 6, 2, 3]
Output: 10
Input: [2, 4]
Output: 2
```

## Key Takeaways
- Use a stack to keep track of the indices of the bars in the histogram.
- Iterate through the array, and for each bar, pop the stack until we find a bar that is smaller than the current bar or the stack is empty.
- Calculate the area of the rectangle that can be formed using the popped bar as the smallest bar and update the maximum area if necessary.