# Move Zeroes

## Problem Statement
Given an array of integers, move all the zeroes to the end of the array while maintaining the relative order of the non-zero elements. The function should modify the input array in-place. The array can contain duplicate elements and can be empty. For example, given the array `[0, 1, 0, 3, 12]`, the function should modify it to `[1, 3, 12, 0, 0]`.

## Approach
The algorithm uses two pointers, one for tracking non-zero elements and the other for iterating through the array. When a non-zero element is found, it is swapped with the element at the tracking pointer's position, and the tracking pointer is moved forward.

## Complexity
- Time: O(n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

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

int main() {
    vector<int> nums = {0, 1, 0, 3, 12};
    moveZeroes(nums);
    for (int num : nums) {
        cout << num << " ";
    }
    return 0;
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
- We can solve this problem in O(n) time complexity by using two pointers.
- The space complexity is O(1) as we are modifying the input array in-place.
- This approach maintains the relative order of non-zero elements.