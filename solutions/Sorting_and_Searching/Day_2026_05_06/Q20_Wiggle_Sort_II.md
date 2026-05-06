# Wiggle Sort II

## Problem Statement
Given an integer array `nums`, reorder it in-place such that `nums[0] <= nums[1] >= nums[2] <= nums[3]...`. You may assume the length of `nums` is at least 2. The array should be sorted in a way that the smaller elements are at the even indices and the larger elements are at the odd indices, or vice versa.

## Approach
The approach is to first sort the array, then rearrange the elements to satisfy the wiggle sort condition. We can use a temporary array to store the sorted elements and then assign them to the original array in a way that alternates between smaller and larger elements.

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
        
        // Initialize two pointers, one at the beginning and one at the end of the sorted array
        int small = 0, large = nums.size() - 1;
        
        // Iterate over the input array and assign the elements in a way that satisfies the wiggle sort condition
        for (int i = 0; i < nums.size(); i++) {
            if (i % 2 == 0) {
                // Assign the smaller element at the even index
                nums[i] = sortedNums[small++];
            } else {
                // Assign the larger element at the odd index
                nums[i] = sortedNums[large--];
            }
        }
    }
};
```

## Test Cases
```
Input: nums = [1, 5, 1, 1, 6, 4]
Output: [1, 6, 1, 5, 1, 4]
```

## Key Takeaways
- First, sort the input array to get the smaller and larger elements.
- Then, assign the elements to the original array in a way that alternates between smaller and larger elements.
- Use two pointers, one at the beginning and one at the end of the sorted array, to keep track of the smaller and larger elements.