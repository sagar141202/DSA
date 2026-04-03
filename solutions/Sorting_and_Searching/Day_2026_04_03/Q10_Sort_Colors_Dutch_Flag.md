# Sort Colors (Dutch Flag)

## Problem Statement
Given an array of integers containing only 0, 1, and 2, sort the array in-place such that all 0s are first, followed by all 1s, and then all 2s. The array will contain only these three numbers, and the goal is to achieve this sorting with a single pass through the array. For example, if the input array is [2, 0, 2, 1, 1, 0], the output should be [0, 0, 1, 1, 2, 2]. The array can be of any size, and the input will always contain only 0, 1, and 2.

## Approach
The algorithm uses three pointers: one for the next 0, one for the next 1, and one for the next 2. It iterates through the array, swapping elements as necessary to keep the 0s and 1s in the correct order. This approach allows for a single pass through the array, ensuring an efficient solution.

## Complexity
- Time: O(n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

void sortColors(vector<int>& nums) {
    // Initialize pointers for 0 and 2
    int low = 0;
    int high = nums.size() - 1;
    int mid = 0;

    // Continue until mid pointer crosses high pointer
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
- The Dutch National Flag problem is a variation of the quicksort partitioning scheme.
- It's essential to understand how to use three pointers to keep track of the positions where the next 0, 1, and 2 should be placed.
- This algorithm can be extended to sort more than three distinct elements by using more pointers.