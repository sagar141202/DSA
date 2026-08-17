# Move Zeroes

## Problem Statement
Given an array of integers, move all the zeroes to the end of the array while maintaining the relative order of non-zero elements. The array can contain duplicate elements and can be empty. The function should modify the input array in-place and return the modified array.

## Approach
The algorithm uses two pointers, one for tracking non-zero elements and one for iterating through the array. When a non-zero element is found, it is swapped with the element at the non-zero pointer index, and the non-zero pointer is incremented.

## Complexity
- Time: O(n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

void moveZeroes(vector<int>& nums) {
    // initialize two pointers
    int nonZeroPtr = 0;
    
    // iterate through the array
    for (int i = 0; i < nums.size(); i++) {
        // if the current element is not zero, swap it with the element at nonZeroPtr
        if (nums[i] != 0) {
            swap(nums[nonZeroPtr], nums[i]);
            // increment nonZeroPtr
            nonZeroPtr++;
        }
    }
}
```

## Test Cases
```
Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Input: [4,2,4,0,0,3,0,5,1,0]
Output: [4,2,4,3,5,1,0,0,0,0]
```

## Key Takeaways
- Use two pointers to track non-zero elements and iterate through the array.
- Swap non-zero elements with the element at the non-zero pointer index to maintain relative order.
- Increment the non-zero pointer after each swap to keep track of the next position for a non-zero element.