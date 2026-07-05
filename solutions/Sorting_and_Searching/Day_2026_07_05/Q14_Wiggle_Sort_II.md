# Wiggle Sort II

## Problem Statement
Given an integer array `nums`, reorder it in-place such that `nums[0] <= nums[1] >= nums[2] <= nums[3]...`. You may assume the length of `nums` is at least 2. The solution should be implemented using an efficient sorting and searching approach.

## Approach
The algorithm involves first sorting the array, then rearranging the elements to satisfy the wiggle sort condition. This can be achieved by placing the smallest elements at the even indices and the largest elements at the odd indices. The intuition is to maintain the alternating pattern of less than or equal to and greater than or equal to relationships between adjacent elements.

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
        
        // Initialize two pointers, one at the beginning and one at the end of the sorted array
        int small = 0, large = nums.size() - 1;
        
        // Traverse the input array, placing the smallest elements at the even indices and the largest elements at the odd indices
        for (int i = 0; i < nums.size(); i++) {
            if (i % 2 == 0) {
                nums[i] = sortedNums[small++];
            } else {
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
- The wiggle sort problem requires an efficient sorting and searching approach to reorder the input array in-place.
- The solution involves sorting the array and then rearranging the elements to satisfy the wiggle sort condition.
- The time complexity of the solution is O(n log n) due to the sorting operation, and the space complexity is O(n) for storing the sorted array.