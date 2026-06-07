# Move Zeroes

## Problem Statement
Given an array of integers, move all the zeroes to the end of the array while maintaining the relative order of non-zero elements. The function should modify the input array in-place. The array can contain duplicate elements and can be empty. For example, if the input array is `[0, 1, 0, 3, 12]`, the function should modify it to `[1, 3, 12, 0, 0]`.

## Approach
The algorithm uses two pointers to track the position of non-zero elements and swap them with the next zero element. It iterates through the array, moving non-zero elements to the front and maintaining their relative order. This approach ensures that all zeroes are moved to the end of the array.

## Complexity
- Time: O(n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

void moveZeroes(vector<int>& nums) {
    // initialize two pointers
    int left = 0;  // tracks the position of non-zero elements
    int right = 0;  // iterates through the array
    
    // iterate through the array
    while (right < nums.size()) {
        // if the current element is not zero, swap it with the left pointer
        if (nums[right] != 0) {
            swap(nums[left], nums[right]);
            // move the left pointer forward
            left++;
        }
        // move the right pointer forward
        right++;
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
- Use two pointers to track the position of non-zero elements and iterate through the array.
- Swap non-zero elements with the next zero element to maintain their relative order.
- The algorithm has a time complexity of O(n) and a space complexity of O(1), making it efficient for large inputs.