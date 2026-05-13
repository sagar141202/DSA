# Largest Rectangle in Histogram

## Problem Statement
Given an array of integers `heights` representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram. The input array will have a length of at least 1 and at most 10^5, and the values in the array will be between 0 and 10^5. For example, given `heights = [2,1,5,6,2,3]`, the output should be `10` because the largest rectangle has an area of 10 (5 x 2).

## Approach
We can use a stack-based approach to solve this problem by maintaining a stack of indices of the histogram bars. We iterate over the histogram, pushing the current index onto the stack if the current bar is higher than or equal to the bar at the top of the stack, and popping the stack if the current bar is lower than the bar at the top of the stack. We calculate the area of the rectangle with the popped bar as the smallest bar.

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
    
    // Iterate over the histogram
    for (int i = 0; i < heights.size(); i++) {
        // If the current bar is lower than the bar at the top of the stack, pop the stack
        while (s.top() != -1 && heights[s.top()] > heights[i]) {
            int top = s.top();
            s.pop();
            // Calculate the area of the rectangle with the popped bar as the smallest bar
            maxArea = max(maxArea, heights[top] * (i - s.top() - 1));
        }
        // Push the current index onto the stack
        s.push(i);
    }
    
    // Pop the remaining bars from the stack
    while (s.top() != -1) {
        int top = s.top();
        s.pop();
        // Calculate the area of the rectangle with the popped bar as the smallest bar
        maxArea = max(maxArea, heights[top] * (heights.size() - s.top() - 1));
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
- Pop the stack when a smaller bar is encountered and calculate the area of the rectangle.
- Handle the remaining bars in the stack after iterating over the histogram.