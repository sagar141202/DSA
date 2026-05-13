# Sort Colors (Dutch Flag)

## Problem Statement
Given an array of integers containing only 0s, 1s, and 2s, sort the array in a single pass such that all 0s come first, followed by all 1s, and then all 2s. The array will contain at least one element and a maximum of 10000 elements. Example: input = [2,0,2,1,1,0], output = [0,0,1,1,2,2].

## Approach
We can use the Dutch National Flag algorithm to solve this problem in a single pass. The algorithm uses three pointers to track the positions of 0s, 1s, and 2s. We iterate through the array and swap elements to maintain the order of 0s, 1s, and 2s.

## Complexity
- Time: O(n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

void sortColors(vector<int>& nums) {
    // Initialize pointers
    int low = 0;  // Pointer for 0s
    int high = nums.size() - 1;  // Pointer for 2s
    int mid = 0;  // Pointer for 1s

    // Iterate through the array
    while (mid <= high) {
        // If the current element is 0, swap it with the element at the low pointer
        if (nums[mid] == 0) {
            swap(nums[low], nums[mid]);
            low++;
            mid++;
        }
        // If the current element is 2, swap it with the element at the high pointer
        else if (nums[mid] == 2) {
            swap(nums[mid], nums[high]);
            high--;
        }
        // If the current element is 1, move to the next element
        else {
            mid++;
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
Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Input: [0,0,0,1,1,1,2,2,2]
Output: [0,0,0,1,1,1,2,2,2]
Input: [2,2,2,1,1,1,0,0,0]
Output: [0,0,0,1,1,1,2,2,2]
```

## Key Takeaways
- The Dutch National Flag algorithm is used for sorting arrays containing only three distinct elements.
- The algorithm uses three pointers to track the positions of the three elements.
- The algorithm has a time complexity of O(n) and a space complexity of O(1), making it efficient for large inputs.