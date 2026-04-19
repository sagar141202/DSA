# Move Zeroes

## Problem Statement
Given an array of integers, move all the zeroes to the end of the array while maintaining the relative order of non-zero elements. The array can contain duplicate elements and can be empty. The function should modify the input array in-place and return the modified array.

## Approach
The approach involves using two pointers to track the position of the next non-zero element and the current element being processed. We iterate through the array and swap non-zero elements with the next available position.

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
        int left = 0; // pointer for non-zero elements
        
        // Iterate through the array
        for (int right = 0; right < nums.size(); right++) {
            // If the current element is not zero, swap it with the next available position
            if (nums[right] != 0) {
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
Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Input: [4,2,4,0,0,3,0,5,1,0]
Output: [4,2,4,3,5,1,0,0,0,0]
```

## Key Takeaways
- We use two pointers to keep track of the position of the next non-zero element and the current element being processed.
- The time complexity is O(n) because we only iterate through the array once.
- The space complexity is O(1) because we only use a constant amount of space to store the pointers.