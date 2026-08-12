# Move Zeroes

## Problem Statement
Given an array of integers, move all the zeroes to the end of the array while maintaining the relative order of non-zero elements. The input array can contain duplicate elements and can be of any size. For example, if the input array is `[0, 1, 0, 3, 12]`, the output should be `[1, 3, 12, 0, 0]`. The constraints are that the input array can have a maximum size of 10^4 and the elements can be in the range of -10^4 to 10^4.

## Approach
The algorithm uses a two-pointer technique to iterate through the array, swapping non-zero elements with the next available position. This approach ensures that all non-zero elements are moved to the front of the array while maintaining their relative order. The algorithm runs in linear time complexity.

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
        // Initialize two pointers, one for the next non-zero element and one for the current element
        int nonZeroIndex = 0;
        
        // Iterate through the array
        for (int i = 0; i < nums.size(); i++) {
            // If the current element is not zero, swap it with the next non-zero element
            if (nums[i] != 0) {
                swap(nums[nonZeroIndex], nums[i]);
                // Move the non-zero index forward
                nonZeroIndex++;
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
- The two-pointer technique can be used to solve problems that require maintaining a specific order or relative position of elements.
- The algorithm can be optimized to run in linear time complexity by only iterating through the array once.
- The space complexity can be reduced to O(1) by only using a constant amount of space to store the pointers and not creating any additional data structures.