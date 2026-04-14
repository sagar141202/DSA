# Sort Colors (Dutch Flag)

## Problem Statement
Given an array of integers containing only 0s, 1s, and 2s, sort the array in a single pass such that all 0s come before 1s and all 1s come before 2s. This is also known as the Dutch Flag problem. The array should be sorted in-place, meaning no extra space should be used. For example, if the input array is [2, 0, 2, 1, 1, 0], the output should be [0, 0, 1, 1, 2, 2]. The input array can contain any number of 0s, 1s, and 2s.

## Approach
The algorithm uses three pointers: low, mid, and high. The low pointer is used to track the position of the next 0, the mid pointer is used to track the current element being processed, and the high pointer is used to track the position of the next 2. The algorithm iterates through the array, swapping elements as necessary to maintain the correct order.

## Complexity
- Time: O(n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

void sortColors(vector<int>& nums) {
    int low = 0; // pointer for 0s
    int mid = 0; // pointer for current element
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
```

## Key Takeaways
- The Dutch Flag problem can be solved in a single pass using three pointers.
- The algorithm has a time complexity of O(n) and a space complexity of O(1), making it efficient for large inputs.
- The solution uses in-place swapping to maintain the correct order of elements.