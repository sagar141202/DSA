# Wiggle Sort II

## Problem Statement
Given an integer array `nums`, reorder it in-place such that `nums[0] <= nums[1] >= nums[2] <= nums[3]...`. Assume that the input array has enough elements to form a wiggle sequence. For example, given `nums = [1, 5, 1, 1, 6, 4]`, one possible answer is `[1, 6, 1, 5, 1, 4]`. The array should be sorted in a way that it forms a wiggle sequence, with the first element being less than or equal to the second element, the second element being greater than or equal to the third element, and so on.

## Approach
The approach to solve this problem is to first sort the array in ascending order. Then, we can create a new array with the elements from the sorted array, but with the elements at the even indices coming from the first half of the sorted array (in reverse order) and the elements at the odd indices coming from the second half of the sorted array (also in reverse order). This way, we can ensure that the resulting array forms a wiggle sequence.

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
        // Create a copy of the input array and sort it in ascending order
        vector<int> sortedNums = nums;
        sort(sortedNums.begin(), sortedNums.end());
        
        // Initialize two pointers, one at the beginning and one at the end of the sorted array
        int small = 0, large = nums.size() - 1;
        
        // Iterate over the input array and fill it with the elements from the sorted array
        for (int i = 0; i < nums.size(); i++) {
            // If the index is even, fill it with the element from the beginning of the sorted array
            if (i % 2 == 0) {
                nums[i] = sortedNums[small++];
            } 
            // If the index is odd, fill it with the element from the end of the sorted array
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
- To create a wiggle sequence, we can use a sorted array and fill the input array with elements from the sorted array in a way that alternates between the beginning and the end of the sorted array.
- The time complexity of this solution is O(n log n) due to the sorting operation, where n is the number of elements in the input array.
- The space complexity is O(n) because we need to create a copy of the input array to sort it.