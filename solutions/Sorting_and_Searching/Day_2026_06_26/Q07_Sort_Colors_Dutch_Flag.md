# Sort Colors (Dutch Flag)

## Problem Statement
Given an array of integers containing only 0, 1, and 2, sort the array in-place such that all 0s are first, followed by all 1s, and then all 2s. The array is often referred to as the Dutch Flag problem because it resembles the Dutch flag, which has three horizontal bands of red (2), white (1), and blue (0). The problem should be solved with a time complexity of O(n) and a space complexity of O(1), where n is the number of elements in the array. For example, given the array [2, 0, 2, 1, 1, 0], the output should be [0, 0, 1, 1, 2, 2].

## Approach
The algorithm uses three pointers to track the positions of the next 0, the next 1, and the next 2 in the array. The intuition is to iterate through the array, swapping elements to maintain the correct order of 0s, 1s, and 2s. This approach ensures a single pass through the array, achieving the required time complexity.

## Complexity
- Time: O(n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

void sortColors(vector<int>& nums) {
    // Initialize three pointers
    int low = 0;  // Pointer for the next 0
    int mid = 0;  // Pointer for the next 1
    int high = nums.size() - 1;  // Pointer for the next 2

    // Iterate through the array until mid pointer crosses high pointer
    while (mid <= high) {
        // If current element is 0, swap it with the element at the low pointer and move both low and mid pointers forward
        if (nums[mid] == 0) {
            swap(nums[low], nums[mid]);
            low++;
            mid++;
        }
        // If current element is 1, just move the mid pointer forward
        else if (nums[mid] == 1) {
            mid++;
        }
        // If current element is 2, swap it with the element at the high pointer and move the high pointer backward
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
Input: [2, 2, 0, 1, 2, 0]
Output: [0, 0, 1, 2, 2, 2]
```

## Key Takeaways
- The Dutch Flag problem can be solved in a single pass through the array with three pointers.
- The algorithm maintains a time complexity of O(n) and a space complexity of O(1), making it efficient for large inputs.
- The use of three pointers allows for the separation of 0s, 1s, and 2s in a single iteration, which is key to solving the problem efficiently.