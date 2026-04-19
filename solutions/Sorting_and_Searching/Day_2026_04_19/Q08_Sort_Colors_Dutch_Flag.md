# Sort Colors (Dutch Flag)

## Problem Statement
Given an array of integers containing only 0s, 1s, and 2s, sort the array in a single pass such that all 0s come first, followed by all 1s, and then all 2s. This problem is also known as the Dutch Flag problem. The array should be sorted in-place.

## Approach
We will use three pointers to solve this problem: low, mid, and high. The low pointer will track the position where the next 0 should be placed, the mid pointer will iterate through the array, and the high pointer will track the position where the next 2 should be placed.

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
```

## Key Takeaways
- We use three pointers to solve this problem efficiently.
- The low and mid pointers start from the beginning of the array, and the high pointer starts from the end.
- The algorithm only requires a single pass through the array, resulting in a time complexity of O(n).