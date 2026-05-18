# Largest Rectangle in Histogram

## Problem Statement
Given an array of integers representing the heights of bars in a histogram, find the area of the largest rectangle that can be formed using these bars. The width of each bar is 1 unit, and the height of each bar is given by the corresponding element in the array. The rectangle must be formed by selecting a contiguous subset of the bars and the area of the rectangle is the product of the width and the minimum height of the selected bars.

## Approach
The problem can be solved using a stack-based approach, where we maintain a stack of indices of the bars. We iterate through the array, pushing the indices of the bars onto the stack if the current bar is higher than the bar at the top of the stack, and popping the top of the stack and calculating the area of the rectangle that can be formed with the popped bar as the smallest bar if the current bar is lower. The maximum area found during the iteration is the area of the largest rectangle.

## Complexity
- Time: O(n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

int largestRectangleArea(vector<int>& heights) {
    int n = heights.size();
    stack<int> s;
    int maxArea = 0;
    for (int i = 0; i <= n; i++) {
        // If the stack is empty or the current bar is higher than the bar at the top of the stack, push the current index onto the stack
        while (!s.empty() && (i == n || heights[s.top()] > heights[i])) {
            int height = heights[s.top()];
            s.pop();
            int width = s.empty() ? i : i - s.top() - 1;
            maxArea = max(maxArea, height * width);
        }
        s.push(i);
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
- Iterate through the array, pushing and popping the stack based on the height of the current bar.
- Calculate the area of the rectangle that can be formed with the popped bar as the smallest bar.