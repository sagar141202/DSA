# Wiggle Sort II

## Problem Statement
Given an integer array nums, reorder it in-place such that nums[0] <= nums[1] >= nums[2] <= nums[3].... You may assume the input array always has a valid answer. The array should be rearranged in a way that the first element is the smallest, the second element is the largest, the third element is the second smallest, and so on. For example, if the input array is [1, 2, 3, 4, 5, 6], the output should be [1, 6, 2, 5, 3, 4].

## Approach
The approach is to first sort the array and then rearrange the elements to meet the wiggle sort condition. We can achieve this by taking elements from the start and end of the sorted array and placing them in the result array in an alternating manner.

## Complexity
- Time: O(n log n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    void wiggleSort(vector<int>& nums) {
        // Create a copy of the input array and sort it
        vector<int> sortedNums = nums;
        sort(sortedNums.begin(), sortedNums.end());
        
        // Initialize two pointers, one at the start and one at the end of the sorted array
        int small = 0, large = nums.size() - 1;
        
        // Iterate through the input array and fill it with the sorted elements in a wiggle manner
        for (int i = 0; i < nums.size(); i++) {
            if (i % 2 == 0) {
                // If the index is even, take the smallest element
                nums[i] = sortedNums[small++];
            } else {
                // If the index is odd, take the largest element
                nums[i] = sortedNums[large--];
            }
        }
    }
};
```

## Test Cases
```
Input: [1, 5, 1, 1, 6, 4]
Output: [1, 6, 1, 5, 1, 4]
```

## Key Takeaways
- First, sort the input array to easily access the smallest and largest elements.
- Use two pointers, one at the start and one at the end of the sorted array, to fill the input array in a wiggle manner.
- The time complexity is O(n log n) due to the sorting step, and the space complexity is O(n) for storing the sorted array.