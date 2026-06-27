# Rotate Array

## Problem Statement
Given an array of integers `nums` and an integer `k`, rotate the array to the right by `k` steps. The rotation should be done in-place, meaning that the array should be modified directly without creating a new array. For example, if `nums = [1, 2, 3, 4, 5, 6, 7]` and `k = 3`, the rotated array should be `[5, 6, 7, 1, 2, 3, 4]`. The length of the array is denoted by `n`, where `1 <= n <= 10^5`. The value of `k` can be greater than `n`, in which case the rotation is equivalent to `k % n` steps.

## Approach
The algorithm uses a three-step approach: reverse the entire array, reverse the first `k % n` elements, and reverse the rest of the array. This approach ensures that the array is rotated to the right by `k` steps in-place.

## Complexity
- Time: O(n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

void rotate(vector<int>& nums, int k) {
    // calculate the effective number of steps
    k = k % nums.size();
    
    // reverse the entire array
    reverse(nums.begin(), nums.end());
    
    // reverse the first k elements
    reverse(nums.begin(), nums.begin() + k);
    
    // reverse the rest of the array
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
Input: nums = [1, 2], k = 3
Output: [2, 1]
```

## Key Takeaways
- The rotation can be achieved by reversing the array three times.
- The effective number of steps is `k % n`, where `n` is the length of the array.
- The time complexity is O(n) because each element is visited at most three times.