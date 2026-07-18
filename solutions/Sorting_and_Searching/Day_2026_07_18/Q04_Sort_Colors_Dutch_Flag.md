# Sort Colors (Dutch Flag)

## Problem Statement
Given an array with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue. We will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively. The solution should have a time complexity of O(n) and a space complexity of O(1). For example, given the array [2,0,2,1,1,0], the function should return [0,0,1,1,2,2].

## Approach
The Dutch National Flag algorithm is used to solve this problem. The idea is to maintain three pointers: low, mid, and high. The low pointer is used to track the position of the next 0, the mid pointer is used to scan the array, and the high pointer is used to track the position of the next 2. When the mid pointer encounters a 0, it swaps the value at the mid pointer with the value at the low pointer and moves both the low and mid pointers forward. When the mid pointer encounters a 2, it swaps the value at the mid pointer with the value at the high pointer and moves the high pointer backward.

## Complexity
- Time: O(n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

void sortColors(vector<int>& nums) {
    // Initialize the low and high pointers
    int low = 0;
    int high = nums.size() - 1;
    int mid = 0;

    // Loop through the array until the mid pointer meets the high pointer
    while (mid <= high) {
        // If the mid pointer encounters a 0, swap it with the value at the low pointer
        if (nums[mid] == 0) {
            swap(nums[low], nums[mid]);
            low++;
            mid++;
        }
        // If the mid pointer encounters a 1, just move the mid pointer forward
        else if (nums[mid] == 1) {
            mid++;
        }
        // If the mid pointer encounters a 2, swap it with the value at the high pointer
        else {
            swap(nums[mid], nums[high]);
            high--;
        }
    }
}

int main() {
    vector<int> nums = {2,0,2,1,1,0};
    sortColors(nums);
    for (int num : nums) {
        cout << num << " ";
    }
    return 0;
}
```

## Test Cases
```
Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Input: [2,2,0,1,2,0]
Output: [0,0,1,2,2,2]
```

## Key Takeaways
- The Dutch National Flag algorithm is an efficient solution for sorting an array of 0s, 1s, and 2s in-place.
- The algorithm uses three pointers: low, mid, and high, to track the positions of the next 0, the current element, and the next 2 respectively.
- The algorithm has a time complexity of O(n) and a space complexity of O(1), making it suitable for large datasets.