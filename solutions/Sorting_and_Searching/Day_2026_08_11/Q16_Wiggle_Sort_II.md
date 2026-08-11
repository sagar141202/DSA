# Wiggle Sort II

## Problem Statement
Given an integer array `nums`, sort the array in-place such that the array becomes a wiggle sequence, i.e., every alternate element is greater than its neighboring elements. The first element can be either greater than or less than the second element. For example, `[1, 5, 1, 5, 1]` and `[1, 2, 3, 4, 5]` are not valid wiggle sequences, but `[1, 3, 1, 5, 1]` and `[5, 1, 5, 1, 5]` are valid wiggle sequences. If there are multiple possible answers, return any one of them.

## Approach
The algorithm involves first sorting the array, then rearranging the elements to create a wiggle sequence. We can achieve this by placing the smaller half of the elements at the even indices and the larger half at the odd indices.

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
        
        int small = (n - 1) / 2, large = n - 1;
        
        for (int i = 0; i < n; i++) {
            if (i % 2 == 0) {
                nums[i] = temp[small--];
            } else {
                nums[i] = temp[large--];
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
- First, we need to sort the input array to easily access the smaller and larger elements.
- We use two pointers, `small` and `large`, to keep track of the current smaller and larger elements to be placed in the wiggle sequence.
- The `small` pointer starts at the middle of the sorted array and moves backwards, while the `large` pointer starts at the end of the sorted array and moves backwards.