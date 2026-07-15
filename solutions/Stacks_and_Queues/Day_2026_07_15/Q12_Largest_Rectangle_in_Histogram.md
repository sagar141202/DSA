# Largest Rectangle in Histogram

## Problem Statement
Given an array of integers representing the heights of bars in a histogram, find the area of the largest rectangle that can be formed using these bars. The width of each bar is 1 unit. The input array will contain at least one element and at most 10,000 elements. Each element will be between 1 and 10,000. For example, given the array [2, 1, 5, 6, 2, 3], the largest rectangle has an area of 10 units, which can be formed using the bars of height 5 and 6, and the bars of width 2.

## Approach
The algorithm uses a stack-based approach to keep track of the indices of the bars. It iterates through the array, pushing the indices of the bars onto the stack if the current bar is higher than the bar at the top of the stack. If the current bar is lower, it calculates the area of the rectangle that can be formed using the bar at the top of the stack as the smallest bar.

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
    
    // calculate the left boundary for each bar
    for (int i = 0; i < n; i++) {
        while (!s.empty() && heights[s.top()] >= heights[i]) {
            s.pop();
        }
        left[i] = s.empty() ? 0 : s.top() + 1;
        s.push(i);
    }
    
    // clear the stack for the right boundary calculation
    while (!s.empty()) {
        s.pop();
    }
    
    // calculate the right boundary for each bar
    for (int i = n - 1; i >= 0; i--) {
        while (!s.empty() && heights[s.top()] >= heights[i]) {
            s.pop();
        }
        right[i] = s.empty() ? n - 1 : s.top() - 1;
        s.push(i);
    }
    
    // calculate the maximum area
    int maxArea = 0;
    for (int i = 0; i < n; i++) {
        int area = heights[i] * (right[i] - left[i] + 1);
        maxArea = max(maxArea, area);
    }
    
    return maxArea;
}

// alternative solution using a single pass
int largestRectangleAreaAlternative(vector<int>& heights) {
    int n = heights.size();
    stack<int> s;
    int maxArea = 0;
    
    for (int i = 0; i <= n; i++) {
        int h = i == n ? 0 : heights[i];
        while (!s.empty() && heights[s.top()] > h) {
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
Input: [2, 1, 5, 6, 2, 3]
Output: 10
Input: [2, 4]
Output: 2
```

## Key Takeaways
- The stack-based approach allows for efficient calculation of the left and right boundaries for each bar.
- The alternative solution using a single pass reduces the space complexity by avoiding the need for separate left and right boundary arrays.
- The time complexity remains O(n) due to the single pass through the input array.