# Sort Colors (Dutch Flag)

## Problem Statement
Given an array of integers containing only 0s, 1s, and 2s, sort the array in a single pass such that all 0s are first, followed by all 1s, and then all 2s. The problem is also known as the Dutch Flag problem. The array will contain at least one element, and the maximum size of the array is not fixed. The goal is to achieve this in linear time complexity.

## Approach
The algorithm uses three pointers: low, mid, and high. The low pointer is used to track the position where the next 0 should be placed, the mid pointer is used to traverse the array, and the high pointer is used to track the position where the next 2 should be placed. The algorithm iterates through the array, swapping elements as necessary to maintain the correct order of 0s, 1s, and 2s.

## Complexity
- Time: O(n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

void sortColors(vector<int>& nums) {
    int low = 0;  // pointer for 0s
    int high = nums.size() - 1;  // pointer for 2s
    int mid = 0;  // pointer for traversal

    while (mid <= high) {
        if (nums[mid] == 0) {
            // swap nums[low] and nums[mid]
            swap(nums[low], nums[mid]);
            low++;
            mid++;
        } else if (nums[mid] == 1) {
            mid++;
        } else {
            // swap nums[mid] and nums[high]
            swap(nums[mid], nums[high]);
            high--;
        }
    }
}

int main() {
    vector<int> nums = {2, 0, 2, 1, 1, 0};
    sortColors(nums);
    for (int num : nums) {
        cout << num << " ";
    }
    return 0;
}
```

## Test Cases
```
Input: [2, 0, 2, 1, 1, 0]
Output: [0, 0, 1, 1, 2, 2]
Input: [2, 2, 0, 1, 2, 0]
Output: [0, 0, 1, 2, 2, 2]
```

## Key Takeaways
- The algorithm uses a single pass through the array, resulting in linear time complexity.
- The use of three pointers (low, mid, and high) allows for efficient tracking of the positions where 0s, 1s, and 2s should be placed.
- The algorithm only uses a constant amount of extra space, making it space-efficient.