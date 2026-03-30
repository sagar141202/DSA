# Move Zeroes

## Problem Statement
Given an array of integers, move all the zeroes to the end of the array while maintaining the relative order of non-zero elements. The function should modify the input array in-place. The array can contain duplicate elements and can be empty. For example, if the input array is `[0, 1, 0, 3, 12]`, the function should modify it to `[1, 3, 12, 0, 0]`.

## Approach
We will use a two-pointer technique to track the position of non-zero elements. One pointer will iterate through the array, and the other pointer will keep track of the position where the next non-zero element should be placed. This approach ensures that the relative order of non-zero elements is maintained.

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
    
    // Traverse through the array
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
- Use a two-pointer technique to track the position of non-zero elements.
- Modify the input array in-place to avoid extra space complexity.
- The relative order of non-zero elements is maintained by swapping non-zero elements with the element at the nonZeroPtr.