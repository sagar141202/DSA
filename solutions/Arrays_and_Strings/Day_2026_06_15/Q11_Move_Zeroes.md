# Move Zeroes

## Problem Statement
Given an array of integers, move all the zeroes to the end of the array while maintaining the relative order of non-zero elements. The function should modify the input array in-place. For example, if the input array is `[0, 1, 0, 3, 12]`, the output should be `[1, 3, 12, 0, 0]`. The input array can contain duplicate elements and can be empty. The length of the input array is in the range `[0, 10^4]`.

## Approach
The approach is to use two pointers, one for tracking non-zero elements and the other for iterating through the array. We swap non-zero elements with the current pointer, effectively moving zeroes to the end. This way, we achieve the desired output in a single pass through the array.

## Complexity
- Time: O(n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

void moveZeroes(vector<int>& nums) {
    // Initialize two pointers
    int nonZeroPtr = 0; // Pointer for non-zero elements
    
    // Traverse through the array
    for (int i = 0; i < nums.size(); i++) {
        // If current element is not zero, swap it with the nonZeroPtr
        if (nums[i] != 0) {
            swap(nums[nonZeroPtr], nums[i]);
            // Move the nonZeroPtr forward
            nonZeroPtr++;
        }
    }
}
```

## Test Cases
```
Input: [0, 1, 0, 3, 12]
Output: [1, 3, 12, 0, 0]
Input: [4, 2, 4, 0, 0, 3, 0, 5, 1, 0]
Output: [4, 2, 4, 3, 5, 1, 0, 0, 0, 0]
```

## Key Takeaways
- We use two pointers to track non-zero elements and iterate through the array.
- The `nonZeroPtr` is used to keep track of the position where the next non-zero element should be placed.
- The time complexity is linear because we make a single pass through the input array.