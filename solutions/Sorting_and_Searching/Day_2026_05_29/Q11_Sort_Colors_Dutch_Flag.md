# Sort Colors (Dutch Flag)

## Problem Statement
Given an array of integers containing only 0s, 1s, and 2s, sort the array in a single pass such that all 0s are first, followed by all 1s, and then all 2s. The array should be modified in-place, and no additional space should be used except for a few variables. The input array may contain duplicate elements. For example, given the array [2, 0, 2, 1, 1, 0], the output should be [0, 0, 1, 1, 2, 2].

## Approach
We use three pointers, low, mid, and high, to keep track of the positions where the next 0, 1, and 2 should be placed. The algorithm iterates through the array, swapping elements as necessary to maintain the correct order. This approach ensures that the array is sorted in a single pass.

## Complexity
- Time: O(n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

void sortColors(vector<int>& nums) {
    int low = 0;  // Pointer for 0s
    int mid = 0;  // Pointer for 1s
    int high = nums.size() - 1;  // Pointer for 2s

    // Iterate through the array until mid crosses high
    while (mid <= high) {
        // If the current element is 0, swap it with the element at low and increment both low and mid
        if (nums[mid] == 0) {
            swap(nums[low], nums[mid]);
            low++;
            mid++;
        }
        // If the current element is 1, just increment mid
        else if (nums[mid] == 1) {
            mid++;
        }
        // If the current element is 2, swap it with the element at high and decrement high
        else {
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
Input: [0, 1, 2, 0, 1, 2]
Output: [0, 0, 1, 1, 2, 2]
Input: [2, 2, 0, 1, 2, 0]
Output: [0, 0, 1, 2, 2, 2]
```

## Key Takeaways
- The three-pointer technique is useful for sorting arrays with a limited number of distinct elements.
- In-place sorting can be achieved by using a few extra variables to keep track of the positions where elements should be placed.
- The algorithm should be designed to handle duplicate elements and edge cases.