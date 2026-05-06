# Move Zeroes

## Problem Statement
Given an array of integers, move all the zeroes to the end of the array while maintaining the relative order of the non-zero elements. The array is modified in-place. For example, given the array `[0, 1, 0, 3, 12]`, the function should return `[1, 3, 12, 0, 0]`. The array can contain duplicate elements and can be empty. The length of the array will not exceed 10^4.

## Approach
The algorithm uses two pointers, one for reading and one for writing, to track the position of the next non-zero element. It iterates through the array, swapping non-zero elements with the next available position. This approach ensures that all non-zero elements are moved to the front of the array while maintaining their relative order.

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
        // Initialize two pointers, one for reading and one for writing
        int write = 0;
        
        // Iterate through the array
        for (int read = 0; read < nums.size(); read++) {
            // If the current element is not zero, swap it with the next available position
            if (nums[read] != 0) {
                swap(nums[read], nums[write]);
                // Move the write pointer forward
                write++;
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
- Use two pointers to track the position of the next non-zero element and the next available position.
- Swap non-zero elements with the next available position to maintain their relative order.
- The algorithm has a time complexity of O(n) and a space complexity of O(1), making it efficient for large inputs.