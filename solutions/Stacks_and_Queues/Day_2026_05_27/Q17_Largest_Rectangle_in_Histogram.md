# Largest Rectangle in Histogram

## Problem Statement
Given an array of integers representing the heights of bars in a histogram, find the area of the largest rectangle that can be formed within the histogram. The histogram has a fixed width of 1 unit for each bar, and the height of each bar is given by the corresponding element in the array. The task is to calculate the maximum area of the rectangle that can be formed using the bars in the histogram. For example, given the array [2, 1, 5, 6, 2, 3], the maximum area of the rectangle that can be formed is 10.

## Approach
The approach to solve this problem is to use a stack-based algorithm, where we maintain a stack of indices of the bars in the histogram. We iterate through the array, pushing the indices of the bars onto the stack if the current bar is higher than or equal to the bar at the top of the stack. If the current bar is lower than the bar at the top of the stack, we calculate the area of the rectangle that can be formed using the bar at the top of the stack as the smallest bar.

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
        // push index of current bar onto stack if it's higher than or equal to the bar at the top of the stack
        while (!st.empty() && (i == n || heights[st.top()] > heights[i])) {
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
Input: [2, 1, 5, 6, 2, 3]
Output: 10
Input: [1]
Output: 1
```

## Key Takeaways
- Use a stack to keep track of the indices of the bars in the histogram.
- Calculate the area of the rectangle that can be formed using the bar at the top of the stack as the smallest bar when a smaller bar is encountered.
- Keep track of the maximum area encountered so far.