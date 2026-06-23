# Largest Rectangle in Histogram

## Problem Statement
Given an array of integers `heights` representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram. The histogram is drawn such that the x-axis is horizontal and the y-axis is vertical. The largest rectangle is the rectangle with the largest area.

## Approach
The approach is to use a stack to keep track of the indices of the bars. We start by pushing the index of the first bar onto the stack. Then, we iterate over the rest of the bars. If the current bar is higher than the bar at the top of the stack, we push its index onto the stack. If the current bar is lower, we keep popping bars from the stack and calculate the area of the rectangle with the popped bar as the smallest bar until we find a bar that is lower than the current bar or the stack is empty.

## Complexity
- Time: O(n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

int largestRectangleArea(vector<int>& heights) {
    int n = heights.size();
    stack<int> st;
    int maxArea = 0;
    
    for (int i = 0; i <= n; i++) {
        // if the stack is empty or the current bar is higher than the bar at the top of the stack, push its index onto the stack
        while (!st.empty() && (i == n || heights[st.top()] >= heights[i])) {
            int h = heights[st.top()];
            st.pop();
            int w = st.empty() ? i : i - st.top() - 1;
            maxArea = max(maxArea, h * w);
        }
        st.push(i);
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
- Use a stack to keep track of the indices of the bars in the histogram.
- Calculate the area of the rectangle with the popped bar as the smallest bar when a smaller bar is encountered.
- The time complexity is O(n) where n is the number of bars in the histogram.