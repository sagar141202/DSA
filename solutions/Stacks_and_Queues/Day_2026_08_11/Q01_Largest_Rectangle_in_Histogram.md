# Largest Rectangle in Histogram

## Problem Statement
Given an array of integers `heights` representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram. The histogram is represented as a list of integers, where each integer represents the height of a bar. The area of a rectangle is calculated as the product of its width and height. The constraints are: `1 <= heights.length <= 100000` and `0 <= heights[i] <= 10^5`.

## Approach
The approach is to use a stack-based solution, where we iterate through the histogram and push the indices of the bars onto the stack. We calculate the area of the rectangle with the current bar as the smallest bar when we encounter a bar that is smaller than the bar at the top of the stack. The area is calculated as the product of the width (current index - index at top of stack - 1) and the height (height of the bar at the top of the stack).

## Complexity
- Time: O(n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

int largestRectangleArea(vector<int>& heights) {
    // Initialize stack to store indices of bars
    stack<int> s;
    int maxArea = 0;
    int index = 0;
    
    // Iterate through histogram
    while (index < heights.size()) {
        // If stack is empty or current bar is higher than bar at top of stack, push index onto stack
        if (s.empty() || heights[index] >= heights[s.top()]) {
            s.push(index);
            index++;
        } else {
            // Calculate area of rectangle with current bar as smallest bar
            int top = s.top();
            s.pop();
            int width = s.empty() ? index : index - s.top() - 1;
            int area = heights[top] * width;
            maxArea = max(maxArea, area);
        }
    }
    
    // Calculate area of remaining bars in stack
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
Input: heights = [2,1,5,6,2,3]
Output: 10
Input: heights = [2,4]
Output: 2
```

## Key Takeaways
- Use a stack to store indices of bars in the histogram.
- Calculate the area of the rectangle with the current bar as the smallest bar when encountering a bar that is smaller than the bar at the top of the stack.
- Iterate through the histogram and update the maximum area found.