# Largest Rectangle in Histogram

## Problem Statement
Given an array of integers `heights` representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram. The histogram is drawn such that the x-axis is horizontal and the y-axis is vertical. The area of a rectangle is calculated as the product of its width and height. The input array `heights` will contain at least one element and a maximum of 10^4 elements, with each element being between 0 and 10^4.

## Approach
The algorithm uses a stack to keep track of the indices of the histogram bars. It iterates over the histogram, pushing the indices of the bars onto the stack if the current bar is higher than the bar at the top of the stack, and calculating the area of the rectangle that can be formed with the bar at the top of the stack as the smallest bar if the current bar is lower. The maximum area found during this process is the area of the largest rectangle in the histogram.

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
    int n = heights.size();
    
    // Iterate over the histogram
    for (int i = 0; i <= n; i++) {
        // If the stack is empty or the current bar is higher than the bar at the top of the stack, push the current index onto the stack
        while (!s.empty() && (i == n || heights[s.top()] >= heights[i])) {
            // Calculate the width of the rectangle that can be formed with the bar at the top of the stack as the smallest bar
            int width = s.empty() ? i : i - s.top() - 1;
            // Calculate the area of the rectangle
            int area = heights[s.top()] * width;
            // Update the maximum area
            maxArea = max(maxArea, area);
            // Pop the top of the stack
            s.pop();
        }
        // Push the current index onto the stack
        s.push(i);
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
- Calculate the area of the rectangle that can be formed with the bar at the top of the stack as the smallest bar when the current bar is lower.
- Update the maximum area during the iteration process.