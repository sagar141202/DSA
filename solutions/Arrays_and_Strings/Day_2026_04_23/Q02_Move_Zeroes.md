# Move Zeroes

## Problem Statement
Given an array of integers, move all the zeroes to the end of the array while maintaining the relative order of non-zero elements. The problem should be solved in-place, meaning no extra space is allowed except for a few variables. For example, given the array `[0, 1, 0, 3, 12]`, the output should be `[1, 3, 12, 0, 0]`. The array can contain duplicate elements and may have a length of up to 10^4 elements.

## Approach
The algorithm uses two pointers to track non-zero elements and swap them with the next available position. It iterates over the array, swapping non-zero elements to the front and keeping track of the next position to place a non-zero element.

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
        // Initialize two pointers
        int left = 0; // Pointer for non-zero elements

        // Iterate over the array
        for (int right = 0; right < nums.size(); right++) {
            // If the current element is not zero, swap it with the left pointer
            if (nums[right] != 0) {
                // Swap elements
                swap(nums[left], nums[right]);
                // Move the left pointer forward
                left++;
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
- Use two pointers to track non-zero elements and swap them with the next available position.
- Iterate over the array, swapping non-zero elements to the front and keeping track of the next position to place a non-zero element.
- The solution has a time complexity of O(n) and a space complexity of O(1), making it efficient for large inputs.