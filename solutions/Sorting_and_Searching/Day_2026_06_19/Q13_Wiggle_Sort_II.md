# Wiggle Sort II

## Problem Statement
Given an integer array `nums`, sort the array in a way that it becomes a wiggle sequence (alternating between smaller and larger elements). A wiggle sequence is defined as a sequence where for every pair of adjacent elements, the difference in value is either increasing or decreasing. The first difference (if all other conditions are equal) should be positive. If there are multiple possible solutions, return any of them. The length of the array will be in the range [1, 5000]. The integers in the array will be in the range [-5000, 5000].

## Approach
The algorithm involves first sorting the array, then rearranging the elements to create a wiggle sequence. This can be achieved by placing the smallest element at the first position, the next smallest at the third, and so on, while placing the largest element at the second position, the next largest at the fourth, and so on.

## Complexity
- Time: O(n log n)
- Space: O(n)

## C++ Solution
```cpp
#include <vector>
#include <algorithm>

class Solution {
public:
    void wiggleSort(std::vector<int>& nums) {
        int n = nums.size();
        std::vector<int> sortedNums = nums;
        std::sort(sortedNums.begin(), sortedNums.end());
        
        int mid = (n - 1) / 2;
        int small = mid, big = n - 1;
        
        for (int i = 0; i < n; i++) {
            if (i % 2 == 0) {
                nums[i] = sortedNums[small--];
            } else {
                nums[i] = sortedNums[big--];
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
- First, sort the input array to easily access the smallest and largest elements.
- Then, rearrange the elements by alternating between the smallest and largest remaining elements.
- The resulting sequence will be a wiggle sequence, satisfying the problem constraints.