# Rotate Array

## Problem Statement
Given an array of integers `nums` and an integer `k`, rotate the array to the right by `k` steps. The rotation should be performed in-place, meaning that the original array should be modified to reflect the rotation. The array can contain duplicate elements and can be rotated by more than its length. For example, if `nums = [1, 2, 3, 4, 5, 6, 7]` and `k = 3`, the rotated array should be `[5, 6, 7, 1, 2, 3, 4]`. The constraints are `1 <= nums.length <= 10^5` and `0 <= k <= 10^5`.

## Approach
We can use a temporary array to store the rotated elements, or we can use a three-step reversal approach to rotate the array in-place. The three-step reversal approach involves reversing the entire array, then reversing the first `k` elements, and finally reversing the rest of the array.

## Complexity
- Time: O(n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        // calculate the effective rotation steps
        k = k % nums.size();
        
        // reverse the entire array
        reverse(nums.begin(), nums.end());
        
        // reverse the first k elements
        reverse(nums.begin(), nums.begin() + k);
        
        // reverse the rest of the array
        reverse(nums.begin() + k, nums.end());
    }
};

int main() {
    Solution solution;
    vector<int> nums = {1, 2, 3, 4, 5, 6, 7};
    int k = 3;
    solution.rotate(nums, k);
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
- The rotation can be performed in-place using a three-step reversal approach.
- The effective rotation steps can be calculated by taking the modulus of `k` with the length of the array.
- The `reverse` function can be used to reverse the elements of a vector in C++.