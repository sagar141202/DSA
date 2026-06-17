# Container With Most Water

## Problem Statement
Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). Find two lines, which, together with the x-axis forms a container, such that the area of water it contains is maximal. The program should return this maximum area. The height of each line is given by the array height = [a1, a2, ..., an]. The width of each line is 1 unit. The lines are numbered from 1 to n, and the program should find the maximum area between any two lines. For example, given the array height = [1,8,6,2,5,4,8,3,7], the maximum area that can be trapped is 49.

## Approach
The algorithm uses a two-pointer technique, starting from both ends of the array and moving towards the center. The area between two lines is calculated as the minimum height of the two lines multiplied by the distance between them. The maximum area is updated at each step if a larger area is found. This approach ensures that all possible pairs of lines are considered.

## Complexity
- Time: O(n)
- Space: O(1)

## C++ Solution
```cpp
#include <vector>
using namespace std;

int maxArea(vector<int>& height) {
    int max_area = 0;
    int left = 0;
    int right = height.size() - 1;
    
    while (left < right) {
        // calculate the area between the two lines
        int area = min(height[left], height[right]) * (right - left);
        
        // update the maximum area if necessary
        max_area = max(max_area, area);
        
        // move the pointer of the shorter line towards the center
        if (height[left] < height[right]) {
            left++;
        } else {
            right--;
        }
    }
    
    return max_area;
}
```

## Test Cases
```
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Input: height = [1,1]
Output: 1
```

## Key Takeaways
- Use a two-pointer technique to consider all possible pairs of lines efficiently.
- The area between two lines is determined by the minimum height of the two lines and the distance between them.
- Move the pointer of the shorter line towards the center to ensure that all possible pairs are considered.