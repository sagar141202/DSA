# Move Zeroes

## Problem Statement
Given an array of integers, move all the zeroes to the end of the array while maintaining the relative order of non-zero elements. The function should modify the input array in-place. The array can contain duplicate elements and can be empty. For example, if the input array is `[0, 1, 0, 3, 12]`, the function should modify it to `[1, 3, 12, 0, 0]`.

## Approach
The algorithm uses a two-pointer approach, iterating over the array and swapping non-zero elements with the next available position. This approach ensures that non-zero elements maintain their relative order. The function iterates over the array only once, making it efficient for large inputs.

## Complexity
- Time: O(n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

void moveZeroes(vector<int>& nums) {
    // Initialize two pointers, one for the next non-zero element and one for the current element
    int nonZeroIndex = 0;
    
    // Iterate over the array
    for (int i = 0; i < nums.size(); i++) {
        // If the current element is not zero, swap it with the next available non-zero position
        if (nums[i] != 0) {
            swap(nums[nonZeroIndex], nums[i]);
            // Move the non-zero index forward
            nonZeroIndex++;
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
- Use a two-pointer approach to iterate over the array and swap non-zero elements with the next available position.
- The function should modify the input array in-place to minimize space complexity.
- The algorithm has a time complexity of O(n) and a space complexity of O(1), making it efficient for large inputs.