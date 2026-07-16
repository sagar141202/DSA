# Move Zeroes

## Problem Statement
Given an array of integers, move all the zeroes to the end of the array while maintaining the relative order of non-zero elements. The input array will contain integers between -10^9 and 10^9, and the length of the array will be between 1 and 10^5. For example, if the input array is [0, 1, 0, 3, 12], the output should be [1, 3, 12, 0, 0].

## Approach
The algorithm uses a two-pointer technique to iterate through the array, swapping non-zero elements with the next available position. This approach ensures that all non-zero elements are moved to the front of the array while maintaining their relative order. The time complexity is optimized by only iterating through the array once.

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
        // Initialize two pointers, one at the beginning of the array
        int left = 0;
        
        // Iterate through the array with the right pointer
        for (int right = 0; right < nums.size(); right++) {
            // If the current element is not zero, swap it with the left pointer
            if (nums[right] != 0) {
                swap(nums[left], nums[right]);
                // Move the left pointer to the next position
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
- Use a two-pointer technique to iterate through the array and swap non-zero elements with the next available position.
- Maintain the relative order of non-zero elements by only swapping them with the next available position.
- Optimize the time complexity by only iterating through the array once.