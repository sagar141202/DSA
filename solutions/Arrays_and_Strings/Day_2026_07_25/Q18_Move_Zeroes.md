# Move Zeroes

## Problem Statement
Given an array of integers `nums`, move all the zeroes to the end of the array while maintaining the relative order of non-zero elements. The function should modify the input array in-place. The length of the array will not exceed 10^4. For example, given `nums = [0,1,0,3,12]`, the function should return `[1,3,12,0,0]`. The function should not return anything (void), but modify the input array in-place.

## Approach
The algorithm uses two pointers, one for tracking non-zero elements and the other for iterating through the array. When a non-zero element is found, it is swapped with the element at the non-zero pointer index. This approach ensures that all non-zero elements are moved to the front of the array while maintaining their relative order.

## Complexity
- Time: O(n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

void moveZeroes(vector<int>& nums) {
    int nonZeroIndex = 0; // pointer for non-zero elements
    for (int i = 0; i < nums.size(); i++) {
        if (nums[i] != 0) { // if current element is not zero
            swap(nums[nonZeroIndex], nums[i]); // swap with non-zero pointer index
            nonZeroIndex++; // increment non-zero pointer
        }
    }
}
```

## Test Cases
```
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Input: nums = [4,2,4,0,0,3,0,5,1,0]
Output: [4,2,4,3,5,1,0,0,0,0]
```

## Key Takeaways
- Use two pointers to track non-zero elements and iterate through the array.
- Swap non-zero elements with the element at the non-zero pointer index to maintain relative order.
- The algorithm has a linear time complexity and constant space complexity, making it efficient for large inputs.