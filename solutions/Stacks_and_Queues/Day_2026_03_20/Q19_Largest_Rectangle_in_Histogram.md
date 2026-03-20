# Largest Rectangle in Histogram

## Problem Statement
Given an array of integers representing the heights of bars in a histogram, find the area of the largest rectangle that can be formed using these bars. The width of each bar is 1 unit, and the height is given by the corresponding element in the array. The rectangle must have its base on the x-axis and its sides parallel to the y-axis. For example, given the array [2, 1, 5, 6, 2, 3], the largest rectangle that can be formed has an area of 10 units.

## Approach
The approach to solve this problem is to use a stack to keep track of the indices of the bars. We iterate through the array and push the indices of the bars onto the stack if the current bar is higher than or equal to the bar at the top of the stack. If the current bar is lower than the bar at the top of the stack, we calculate the area of the rectangle that can be formed using the bar at the top of the stack as the smallest bar.

## Complexity
- Time: O(n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

int largestRectangleArea(vector<int>& heights) {
    stack<int> s;
    int maxArea = 0;
    int n = heights.size();
    
    for (int i = 0; i <= n; i++) {
        // If the stack is empty or the current bar is higher than the bar at the top of the stack, push the index onto the stack
        if (s.empty() || (i < n && heights[i] >= heights[s.top()])) {
            s.push(i);
        } else {
            // If the current bar is lower than the bar at the top of the stack, calculate the area of the rectangle
            while (!s.empty() && (i == n || heights[i] < heights[s.top()])) {
                int top = s.top();
                s.pop();
                int width = s.empty() ? i : i - s.top() - 1;
                maxArea = max(maxArea, heights[top] * width);
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
- Calculate the area of the rectangle using the bar at the top of the stack as the smallest bar when the current bar is lower than the bar at the top of the stack.
- The time complexity of the solution is O(n), where n is the number of bars in the histogram.