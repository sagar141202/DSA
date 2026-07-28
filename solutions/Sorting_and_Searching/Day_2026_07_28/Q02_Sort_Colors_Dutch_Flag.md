# Sort Colors (Dutch Flag)

## Problem Statement
Given an array of integers containing only 0s, 1s, and 2s, sort the array in a single pass such that all 0s are first, followed by all 1s, and then all 2s. The problem is also known as the Dutch Flag problem. The array is not allowed to be sorted using any built-in sorting functions or data structures like hash maps or sets. The input array will contain at least one element.

## Approach
The algorithm uses three pointers: low, mid, and high. The low pointer is used to track the position where the next 0 should be placed, the mid pointer is used to scan the array, and the high pointer is used to track the position where the next 2 should be placed. The algorithm iterates through the array, swapping elements as necessary to maintain the correct order.

## Complexity
- Time: O(n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

void sortColors(vector<int>& nums) {
    int low = 0; // pointer for 0s
    int high = nums.size() - 1; // pointer for 2s
    int mid = 0; // pointer for scanning the array
    
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
```

## Key Takeaways
- The three-pointer technique can be used to solve problems that require partitioning an array into multiple sections.
- The Dutch Flag problem can be solved in a single pass through the array, resulting in a time complexity of O(n).
- The algorithm uses a constant amount of space, resulting in a space complexity of O(1).