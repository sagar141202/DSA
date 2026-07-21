# Move Zeroes

## Problem Statement
Given an array of integers, move all the zeroes to the end of the array while maintaining the relative order of the non-zero elements. The array is 0-indexed and can contain duplicate elements. For example, if the input array is `[0, 1, 0, 3, 12]`, the output should be `[1, 3, 12, 0, 0]`. The function should modify the input array in-place and return the modified array.

## Approach
The approach is to use two pointers, one for tracking non-zero elements and another for iterating through the array. We swap the non-zero elements with the elements at the tracking pointer's position. This ensures that all non-zero elements are moved to the front of the array while maintaining their relative order.

## Complexity
- Time: O(n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

void moveZeroes(vector<int>& nums) {
    // Initialize two pointers
    int slow = 0; // tracks the position of the next non-zero element
    int fast = 0; // iterates through the array
    
    // Iterate through the array
    while (fast < nums.size()) {
        // If the current element is non-zero, swap it with the element at the slow pointer's position
        if (nums[fast] != 0) {
            swap(nums[slow], nums[fast]);
            // Move the slow pointer forward
            slow++;
        }
        // Move the fast pointer forward
        fast++;
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
- Use two pointers to track the position of the next non-zero element and iterate through the array.
- Swap non-zero elements with the elements at the tracking pointer's position to maintain relative order.
- The solution has a time complexity of O(n) and a space complexity of O(1), making it efficient for large inputs.