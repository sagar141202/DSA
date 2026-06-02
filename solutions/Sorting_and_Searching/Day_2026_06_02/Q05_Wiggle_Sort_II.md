# Wiggle Sort II

## Problem Statement
Given an integer array `nums`, sort the array in a way that all the even-indexed elements are in increasing order and all the odd-indexed elements are in decreasing order. If there are multiple possible answers, return any of them. The array should be sorted in-place. For example, given `nums = [1, 5, 1, 1, 6, 4]`, one possible answer is `[1, 6, 1, 5, 1, 4]`.

## Approach
To solve this problem, we first sort the array in ascending order. Then, we create a new array where the even-indexed elements are taken from the beginning of the sorted array and the odd-indexed elements are taken from the end of the sorted array. This way, we ensure that the even-indexed elements are in increasing order and the odd-indexed elements are in decreasing order.

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
        vector<int> sorted = nums;
        sort(sorted.begin(), sorted.end());
        
        int small = (n - 1) / 2, large = n - 1;
        for (int i = 0; i < n; i++) {
            if (i % 2 == 0) {
                nums[i] = sorted[small--];
            } else {
                nums[i] = sorted[large--];
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
- First, we sort the array in ascending order to get the smallest and largest elements.
- Then, we create a new array where the even-indexed elements are taken from the beginning of the sorted array and the odd-indexed elements are taken from the end of the sorted array.
- We use two pointers, `small` and `large`, to keep track of the current smallest and largest elements in the sorted array.