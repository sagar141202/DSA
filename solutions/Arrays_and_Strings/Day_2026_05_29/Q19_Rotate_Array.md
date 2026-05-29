# Rotate Array

## Problem Statement
Given an array of integers `nums` and an integer `k`, rotate the array to the right by `k` steps. The rotation should be performed in-place, meaning that the original array should be modified to reflect the rotation. For example, given `nums = [1, 2, 3, 4, 5, 6, 7]` and `k = 3`, the rotated array should be `[5, 6, 7, 1, 2, 3, 4]`. The constraints are `1 <= nums.length <= 10^5` and `0 <= k < 10^5`.

## Approach
The algorithm uses a three-step reversal approach to rotate the array in-place, first reversing the entire array, then reversing the first `k` elements, and finally reversing the remaining elements. This approach ensures that the array is rotated to the right by `k` steps.

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
        
        // reverse the remaining elements
        reverse(nums.begin() + k, nums.end());
    }
};

int main() {
    Solution solution;
    vector<int> nums = {1, 2, 3, 4, 5, 6, 7};
    int k = 3;
    solution.rotate(nums, k);
    
    // print the rotated array
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
```

## Key Takeaways
- The three-step reversal approach is an efficient way to rotate an array in-place.
- The effective rotation steps are calculated by taking the modulus of `k` with the length of the array, which handles cases where `k` is greater than the length of the array.
- The `reverse` function is used to reverse the elements of the array, which is a built-in function in C++.