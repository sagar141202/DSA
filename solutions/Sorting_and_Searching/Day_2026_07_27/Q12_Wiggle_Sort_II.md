# Wiggle Sort II

## Problem Statement
Given an unsorted array `nums`, reorder it such that `nums[0] < nums[1] > nums[2] < nums[3]...`. You may assume the input has at least one element. The solution should be implemented in-place. For example, given `nums = [1, 5, 1, 1, 6, 4]`, one possible answer is `[1, 4, 1, 5, 1, 6]`.

## Approach
The approach involves first sorting the array, then rearranging the elements to achieve the wiggle pattern. This can be done by iterating over the sorted array and placing the smaller elements at the even indices and the larger elements at the odd indices.

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
        // Create a copy of the original array and sort it
        vector<int> sortedNums = nums;
        sort(sortedNums.begin(), sortedNums.end());
        
        // Initialize two pointers, one at the beginning and one at the end of the sorted array
        int small = 0, large = nums.size() - 1;
        
        // Iterate over the original array and fill it with elements from the sorted array
        for (int i = 0; i < nums.size(); i++) {
            // If the index is even, fill it with the smaller element
            if (i % 2 == 0) {
                nums[i] = sortedNums[small++];
            } 
            // If the index is odd, fill it with the larger element
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
- To achieve the wiggle pattern, we need to place the smaller elements at the even indices and the larger elements at the odd indices.
- We can use two pointers, one at the beginning and one at the end of the sorted array, to fill the original array with the elements in the correct order.
- The time complexity is O(n log n) due to the sorting operation, and the space complexity is O(n) for the sorted array.