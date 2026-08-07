# Largest Rectangle in Histogram

## Problem Statement
Given an array of integers representing the heights of bars in a histogram, find the area of the largest rectangle that can be formed using these bars. The width of each bar is 1 unit, and the height is given by the corresponding integer in the array. The rectangle must be formed using consecutive bars in the histogram.

## Approach
The algorithm uses a stack to keep track of the indices of the bars. It iterates through the array, pushing indices onto the stack when the current bar is higher than or equal to the bar at the top of the stack, and popping indices when the current bar is lower. The area of the rectangle that can be formed using the bar at the popped index is calculated and compared to the maximum area found so far.

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
        // push a dummy bar of height 0 at the end
        int height = (i == n) ? 0 : heights[i];
        
        while (!st.empty() && heights[st.top()] > height) {
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
- Calculate the area of the rectangle that can be formed using the bar at the popped index.
- Keep track of the maximum area found so far.