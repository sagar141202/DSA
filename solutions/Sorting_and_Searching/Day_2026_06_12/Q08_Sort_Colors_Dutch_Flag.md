# Sort Colors (Dutch Flag)

## Problem Statement
Given an array of integers containing only 0s, 1s, and 2s, sort the array in a single pass such that all 0s are first, followed by all 1s, and then all 2s. This is also known as the Dutch National Flag problem. The array should be sorted in-place, meaning no additional space should be used. For example, if the input array is [2, 0, 2, 1, 1, 0], the output array should be [0, 0, 1, 1, 2, 2]. The input array will contain only 0s, 1s, and 2s, and will have a length of at least 1.

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

    // iterate through the array
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
- The Dutch National Flag problem can be solved in a single pass using three pointers.
- The algorithm has a time complexity of O(n) and a space complexity of O(1), making it efficient for large inputs.
- The algorithm can be applied to other problems that require partitioning an array into three parts based on certain conditions.