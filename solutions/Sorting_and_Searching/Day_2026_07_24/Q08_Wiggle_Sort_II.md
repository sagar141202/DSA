# Wiggle Sort II

## Problem Statement
Given an unsorted array `nums`, reorder it in-place such that `nums[0] <= nums[1] >= nums[2] <= nums[3]...`. You may assume the input has at least two elements and the input array can be modified in-place. For example, if the input is `[1, 5, 1, 1, 6, 4]`, one possible answer is `[1, 4, 1, 5, 1, 6]`.

## Approach
The algorithm involves first sorting the array, then finding the median. We use two pointers to rearrange the elements in a wiggle sort order. The smaller half of the elements will be placed at the even indices, and the larger half will be placed at the odd indices.

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
        vector<int> copy = nums;
        sort(copy.begin(), copy.end());
        
        int mid = (n - 1) / 2;
        int small = mid, big = n - 1;
        
        for (int i = 0; i < n; i++) {
            if (i % 2 == 0) {
                nums[i] = copy[small--];
            } else {
                nums[i] = copy[big--];
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
- First, we sort the array to easily find the median and split the array into two halves.
- We use two pointers, one starting from the median and one from the end, to fill the array in a wiggle sort order.
- The wiggle sort order is achieved by placing the smaller half of elements at even indices and the larger half at odd indices.