# Largest Rectangle in Histogram

## Problem Statement
Given an array of integers `heights` representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram. The histogram is drawn such that the x-axis is horizontal and the y-axis is vertical. The input array will have a length between 1 and 10000, and each element will be between 1 and 10000.

## Approach
The algorithm uses a stack to keep track of the indices of the histogram bars. It iterates over the histogram, pushing the indices of the bars onto the stack if the current bar is higher than the bar at the top of the stack, and calculating the area of the rectangle with the bar at the top of the stack as the smallest bar when the current bar is lower.

## Complexity
- Time: O(n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

int largestRectangleArea(vector<int>& heights) {
    // Initialize the stack and the maximum area
    stack<int> s;
    int maxArea = 0;
    
    // Iterate over the histogram
    for (int i = 0; i <= heights.size(); i++) {
        // If the stack is empty or the current bar is higher than the bar at the top of the stack, push the index onto the stack
        if (s.empty() || (i < heights.size() && heights[i] >= heights[s.top()])) {
            s.push(i);
        } else {
            // Calculate the area of the rectangle with the bar at the top of the stack as the smallest bar
            while (!s.empty() && (i == heights.size() || heights[i] < heights[s.top()])) {
                int top = s.top();
                s.pop();
                int width = s.empty() ? i : i - s.top() - 1;
                maxArea = max(maxArea, heights[top] * width);
            }
            // Push the index onto the stack
            s.push(i);
        }
    }
    
    return maxArea;
}
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
- Calculate the area of the rectangle with the bar at the top of the stack as the smallest bar when the current bar is lower.
- The time complexity is O(n) and the space complexity is O(n), where n is the number of bars in the histogram.