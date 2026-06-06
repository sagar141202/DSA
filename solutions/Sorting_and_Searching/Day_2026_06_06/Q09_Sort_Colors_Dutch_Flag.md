# Sort Colors (Dutch Flag)

## Problem Statement
Given an array of integers containing only 0s, 1s, and 2s, sort the array in-place such that all 0s are first, followed by all 1s, and then all 2s. The problem is also known as the Dutch Flag problem. The array is not necessarily sorted and may contain duplicate values. For example, given the array [2,0,2,1,1,0], the function should return [0,0,1,1,2,2]. The array should be sorted in-place, meaning that no additional space should be used.

## Approach
The algorithm uses three pointers to track the positions of 0s, 1s, and 2s. The idea is to maintain a pointer for the next 0 and the next 2, and then iterate through the array, swapping elements as necessary. This approach ensures that all 0s are placed before all 1s, and all 1s are placed before all 2s.

## Complexity
- Time: O(n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    void sortColors(vector<int>& nums) {
        int low = 0; // pointer for the next 0
        int high = nums.size() - 1; // pointer for the next 2
        int mid = 0; // pointer for the current element
        
        while (mid <= high) {
            if (nums[mid] == 0) {
                // swap the current element with the next 0
                swap(nums[low], nums[mid]);
                low++;
                mid++;
            } else if (nums[mid] == 2) {
                // swap the current element with the next 2
                swap(nums[mid], nums[high]);
                high--;
            } else {
                // the current element is 1, just move to the next element
                mid++;
            }
        }
    }
};
```

## Test Cases
```
Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Input: [0]
Output: [0]
Input: [1]
Output: [1]
```

## Key Takeaways
- Use three pointers to track the positions of 0s, 1s, and 2s.
- Swap elements in-place to sort the array without using extra space.
- The algorithm has a time complexity of O(n) and a space complexity of O(1), making it efficient for large inputs.