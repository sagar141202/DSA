# Largest Rectangle in Histogram

## Problem Statement
Given an array of integers `heights` representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram. The histogram is drawn such that the x-axis is horizontal and the y-axis is vertical. The area of a rectangle is calculated as the product of its width and height. The input array will contain at least one element and no more than 10^4 elements. Each element in the array will be a non-negative integer not exceeding 10^4. For example, given `heights = [2,1,5,6,2,3]`, the output should be `10` because the largest rectangle has a width of 2 and a height of 5, giving an area of 10.

## Approach
The algorithm uses a stack to store indices of the histogram bars. It iterates through the histogram, pushing indices onto the stack when the current bar is higher than or equal to the bar at the top of the stack, and calculating the area of the rectangle with the bar at the top of the stack as the smallest bar when the current bar is lower. The maximum area found during this process is the area of the largest rectangle in the histogram. The stack is used to keep track of the indices of the bars that are still "active" (i.e., they have not been popped from the stack yet).

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
        // If the stack is empty or the current bar is higher than the bar at the top of the stack, push the current index onto the stack
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
Input: heights = [2,1,5,6,2,3]
Output: 10
Input: heights = [2,4]
Output: 4
```

## Key Takeaways
- The stack is used to store indices of the histogram bars, allowing us to efficiently calculate the width of the rectangle.
- The algorithm iterates through the histogram only once, resulting in a time complexity of O(n).
- The space complexity is O(n) due to the use of the stack to store indices of the histogram bars.