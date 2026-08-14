# Largest Rectangle in Histogram

## Problem Statement
Given an array of integers `heights` representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram. The histogram is drawn such that the x-axis is horizontal and the y-axis is vertical. The input array will have a length of at least 1 and a maximum length of 10^4. Each element in the array will be between 1 and 10^4. For example, given the array `[2,1,5,6,2,3]`, the output should be `10` because the largest rectangle has an area of 10.

## Approach
The approach is to use a stack to keep track of the indices of the bars. We iterate through the array and push the indices onto the stack if the current bar is higher than or equal to the bar at the top of the stack. If the current bar is lower than the bar at the top of the stack, we calculate the area of the rectangle with the bar at the top of the stack as the smallest bar.

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
        int h = (i == n) ? 0 : heights[i];
        while (!st.empty() && heights[st.top()] > h) {
            int height = heights[st.top()];
            st.pop();
            int width = st.empty() ? i : i - st.top() - 1;
            maxArea = max(maxArea, height * width);
        }
        st.push(i);
    }
    
    return maxArea;
}
```

## Test Cases
```
Input: [2,1,5,6,2,3]
Output: 10
Input: [2,4]
Output: 2
```

## Key Takeaways
- Use a stack to keep track of the indices of the bars in the histogram.
- Calculate the area of the rectangle with the bar at the top of the stack as the smallest bar when a smaller bar is encountered.
- Keep track of the maximum area found so far.