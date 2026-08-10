# Sort Colors (Dutch Flag)

## Problem Statement
Given an array of integers containing only 0s, 1s, and 2s, sort the array in a single pass such that all 0s are first, followed by all 1s, and then all 2s. This is also known as the Dutch Flag problem. The array can contain any number of 0s, 1s, and 2s. For example, if the input is [2, 0, 2, 1, 1, 0], the output should be [0, 0, 1, 1, 2, 2]. The solution should be efficient in terms of time and space complexity.

## Approach
The algorithm uses three pointers to track the positions of 0s and 2s in the array. It iterates through the array, swapping elements as necessary to maintain the correct order. The intuition is to consider the array as having three sections: one for 0s, one for 1s, and one for 2s.

## Complexity
- Time: O(n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

void sortColors(vector<int>& nums) {
    int low = 0; // Pointer for 0s
    int high = nums.size() - 1; // Pointer for 2s
    int mid = 0; // Pointer for current element

    while (mid <= high) {
        if (nums[mid] == 0) {
            swap(nums[low], nums[mid]);
            low++;
            mid++;
        } else if (nums[mid] == 1) {
            mid++;
        } else {
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
- The Dutch Flag problem can be solved in a single pass using three pointers.
- The time complexity is O(n), where n is the number of elements in the array.
- The space complexity is O(1), as no extra space is used.