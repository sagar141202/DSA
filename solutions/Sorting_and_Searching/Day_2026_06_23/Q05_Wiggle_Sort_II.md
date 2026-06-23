# Wiggle Sort II

## Problem Statement
Given an integer array `nums`, sort it in-place such that `nums[0] <= nums[1] >= nums[2] <= nums[3]...`. The array should be wiggle sorted, meaning that each element is either greater than or equal to its neighbors if it's at an even index, or less than or equal to its neighbors if it's at an odd index. If there are multiple possible answers, any of them will be accepted. For example, given `nums = [1, 5, 1, 1, 6, 4]`, one possible answer is `[1, 4, 1, 5, 1, 6]`.

## Approach
The approach is to first sort the array and then rearrange the elements to satisfy the wiggle sort condition. We can use a two-pointer technique to achieve this.

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
        
        int small = (n - 1) / 2, large = n - 1;
        for (int i = 0; i < n; i++) {
            if (i % 2 == 0) {
                nums[i] = sortedNums[small--];
            } else {
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
- Sort the array first to get a clear view of the smallest and largest elements.
- Use two pointers, one starting from the middle of the array and one from the end, to assign elements to the `nums` array in a wiggle sort order.
- The time complexity is dominated by the sorting operation, which is O(n log n) in the worst case.