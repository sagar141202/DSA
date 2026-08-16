# Wiggle Sort II

## Problem Statement
Given an integer array `nums`, wiggle sort it in-place. You may assume the input array is non-empty and the length of `nums` is a power of 2. A wiggle sequence is an array such that every pair of adjacent elements in the sequence either increases or decreases in a alternating manner. For example, `[1, 3, 2, 5, 4]` and `[1, 2, 3, 4, 5]` are not wiggle sequences, but `[1, 3, 4, 2, 5]` is. Your task is to change the array in-place such that it becomes a wiggle sequence.

## Approach
The algorithm first sorts the array, then rearranges the elements to create a wiggle sequence. It uses a two-pointer technique to swap elements from the start and end of the sorted array.

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
        // Create a copy of the input array
        vector<int> copy = nums;
        
        // Sort the copy of the array
        sort(copy.begin(), copy.end());
        
        int small = (nums.size() - 1) / 2;
        int large = nums.size() - 1;
        
        // Rearrange the elements to create a wiggle sequence
        for (int i = 0; i < nums.size(); i++) {
            if (i % 2 == 0) {
                nums[i] = copy[small--];
            } else {
                nums[i] = copy[large--];
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
- First, sort the input array to have a clear ordering of elements.
- Use two pointers, one at the start and one at the end of the sorted array, to create the wiggle sequence.
- Swap elements from the start and end of the sorted array to create the wiggle sequence in the original array.