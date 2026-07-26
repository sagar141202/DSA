# Largest Rectangle in Histogram

## Problem Statement
Given an array of integers representing the heights of bars in a histogram, find the area of the largest rectangle that can be formed using these bars. The width of each bar is 1 unit, and the height is given by the corresponding value in the array. The rectangle must be formed by selecting a contiguous subset of the bars and the height of the rectangle is determined by the shortest bar in the subset.

## Approach
We use a stack-based approach to solve this problem. The idea is to maintain a stack of indices of the bars and keep track of the maximum area that can be formed. We iterate over the array, pushing indices onto the stack if the current bar is higher than the bar at the top of the stack, and popping indices if the current bar is lower.

## Complexity
- Time: O(n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

int largestRectangleArea(vector<int>& heights) {
    // Initialize the stack with -1 as the first element
    stack<int> s;
    s.push(-1);
    int maxArea = 0;
    
    // Iterate over the array
    for (int i = 0; i < heights.size(); i++) {
        // If the current bar is lower than the bar at the top of the stack, pop indices
        while (s.top() != -1 && heights[s.top()] >= heights[i]) {
            int height = heights[s.top()];
            s.pop();
            int width = i - s.top() - 1;
            maxArea = max(maxArea, height * width);
        }
        // Push the current index onto the stack
        s.push(i);
    }
    
    // Pop the remaining indices
    while (s.top() != -1) {
        int height = heights[s.top()];
        s.pop();
        int width = heights.size() - s.top() - 1;
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
- Use a stack to keep track of the indices of the bars.
- Iterate over the array, pushing and popping indices based on the height of the bars.
- Calculate the maximum area that can be formed by considering the width and height of the rectangle.