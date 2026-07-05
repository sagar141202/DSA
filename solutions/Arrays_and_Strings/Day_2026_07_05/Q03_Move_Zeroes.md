# Move Zeroes

## Problem Statement
Given an array of integers, move all the zeroes to the end of the array while maintaining the relative order of non-zero elements. The function should modify the input array in-place. The input array can contain duplicate elements and can be empty. For example, given the array `[0, 1, 0, 3, 12]`, the function should modify it to `[1, 3, 12, 0, 0]`.

## Approach
The algorithm uses two pointers to track the position of non-zero elements. It iterates through the array, swapping non-zero elements with the next available position. This approach ensures that all non-zero elements are moved to the front of the array, and the zeroes are moved to the end.

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
        // Initialize two pointers, one for tracking non-zero elements and one for iteration
        int nonZeroPtr = 0;
        
        // Iterate through the array
        for (int i = 0; i < nums.size(); i++) {
            // If the current element is not zero, swap it with the next available position
            if (nums[i] != 0) {
                swap(nums[nonZeroPtr], nums[i]);
                // Move the non-zero pointer forward
                nonZeroPtr++;
            }
        }
    }
};

int main() {
    Solution solution;
    vector<int> nums = {0, 1, 0, 3, 12};
    solution.moveZeroes(nums);
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
- Use two pointers to track the position of non-zero elements and iterate through the array.
- Swap non-zero elements with the next available position to maintain the relative order.
- The algorithm has a time complexity of O(n) and a space complexity of O(1), making it efficient for large inputs.