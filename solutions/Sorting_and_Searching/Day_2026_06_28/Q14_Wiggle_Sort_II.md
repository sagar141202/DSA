# Wiggle Sort II

## Problem Statement
Given an integer array `nums`, reorder it in-place such that `nums[0] <= nums[1] >= nums[2] <= nums[3]...`. The array should be wiggle sorted in a way that the smallest number is at the beginning and the second smallest number is at the second position, and so on, alternating between smaller and larger numbers. If there are multiple possible answers, any of them is acceptable. For example, given `nums = [1, 5, 1, 1, 6, 4]`, one possible answer is `[1, 4, 1, 5, 1, 6]`.

## Approach
The algorithm involves first sorting the array, then using two pointers to place the elements in their correct positions in the result array, alternating between smaller and larger numbers. We use a copy of the sorted array to keep track of the elements that have not been placed yet.

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
Input: [1, 5, 1, 1, 6, 4]
Output: [1, 4, 1, 5, 1, 6]
```

## Key Takeaways
- First, sort the array to have all elements in ascending order.
- Then, use two pointers to place the elements in their correct positions in the result array, alternating between smaller and larger numbers.
- The time complexity is O(n log n) due to the sorting step, and the space complexity is O(n) for the copy of the sorted array.