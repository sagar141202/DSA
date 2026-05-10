# Wiggle Sort II

## Problem Statement
Given an integer array `nums`, reorder it in-place such that `nums[0] <= nums[1] >= nums[2] <= nums[3]...`. You may assume the input array always has a valid answer. For example, if the input is `[1, 5, 1, 1, 6, 4]`, one possible answer is `[1, 4, 1, 5, 1, 6]`.

## Approach
We will first sort the array, then use two pointers to construct the result array in a wiggle sort order. The two pointers will start from the smallest and the largest number in the sorted array.

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
        
        // Iterate over the input array and fill it in a wiggle sort order
        for (int i = 0; i < nums.size(); i++) {
            if (i % 2 == 0) {
                // If the index is even, fill it with the smallest number
                nums[i] = sortedNums[small++];
            } else {
                // If the index is odd, fill it with the largest number
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
- First, sort the input array to have a clear order of the numbers.
- Use two pointers to fill the input array in a wiggle sort order, one starting from the smallest number and one from the largest.
- The time complexity is O(n log n) due to the sorting operation.