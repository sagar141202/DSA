# Largest Rectangle in Histogram

## Problem Statement
Given an array of integers `heights` representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram. The histogram is drawn such that the x-axis is horizontal and the y-axis is vertical. The problem constraints are: `1 <= heights.length <= 100000` and `0 <= heights[i] <= 10^5`.

## Approach
We use a stack-based approach to solve this problem, where we maintain a stack of indices of the histogram bars. We iterate through the histogram, pushing the index of each bar onto the stack if the stack is empty or the current bar is higher than the bar at the top of the stack. If the current bar is lower than the bar at the top of the stack, we calculate the area of the rectangle with the bar at the top of the stack as the smallest bar.

## Complexity
- Time: O(n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

int largestRectangleArea(vector<int>& heights) {
    // Initialize the stack and the maximum area
    stack<int> st;
    int maxArea = 0;
    int n = heights.size();
    
    // Iterate through the histogram
    for (int i = 0; i <= n; i++) {
        // If the stack is empty or the current bar is higher than the bar at the top of the stack, push the index onto the stack
        if (st.empty() || (i < n && heights[i] >= heights[st.top()])) {
            st.push(i);
        } else {
            // If the current bar is lower than the bar at the top of the stack, calculate the area of the rectangle
            while (!st.empty() && (i == n || heights[i] < heights[st.top()])) {
                int top = st.top();
                st.pop();
                int width = st.empty() ? i : i - st.top() - 1;
                maxArea = max(maxArea, heights[top] * width);
            }
            // Push the index onto the stack
            st.push(i);
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
- Use a stack to store the indices of the histogram bars.
- Calculate the area of the rectangle when a smaller bar is encountered.
- The maximum area is updated at each calculation.