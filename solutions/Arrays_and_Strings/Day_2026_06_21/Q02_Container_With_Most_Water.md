# Container With Most Water

## Problem Statement
Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). Find two lines, which, together with the x-axis forms a container, such that the area of water it contains is maximal. The program should return this maximum area. The constraints are 2 <= a.length <= 10^5 and 0 <= a[i] <= 10^4.

## Approach
The algorithm uses a two-pointer approach, starting from both ends of the array and moving towards the center. The area of water that can be trapped between two lines is calculated at each step. The maximum area found so far is updated accordingly. This approach ensures that all possible pairs of lines are considered.

## Complexity
- Time: O(n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int maxArea(vector<int>& height) {
        int maxArea = 0;
        int left = 0;
        int right = height.size() - 1;
        
        while (left < right) {
            // Calculate the area of water that can be trapped between two lines
            int area = min(height[left], height[right]) * (right - left);
            maxArea = max(maxArea, area);
            
            // Move the pointer of the shorter line towards the center
            if (height[left] < height[right]) {
                left++;
            } else {
                right--;
            }
        }
        
        return maxArea;
    }
};
```

## Test Cases
```
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Input: height = [1,1]
Output: 1
```

## Key Takeaways
- The two-pointer approach is useful for solving problems that involve finding the maximum or minimum value of a function that depends on two variables.
- The area of water that can be trapped between two lines depends on the minimum height of the two lines and the distance between them.
- The time complexity of the solution is O(n), where n is the number of lines, because each line is visited at most once.