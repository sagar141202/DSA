# Move Zeroes

## Problem Statement
Given an array of integers, move all the zeroes to the end of the array while maintaining the relative order of the non-zero elements. The problem statement requires us to modify the input array in-place and return the modified array. For example, if the input array is [0, 1, 0, 3, 12], the output should be [1, 3, 12, 0, 0]. The constraints of the problem are that the input array will contain only non-negative integers and the size of the array will be in the range [0, 10000].

## Approach
The approach to solve this problem is to use a two-pointer technique. We will maintain two pointers, one for the non-zero elements and one for the current element being processed. When a non-zero element is found, we will swap it with the element at the non-zero pointer and increment the non-zero pointer.

## Complexity
- Time: O(n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int nonZeroPtr = 0; // pointer for non-zero elements
        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] != 0) { // if current element is not zero
                swap(nums[nonZeroPtr], nums[i]); // swap with non-zero pointer
                nonZeroPtr++; // increment non-zero pointer
            }
        }
    }
};
```

## Test Cases
```
Input: [0, 1, 0, 3, 12]
Output: [1, 3, 12, 0, 0]
Input: [4, 2, 4, 0, 0, 3, 0, 5, 1, 0]
Output: [4, 2, 4, 3, 5, 1, 0, 0, 0, 0]
```

## Key Takeaways
- Use a two-pointer technique to solve the problem efficiently.
- Swap non-zero elements with the element at the non-zero pointer to maintain the relative order.
- The time complexity of the solution is linear, making it efficient for large inputs.