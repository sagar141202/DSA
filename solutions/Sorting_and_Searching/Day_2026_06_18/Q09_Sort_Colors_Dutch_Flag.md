# Sort Colors (Dutch Flag)

## Problem Statement
Given an array of integers where each integer represents a color (0 for red, 1 for white, and 2 for blue), sort the array such that all 0s come first, followed by all 1s, and then all 2s. The array must be sorted in-place, meaning no additional space can be used. For example, if the input array is [2, 0, 2, 1, 1, 0], the output should be [0, 0, 1, 1, 2, 2]. The input array can contain only 0s, 1s, and 2s.

## Approach
The algorithm uses three pointers (low, mid, high) to divide the array into four parts: elements less than 0, equal to 0, equal to 1, and greater than 1. The low pointer is used to track the position of the next 0, the mid pointer is used to track the position of the next 1, and the high pointer is used to track the position of the next 2.

## Complexity
- Time: O(n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

void sortColors(vector<int>& nums) {
    int low = 0, mid = 0, high = nums.size() - 1;
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
Input: [2, 2, 0, 1, 2, 0]
Output: [0, 0, 1, 2, 2, 2]
```

## Key Takeaways
- The Dutch National Flag problem can be solved using a three-pointer approach.
- The algorithm has a time complexity of O(n) and a space complexity of O(1), making it efficient for large inputs.
- The algorithm can be used to sort arrays with three distinct elements, and can be modified to sort arrays with more than three distinct elements.