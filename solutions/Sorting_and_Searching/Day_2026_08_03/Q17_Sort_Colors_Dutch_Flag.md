# Sort Colors (Dutch Flag)

## Problem Statement
Given an array of integers containing only 0s, 1s, and 2s, sort the array in-place such that all 0s come first, followed by all 1s, and then all 2s. The array will contain at least one 0, one 1, and one 2. The function should not return anything, but modify the input array in-place. For example, given the array [2,0,2,1,1,0], the function should modify it to [0,0,1,1,2,2]. The array can be of any size, and the function should have a time complexity of O(n), where n is the size of the array.

## Approach
The algorithm uses three pointers to track the positions of 0s, 1s, and 2s in the array. The low pointer is used to track the position of the next 0, the mid pointer is used to track the current element being processed, and the high pointer is used to track the position of the next 2. The algorithm iterates through the array, swapping elements as necessary to maintain the correct order.

## Complexity
- Time: O(n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

void sortColors(vector<int>& nums) {
    // Initialize low and high pointers
    int low = 0;
    int high = nums.size() - 1;
    int mid = 0;

    // Iterate through the array until mid pointer crosses high pointer
    while (mid <= high) {
        // If current element is 0, swap it with the element at low pointer and move both low and mid pointers forward
        if (nums[mid] == 0) {
            swap(nums[low], nums[mid]);
            low++;
            mid++;
        }
        // If current element is 1, just move mid pointer forward
        else if (nums[mid] == 1) {
            mid++;
        }
        // If current element is 2, swap it with the element at high pointer and move high pointer backward
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
Input: [2,0,1]
Output: [0,1,2]
Input: [0,1,2,0,1,2]
Output: [0,0,1,1,2,2]
```

## Key Takeaways
- The Dutch National Flag algorithm can be used to sort an array of 0s, 1s, and 2s in a single pass.
- The algorithm uses three pointers to track the positions of 0s, 1s, and 2s in the array.
- The algorithm has a time complexity of O(n) and a space complexity of O(1), making it efficient for large inputs.