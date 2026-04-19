# Wiggle Sort II

## Problem Statement
Given an integer array `nums`, reorder it in-place such that `nums[0] <= nums[1] >= nums[2] <= nums[3]...`. You may assume the input array always has a valid answer. The length of the array is in the range [1, 5000]. The elements in the array are in the range [1, 10^4].

## Approach
The algorithm first finds the median of the array, then rearranges the elements to satisfy the wiggle sort condition. It uses a temporary array to store the sorted elements and then assigns them to the original array in a way that maintains the wiggle sort order.

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
        vector<int> temp = nums;
        sort(temp.begin(), temp.end());
        int mid = (n - 1) / 2;
        int small = mid, big = n - 1;
        
        for (int i = 0; i < n; i++) {
            if (i % 2 == 0) {
                nums[i] = temp[small--];
            } else {
                nums[i] = temp[big--];
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
- First, sort the input array to easily access the smallest and largest elements.
- Use two pointers, one starting from the middle of the sorted array (for the smallest elements) and one from the end (for the largest elements).
- Assign elements to the original array in a way that maintains the wiggle sort order, alternating between the smallest and largest elements.