# Sort Colors (Dutch Flag)

## Problem Statement
Given an array of integers containing only 0s, 1s, and 2s, sort the array in a single pass such that all 0s come first, followed by all 1s, and then all 2s. This problem is also known as the Dutch Flag problem. The array should be modified in-place, and the solution should have a time complexity of O(n) and a space complexity of O(1), where n is the number of elements in the array. For example, if the input array is [2, 0, 2, 1, 1, 0], the output array should be [0, 0, 1, 1, 2, 2].

## Approach
The algorithm uses three pointers: low, mid, and high. The low pointer is used to track the position of the next 0, the mid pointer is used to track the position of the next 1, and the high pointer is used to track the position of the next 2. The algorithm iterates through the array, swapping elements as necessary to maintain the correct order.

## Complexity
- Time: O(n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

void sortColors(vector<int>& nums) {
    int low = 0; // pointer for 0s
    int mid = 0; // pointer for 1s
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
- The Dutch Flag problem can be solved in a single pass with a time complexity of O(n) and a space complexity of O(1).
- The algorithm uses three pointers to track the positions of the next 0, 1, and 2 in the array.
- The solution modifies the input array in-place, making it efficient for large inputs.