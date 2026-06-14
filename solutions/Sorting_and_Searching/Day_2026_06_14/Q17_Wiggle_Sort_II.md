# Wiggle Sort II

## Problem Statement
Given an integer array `nums`, reorder it in-place such that `nums[0] <= nums[1] >= nums[2] <= nums[3]...`. Assume that the input array `nums` has at least 2 elements and that the length of `nums` is even. The output should be in the same array `nums`.

## Approach
The approach is to first sort the array in ascending order, then rearrange the elements to achieve the wiggle sort order. This can be done by placing the smallest element at the first position, the next smallest at the third, and so on, while placing the largest element at the second position, the next largest at the fourth, and so on.

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
        // Create a copy of the original array
        vector<int> copy = nums;
        
        // Sort the copy in ascending order
        sort(copy.begin(), copy.end());
        
        int small = 0, large = copy.size() - 1;
        
        // Rearrange the elements in the original array
        for (int i = 0; i < nums.size(); i++) {
            if (i % 2 == 0) {
                nums[i] = copy[small++];
            } else {
                nums[i] = copy[large--];
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
- First, sort the array in ascending order to easily access the smallest and largest elements.
- Then, rearrange the elements to achieve the wiggle sort order by placing the smallest element at the first position, the next smallest at the third, and so on, while placing the largest element at the second position, the next largest at the fourth, and so on.
- The `wiggleSort` function modifies the input array in-place.