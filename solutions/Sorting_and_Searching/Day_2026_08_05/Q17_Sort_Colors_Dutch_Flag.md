# Sort Colors (Dutch Flag)

## Problem Statement
Given an array of integers containing only 0s, 1s, and 2s, sort the array in a single pass such that all 0s are first, followed by all 1s, and then all 2s. This is also known as the Dutch Flag problem. The array should be sorted in-place, meaning no extra space should be used. For example, given the array [2, 0, 2, 1, 1, 0], the output should be [0, 0, 1, 1, 2, 2]. The input array can contain any number of 0s, 1s, and 2s.

## Approach
The algorithm uses three pointers: low, mid, and high. The low pointer is used to track the position where the next 0 should be placed, the mid pointer is used to scan the array, and the high pointer is used to track the position where the next 2 should be placed. The mid pointer scans the array and swaps elements based on their values.

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
    int mid = 0; // pointer to scan the array

    while (mid <= high) {
        // if current element is 0, swap with low and increment both low and mid
        if (nums[mid] == 0) {
            swap(nums[low], nums[mid]);
            low++;
            mid++;
        }
        // if current element is 1, just increment mid
        else if (nums[mid] == 1) {
            mid++;
        }
        // if current element is 2, swap with high and decrement high
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
Input: [2, 2, 0, 1, 2, 0]
Output: [0, 0, 1, 2, 2, 2]
```

## Key Takeaways
- The Dutch Flag problem can be solved in a single pass using three pointers.
- The algorithm has a time complexity of O(n) and a space complexity of O(1), making it efficient for large inputs.
- The solution can be extended to sort arrays containing more than three distinct elements by using a similar approach with additional pointers.