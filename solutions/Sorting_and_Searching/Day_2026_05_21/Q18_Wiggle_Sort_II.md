# Wiggle Sort II

## Problem Statement
Given an integer array `nums`, reorder it in-place such that `nums[0] <= nums[1] >= nums[2] <= nums[3]...`. You may assume the length of `nums` is at least 2. The solution should have a time complexity of O(n log n) and a space complexity of O(n). For example, if the input array is `[1, 5, 1, 1, 6, 4]`, one possible output is `[1, 6, 1, 5, 1, 4]`.

## Approach
The approach is to first sort the array and then rearrange the elements to satisfy the wiggle sort condition. We can use a two-pointer technique to achieve this in a single pass. The idea is to place the smallest elements at the even indices and the largest elements at the odd indices.

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
        
        // Traverse the input array and place the elements at the correct positions
        for (int i = 0; i < nums.size(); i++) {
            if (i % 2 == 0) {
                // Place the smallest element at the even index
                nums[i] = sortedNums[small++];
            } else {
                // Place the largest element at the odd index
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
Input: [1, 3, 2, 2, 3, 1]
Output: [1, 3, 1, 3, 2, 2]
```

## Key Takeaways
- First, sort the input array to have a clear understanding of the smallest and largest elements.
- Use a two-pointer technique to place the elements at the correct positions in a single pass.
- The solution has a time complexity of O(n log n) due to the sorting step, and a space complexity of O(n) for the sorted array.