# Largest Rectangle in Histogram

## Problem Statement
Given an array of integers representing the heights of bars in a histogram, find the area of the largest rectangle that can be formed within the histogram. The histogram has a fixed width of 1 unit, and the height of each bar is given by the corresponding element in the array. The task is to find the maximum area of a rectangle with a fixed width and variable height that can be formed using the bars of the histogram. For example, given the array [2, 1, 5, 6, 2, 3], the largest rectangle that can be formed has an area of 10.

## Approach
The approach is to use a stack-based algorithm to keep track of the indices of the bars. We iterate through the array, pushing the indices of the bars onto the stack if the current bar is higher than the bar at the top of the stack. If the current bar is lower, we pop the top of the stack and calculate the area of the rectangle that can be formed with the popped bar as the smallest bar.

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
    int index = 0;
    
    // Iterate through the array
    while (index < heights.size()) {
        // If the stack is empty or the current bar is higher than the bar at the top of the stack, push the index onto the stack
        if (s.empty() || heights[index] >= heights[s.top()]) {
            s.push(index);
            index++;
        } else {
            // If the current bar is lower, pop the top of the stack and calculate the area of the rectangle
            int top = s.top();
            s.pop();
            int width = s.empty() ? index : index - s.top() - 1;
            int area = heights[top] * width;
            maxArea = max(maxArea, area);
        }
    }
    
    // Calculate the area of the rectangles with the remaining bars in the stack
    while (!s.empty()) {
        int top = s.top();
        s.pop();
        int width = s.empty() ? index : index - s.top() - 1;
        int area = heights[top] * width;
        maxArea = max(maxArea, area);
    }
    
    return maxArea;
}
```

## Test Cases
```
Input: [2, 1, 5, 6, 2, 3]
Output: 10
Input: [2, 4]
Output: 2
```

## Key Takeaways
- The stack-based algorithm allows us to efficiently keep track of the indices of the bars and calculate the area of the rectangles.
- The time complexity is O(n) because we only iterate through the array once and perform constant-time operations for each element.
- The space complexity is O(n) because in the worst case, we may need to store all the indices of the bars in the stack.