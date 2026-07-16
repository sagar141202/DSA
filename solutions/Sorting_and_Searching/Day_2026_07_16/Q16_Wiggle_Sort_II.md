# Wiggle Sort II

## Problem Statement
Given an integer array `nums`, reorder it in-place such that `nums[0] <= nums[1] >= nums[2] <= nums[3]...`. You may assume the length of `nums` is at least 2. The solution should be efficient and not use extra space. For example, if `nums = [1, 5, 1, 1, 6, 4]`, one possible answer is `[1, 4, 1, 5, 1, 6]`.

## Approach
The approach is to first sort the array, then rearrange the elements to satisfy the wiggle sort condition. We can use a two-pointer technique to achieve this in linear time. The idea is to place the smallest element at the first position, the largest element at the second position, the second smallest element at the third position, and so on.

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
        int n = nums.size();
        vector<int> sortedNums = nums;
        sort(sortedNums.begin(), sortedNums.end());
        
        int small = 0, large = n - 1;
        for (int i = 0; i < n; i++) {
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
Input: [1, 3, 2, 2, 3, 1]
Output: [1, 3, 1, 3, 2, 2]
```

## Key Takeaways
- First, we need to sort the array to get the smallest and largest elements.
- Then, we can use a two-pointer technique to rearrange the elements and satisfy the wiggle sort condition.
- The time complexity is O(n log n) due to the sorting operation, and the space complexity is O(n) for storing the sorted array.