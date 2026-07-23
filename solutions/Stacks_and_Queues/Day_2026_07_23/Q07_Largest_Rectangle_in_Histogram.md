# Largest Rectangle in Histogram

## Problem Statement
Given an array of integers `heights` representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram. The histogram is drawn such that the x-axis is horizontal and the y-axis is vertical. The area of a rectangle is calculated as its width multiplied by its height. The constraints are: `1 <= heights.length <= 100000` and `0 <= heights[i] <= 10^5`.

## Approach
We use a stack-based approach to solve this problem. The idea is to maintain a stack of indices of the histogram bars. For each bar, we calculate the area of the rectangle with the bar as the smallest bar.

## Complexity
- Time: O(n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

int largestRectangleArea(vector<int>& heights) {
    // Initialize the stack with -1 as the first element
    stack<int> st;
    st.push(-1);
    int maxArea = 0;
    
    // Iterate over the heights array
    for (int i = 0; i < heights.size(); i++) {
        // If the stack is not empty and the current height is less than the height at the top of the stack
        while (st.size() > 1 && heights[st.top()] > heights[i]) {
            // Calculate the area of the rectangle with the height at the top of the stack as the smallest bar
            int height = heights[st.top()];
            st.pop();
            int width = i - st.top() - 1;
            maxArea = max(maxArea, height * width);
        }
        // Push the current index to the stack
        st.push(i);
    }
    
    // Calculate the area of the rectangles with the remaining heights in the stack
    while (st.size() > 1) {
        int height = heights[st.top()];
        st.pop();
        int width = heights.size() - st.top() - 1;
        maxArea = max(maxArea, height * width);
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
- The stack is used to store the indices of the histogram bars.
- The area of the rectangle with the bar as the smallest bar is calculated using the width and height of the rectangle.
- The time complexity is O(n) because we iterate over the heights array once.