# Move Zeroes

## Problem Statement
Given an array of integers, move all the zeroes to the end of the array while maintaining the relative order of the non-zero elements. The array can contain duplicate elements and can be empty. The goal is to achieve this in a single pass through the array. For example, if the input array is `[0, 1, 0, 3, 12]`, the output should be `[1, 3, 12, 0, 0]`. The array can have a maximum length of 10^4 and the integers can range from -10^4 to 10^4.

## Approach
The algorithm uses a two-pointer technique, where one pointer tracks the position of the next non-zero element and the other pointer iterates through the array. When a non-zero element is found, it is swapped with the element at the next non-zero position. This approach ensures that all non-zero elements are moved to the front of the array while maintaining their relative order.

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
        int nonZeroPtr = 0;
        
        // Iterate through the array
        for (int i = 0; i < nums.size(); i++) {
            // If the current element is not zero, swap it with the element at the nonZeroPtr
            if (nums[i] != 0) {
                swap(nums[nonZeroPtr], nums[i]);
                // Move the nonZeroPtr forward
                nonZeroPtr++;
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
- The two-pointer technique is useful for problems that require maintaining a certain order or position in the array.
- In-place algorithms can be more efficient than algorithms that require extra space.
- The relative order of elements can be maintained by swapping elements instead of shifting them.