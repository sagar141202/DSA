# Largest Rectangle in Histogram

## Problem Statement
Given an array of integers `heights` representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram. The input array `heights` will contain at least one element and at most 10,000 elements, and each element will be between 0 and 10,000. For example, given `heights = [2,1,5,6,2,3]`, the output should be `10` because the largest rectangle has an area of 10.

## Approach
The algorithm uses a stack to keep track of the indices of the bars. It iterates through the histogram, pushing indices onto the stack when the current bar is higher than the bar at the top of the stack, and calculating the area of the rectangle when the current bar is lower. The maximum area found is returned as the result. The key idea is to use the stack to efficiently find the left and right boundaries of the rectangle.

## Complexity
- Time: O(n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

int largestRectangleArea(vector<int>& heights) {
    int n = heights.size();
    vector<int> left(n), right(n);
    stack<int> s;
    
    // find left boundary
    for (int i = 0; i < n; i++) {
        while (!s.empty() && heights[s.top()] >= heights[i]) {
            s.pop();
        }
        left[i] = s.empty() ? 0 : s.top() + 1;
        s.push(i);
    }
    
    while (!s.empty()) {
        s.pop();
    }
    
    // find right boundary
    for (int i = n - 1; i >= 0; i--) {
        while (!s.empty() && heights[s.top()] >= heights[i]) {
            s.pop();
        }
        right[i] = s.empty() ? n - 1 : s.top() - 1;
        s.push(i);
    }
    
    int maxArea = 0;
    for (int i = 0; i < n; i++) {
        maxArea = max(maxArea, heights[i] * (right[i] - left[i] + 1));
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
- Use a stack to efficiently find the left and right boundaries of the rectangle.
- Calculate the area of the rectangle by multiplying the height of the bar by the width of the rectangle.
- Keep track of the maximum area found during the iteration.