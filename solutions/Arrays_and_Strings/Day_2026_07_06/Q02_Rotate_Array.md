# Rotate Array

## Problem Statement
Given an array of integers `nums` and an integer `k`, rotate the array to the right by `k` steps. The rotation should be performed in-place, meaning that the original array should be modified. The length of the array `nums` is `n`, and `k` can be greater than `n`. For example, if `nums = [1, 2, 3, 4, 5, 6, 7]` and `k = 3`, the rotated array should be `[5, 6, 7, 1, 2, 3, 4]`.

## Approach
We can solve this problem by using the reverse algorithm to reverse the entire array and then reverse the first `k` elements and the rest of the array. This approach ensures that the rotation is performed in-place and efficiently.

## Complexity
- Time: O(n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

void rotate(vector<int>& nums, int k) {
    // Calculate the effective rotation steps
    k = k % nums.size();
    
    // Reverse the entire array
    reverse(nums.begin(), nums.end());
    
    // Reverse the first k elements
    reverse(nums.begin(), nums.begin() + k);
    
    // Reverse the rest of the array
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
- The rotation can be performed in-place by reversing the array.
- The effective rotation steps can be calculated by taking the modulus of `k` with the length of the array.
- The reverse algorithm can be used to reverse the entire array and the sub-arrays.