# Wiggle Sort II

## Problem Statement
Given an unsorted array `nums`, reorder it in-place such that `nums[0] <= nums[1] >= nums[2] <= nums[3]...`. You may assume the input has at least two elements. The solution must be done in O(n log n) time complexity due to sorting. For example, given `nums = [1, 5, 1, 1, 6, 4]`, one possible answer is `[1, 4, 1, 5, 1, 6]`.

## Approach
The algorithm first sorts the input array in ascending order. Then it rearranges the elements to satisfy the wiggle sort condition by placing the smallest element at the first position, the next smallest at the third, and the largest at the second position, and so on.

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

        int small = 0, large = nums.size() - 1;
        // Iterate over the input array and place elements at correct positions
        for (int i = 0; i < nums.size(); i++) {
            // For even indices, place the smallest remaining element
            if (i % 2 == 0) {
                nums[i] = sortedNums[small++];
            }
            // For odd indices, place the largest remaining element
            else {
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
- First, sort the input array in ascending order.
- Then, rearrange the elements by placing the smallest elements at even indices and the largest elements at odd indices.
- The solution has a time complexity of O(n log n) due to the sorting operation and a space complexity of O(n) for storing the sorted array.