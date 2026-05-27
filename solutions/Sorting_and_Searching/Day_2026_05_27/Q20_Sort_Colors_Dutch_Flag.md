# Sort Colors (Dutch Flag)

## Problem Statement
Given an array of integers containing only 0, 1, and 2, sort the array in-place such that all 0's are first, followed by all 1's and then all 2's. The array is also known as the Dutch Flag because it resembles the Dutch flag which has three horizontal stripes of red (0), white (1), and blue (2). The constraints are that we should only use a constant amount of additional space and the time complexity should be linear.

## Approach
The algorithm uses three pointers to track the positions of 0's, 1's, and 2's in the array. It iterates through the array, swapping elements as necessary to maintain the correct order. The intuition is to maintain a "window" of sorted elements and expand it as we iterate through the array.

## Complexity
- Time: O(n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

void sortColors(vector<int>& nums) {
    // Initialize three pointers
    int low = 0;  // Pointer for 0's
    int mid = 0;  // Pointer for 1's
    int high = nums.size() - 1;  // Pointer for 2's

    // Iterate through the array
    while (mid <= high) {
        // If current element is 0, swap it with the element at the low pointer
        if (nums[mid] == 0) {
            swap(nums[low], nums[mid]);
            low++;
            mid++;
        }
        // If current element is 1, just move to the next element
        else if (nums[mid] == 1) {
            mid++;
        }
        // If current element is 2, swap it with the element at the high pointer
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
```

## Key Takeaways
- We can solve this problem in linear time complexity by using three pointers to track the positions of 0's, 1's, and 2's in the array.
- We only need a constant amount of additional space to store the pointers, making the space complexity O(1).
- The algorithm can be easily extended to sort arrays with more than three distinct elements by using more pointers.