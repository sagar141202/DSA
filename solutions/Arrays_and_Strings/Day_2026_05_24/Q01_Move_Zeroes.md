# Move Zeroes

## Problem Statement
Given an array of integers, move all the zeroes to the end of the array while maintaining the relative order of non-zero elements. The input array will contain integers between -10^9 and 10^9, and the size of the array will be between 1 and 10^5. For example, if the input array is [0, 1, 0, 3, 12], the output should be [1, 3, 12, 0, 0]. If the input array is [4, 2, 4, 0, 0, 3, 0, 5, 1, 0], the output should be [4, 2, 4, 3, 5, 1, 0, 0, 0, 0].

## Approach
The algorithm uses two pointers, one for reading and one for writing, to iterate through the array and move non-zero elements to the front. The writing pointer only moves when a non-zero element is found, effectively shifting all non-zero elements to the front of the array. This approach ensures that the relative order of non-zero elements is maintained.

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
            // If the current element is not zero, move it to the front
            if (nums[read] != 0) {
                // Swap the current element with the element at the writing pointer
                swap(nums[write], nums[read]);
                // Move the writing pointer forward
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
- Use two pointers to iterate through the array and move non-zero elements to the front.
- The writing pointer only moves when a non-zero element is found, effectively shifting all non-zero elements to the front of the array.
- This approach ensures that the relative order of non-zero elements is maintained and has a time complexity of O(n) and a space complexity of O(1).