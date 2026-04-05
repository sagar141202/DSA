# Wiggle Sort II

## Problem Statement
Given an integer array `nums`, sort it in-place such that `nums[0] <= nums[1] >= nums[2] <= nums[3]...`. The array should be sorted in a way that the first element is the smallest, the second element is the largest among the remaining elements, the third element is the smallest among the remaining elements, and so on. If there are multiple possible solutions, any of them will be accepted. The input array `nums` has a length of `n`, where `1 <= n <= 10^5`. The elements in the array are distinct and within the range `0 <= nums[i] <= 10^9`.

## Approach
The solution involves first sorting the array in ascending order, then rearranging the elements to achieve the wiggle sort order. The rearrangement is done by iterating over the sorted array and placing the elements at their correct positions in the original array.

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
        // Iterate over the input array and place the elements at their correct positions
        for (int i = 0; i < nums.size(); i++) {
            if (i % 2 == 0) {
                // Place the smallest remaining element at the current position
                nums[i] = sortedNums[small++];
            } else {
                // Place the largest remaining element at the current position
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
- First, sort the input array in ascending order to easily access the smallest and largest elements.
- Then, iterate over the input array and place the elements at their correct positions to achieve the wiggle sort order.
- The solution has a time complexity of O(n log n) due to the sorting step, and a space complexity of O(n) for the sorted copy of the input array.