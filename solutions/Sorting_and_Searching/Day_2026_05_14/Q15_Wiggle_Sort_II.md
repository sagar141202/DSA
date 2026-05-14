# Wiggle Sort II

## Problem Statement
Given an integer array `nums`, reorder it in-place such that `nums[0] <= nums[1] >= nums[2] <= nums[3]...`. You may assume the length of `nums` is at least 2. The problem statement requires us to rearrange the elements to form a wiggle sort sequence. For example, if the input array is `[1, 5, 1, 1, 6, 4]`, one possible output is `[1, 4, 1, 5, 1, 6]`. The constraints are that the input array has at least two elements, and all elements are integers.

## Approach
The approach involves first sorting the array, then rearranging the elements to form the wiggle sort sequence. We can achieve this by placing the smaller half of the elements at the even indices and the larger half at the odd indices. This ensures that the resulting sequence satisfies the wiggle sort condition.

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
        int mid = (n - 1) / 2;
        int small = mid, big = n - 1;
        for (int i = 0; i < n; i++) {
            if (i % 2 == 0) {
                nums[i] = sorted[small--];
            } else {
                nums[i] = sorted[big--];
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
- First, sort the input array to easily access the smaller and larger halves of the elements.
- Use two pointers, one starting from the middle of the sorted array (for smaller elements) and one from the end (for larger elements), to fill the resulting array in a wiggle sort order.
- The wiggle sort sequence can be formed by alternating between the smaller and larger halves of the sorted array.