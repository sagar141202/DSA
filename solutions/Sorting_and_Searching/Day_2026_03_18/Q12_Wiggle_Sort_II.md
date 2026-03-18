# Wiggle Sort II

## Problem Statement
Given an integer array `nums`, sort it in-place such that `nums[0] <= nums[1] >= nums[2] <= nums[3]...`. The length of the array is at least 2 and at most 16. You may assume the input array is non-empty and the length of `nums` is even. For example, if the input array is `[1, 5, 1, 1, 6, 4]`, one possible answer is `[1, 6, 1, 5, 1, 4]`.

## Approach
We can first sort the array in ascending order, then rearrange the elements to satisfy the wiggle sort condition. The rearrangement can be done by swapping elements at even and odd indices.

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
        // Sort the array in ascending order
        vector<int> sortedNums = nums;
        sort(sortedNums.begin(), sortedNums.end());
        
        // Rearrange the elements to satisfy the wiggle sort condition
        int small = 0, large = nums.size() - 1;
        for (int i = 0; i < nums.size(); i++) {
            if (i % 2 == 0) {
                nums[i] = sortedNums[small++];
            } else {
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
- First, sort the array in ascending order to get the smallest and largest elements.
- Then, rearrange the elements to satisfy the wiggle sort condition by swapping elements at even and odd indices.
- The time complexity is O(n log n) due to the sorting step, and the space complexity is O(n) for storing the sorted array.