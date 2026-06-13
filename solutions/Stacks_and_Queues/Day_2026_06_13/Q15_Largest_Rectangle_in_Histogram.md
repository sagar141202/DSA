# Largest Rectangle in Histogram

## Problem Statement
Given an array of integers representing the heights of bars in a histogram, find the area of the largest rectangle that can be formed using these bars. The width of each bar is 1 unit, and the height is given by the corresponding value in the array. The rectangle must be formed using consecutive bars, and its height is determined by the shortest bar in the selected range.

## Approach
We will use a stack-based approach to solve this problem, where we maintain a stack of indices of the bars. We iterate over the array, pushing indices onto the stack if the current bar is higher than the bar at the top of the stack, and popping indices if the current bar is lower. For each popped index, we calculate the area of the rectangle that can be formed using the bar at that index as the smallest bar.

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
        // if stack is empty or current height is greater than height at top of stack, push index
        while (!st.empty() && (i == n || heights[st.top()] >= heights[i])) {
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
Input: heights = [2,1,5,6,2,3]
Output: 10
Input: heights = [2,4]
Output: 2
```

## Key Takeaways
- Use a stack to keep track of indices of bars in the histogram.
- Iterate over the array, pushing and popping indices as necessary to calculate the area of the largest rectangle.
- Keep track of the maximum area seen so far to return the final result.