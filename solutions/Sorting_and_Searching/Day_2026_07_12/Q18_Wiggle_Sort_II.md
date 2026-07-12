# Wiggle Sort II

## Problem Statement
Given an integer array `nums`, sort it in-place such that `nums[0] <= nums[1] >= nums[2] <= nums[3]...`. If the length of the array is odd, the last element should be in an increasing sequence (i.e., `nums[length - 2] <= nums[length - 1]`). The array should be sorted in a way that maximizes the length of the wiggle sequence. For example, given the array `[1, 5, 1, 1, 6, 4]`, one possible answer is `[1, 6, 1, 5, 1, 4]`.

## Approach
The approach is to first sort the array in ascending order, then rearrange the elements to form the wiggle sequence. We can achieve this by taking elements from the beginning and end of the sorted array alternately.

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
        vector<int> sorted_nums = nums;
        sort(sorted_nums.begin(), sorted_nums.end());
        
        int small = 0, large = n - 1;
        for (int i = 0; i < n; i++) {
            if (i % 2 == 0) {
                nums[i] = sorted_nums[small++];
            } else {
                nums[i] = sorted_nums[large--];
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
- First, sort the array in ascending order to have control over the arrangement of elements.
- Then, rearrange the elements to form the wiggle sequence by taking elements from the beginning and end of the sorted array alternately.
- This approach maximizes the length of the wiggle sequence and satisfies the problem constraints.