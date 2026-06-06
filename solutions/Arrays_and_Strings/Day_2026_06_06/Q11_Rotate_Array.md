# Rotate Array

## Problem Statement
Given an array of integers `nums` and an integer `k`, rotate the array to the right by `k` steps. The rotation should be performed in-place, meaning that the original array should be modified. The length of the array `nums` is denoted by `n`. For example, if `nums = [1, 2, 3, 4, 5, 6, 7]` and `k = 3`, the rotated array should be `[5, 6, 7, 1, 2, 3, 4]`. The constraint is that `1 <= n <= 10^5` and `k` can be any integer.

## Approach
The algorithm uses the concept of reversing the array to achieve rotation in-place. It first reverses the entire array, then reverses the first `k` elements, and finally reverses the remaining elements. This results in the desired rotation.

## Complexity
- Time: O(n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

void rotate(vector<int>& nums, int k) {
    // calculate effective rotation steps
    k = k % nums.size();
    
    // reverse the entire array
    reverse(nums.begin(), nums.end());
    
    // reverse the first k elements
    reverse(nums.begin(), nums.begin() + k);
    
    // reverse the remaining elements
    reverse(nums.begin() + k, nums.end());
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
```

## Key Takeaways
- The rotation can be achieved by reversing the array in three steps.
- The effective rotation steps are calculated as `k % n` to handle cases where `k` is greater than `n`.
- The algorithm has a time complexity of O(n) and a space complexity of O(1), making it efficient for large inputs.