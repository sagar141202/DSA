# Sort Colors (Dutch Flag)

## Problem Statement
Given an array of integers containing only 0s, 1s, and 2s, sort the array in a single pass such that all 0s come first, followed by all 1s, and then all 2s. This problem is also known as the Dutch Flag problem. The array should be sorted in-place, meaning no extra space should be used.

## Approach
The algorithm uses three pointers, one for each color, to partition the array. The intuition is to maintain the relative order of the colors by swapping elements when necessary. The algorithm iterates through the array, swapping elements to maintain the correct order.

## Complexity
- Time: O(n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

void sortColors(vector<int>& nums) {
    // Initialize pointers for 0s and 2s
    int low = 0;
    int high = nums.size() - 1;
    int mid = 0;

    // Iterate through the array
    while (mid <= high) {
        // If current element is 0, swap with low and increment both low and mid
        if (nums[mid] == 0) {
            swap(nums[low], nums[mid]);
            low++;
            mid++;
        }
        // If current element is 1, just increment mid
        else if (nums[mid] == 1) {
            mid++;
        }
        // If current element is 2, swap with high and decrement high
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
```

## Key Takeaways
- Use three pointers to partition the array and maintain the relative order of the colors.
- The algorithm should iterate through the array only once, resulting in a time complexity of O(n).
- The space complexity is O(1), as no extra space is used.