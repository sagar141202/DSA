# Wiggle Sort II

## Problem Statement
Given an unsorted array `nums`, reorder it in-place such that `nums[0] <= nums[1] >= nums[2] <= nums[3]...`. You may assume the length of `nums` is at least 2. The solution should be implemented in a way that minimizes the number of swaps. For example, if the input is `[1, 5, 1, 1, 6, 4]`, one possible output is `[1, 6, 1, 5, 1, 4]`.

## Approach
The approach involves first sorting the array and then swapping elements to achieve the wiggle sort order. We can use a two-pointer technique to swap elements from the start and end of the array.

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
        // Create a copy of the array and sort it
        vector<int> sortedNums = nums;
        sort(sortedNums.begin(), sortedNums.end());
        
        // Initialize two pointers, one at the start and one at the end of the sorted array
        int small = 0, large = nums.size() - 1;
        
        // Traverse the array and swap elements to achieve the wiggle sort order
        for (int i = 0; i < nums.size(); i++) {
            if (i % 2 == 0) {
                nums[i] = sortedNums[small++];
            } else {
                nums[i] = sortedNums[large--];
            }
        }
    }
};

int main() {
    Solution solution;
    vector<int> nums = {1, 5, 1, 1, 6, 4};
    solution.wiggleSort(nums);
    for (int num : nums) {
        cout << num << " ";
    }
    return 0;
}
```

## Test Cases
```
Input: [1, 5, 1, 1, 6, 4]
Output: [1, 6, 1, 5, 1, 4]
```

## Key Takeaways
- The `wiggleSort` function first creates a sorted copy of the input array `nums`.
- It then uses two pointers, `small` and `large`, to swap elements from the start and end of the sorted array to achieve the wiggle sort order.
- The function modifies the input array `nums` in-place to achieve the desired order.