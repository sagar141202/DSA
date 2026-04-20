# Sort Colors (Dutch Flag)

## Problem Statement
Given an array of integers containing only 0s, 1s, and 2s, sort the array in a single pass. The solution should be efficient and scalable. The array is not sorted and can contain duplicate values. The goal is to sort the array such that all 0s are on the left, all 1s are in the middle, and all 2s are on the right. For example, if the input array is [2, 0, 2, 1, 1, 0], the output should be [0, 0, 1, 1, 2, 2].

## Approach
We will use the Dutch National Flag algorithm, a variation of the QuickSort algorithm that is suitable for this problem. The algorithm uses three pointers: low, mid, and high. The low pointer is used to track the position of the next 0, the mid pointer is used to scan the array, and the high pointer is used to track the position of the next 2.

## Complexity
- Time: O(n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

void sortColors(vector<int>& nums) {
    int low = 0; // pointer for 0s
    int mid = 0; // pointer for 1s
    int high = nums.size() - 1; // pointer for 2s

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
Input: [0, 1, 2, 0, 1, 2]
Output: [0, 0, 1, 1, 2, 2]
Input: [2, 2, 0, 1, 2, 0]
Output: [0, 0, 1, 2, 2, 2]
```

## Key Takeaways
- The Dutch National Flag algorithm is an efficient solution for sorting an array with only three distinct values.
- The algorithm uses three pointers to track the positions of the three values, allowing for a single pass through the array.
- The solution has a time complexity of O(n) and a space complexity of O(1), making it efficient and scalable.