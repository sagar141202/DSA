# Rotate Array

## Problem Statement
Given an array of integers `nums` and an integer `k`, rotate the array to the right by `k` steps. The rotation should be performed in-place, meaning that the original array should be modified. The length of the array is denoted by `n`. If `k` is greater than `n`, the rotation should be equivalent to `k % n` steps. For example, if `nums = [1, 2, 3, 4, 5, 6, 7]` and `k = 3`, the rotated array should be `[5, 6, 7, 1, 2, 3, 4]`.

## Approach
The algorithm uses a temporary array to store the rotated elements, then copies them back to the original array. Alternatively, a more efficient approach uses three reversals to rotate the array in-place. The first reversal reverses the entire array, the second reversal reverses the first `k` elements, and the third reversal reverses the remaining elements.

## Complexity
- Time: O(n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

void reverse(vector<int>& nums, int start, int end) {
    while (start < end) {
        swap(nums[start], nums[end]);
        start++;
        end--;
    }
}

void rotate(vector<int>& nums, int k) {
    k = k % nums.size();
    reverse(nums, 0, nums.size() - 1);
    reverse(nums, 0, k - 1);
    reverse(nums, k, nums.size() - 1);
}

int main() {
    vector<int> nums = {1, 2, 3, 4, 5, 6, 7};
    int k = 3;
    rotate(nums, k);
    for (int num : nums) {
        cout << num << " ";
    }
    return 0;
}
```

## Test Cases
```
Input: nums = [1, 2, 3, 4, 5, 6, 7], k = 3
Output: [5, 6, 7, 1, 2, 3, 4]
Input: nums = [1, 2, 3, 4, 5, 6, 7], k = 7
Output: [1, 2, 3, 4, 5, 6, 7]
Input: nums = [1, 2], k = 3
Output: [2, 1]
```

## Key Takeaways
- The rotation can be performed in-place using three reversals.
- The `k % n` operation is used to handle cases where `k` is greater than the length of the array.
- The time complexity is O(n) because each element is visited at most twice during the reversals.