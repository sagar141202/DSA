# Rotate Array

## Problem Statement
Given an array of integers `nums` and an integer `k`, rotate the array to the right by `k` steps. The rotation should be performed in-place, meaning that the original array should be modified. The length of the array is denoted by `n`. For example, given `nums = [1, 2, 3, 4, 5, 6, 7]` and `k = 3`, the rotated array should be `[5, 6, 7, 1, 2, 3, 4]`. The value of `k` can be larger than `n`, and in such cases, the rotation should be performed by `k % n` steps.

## Approach
To rotate the array, we can use a temporary array to store the rotated elements. We can also use a reverse approach, where we reverse the entire array and then reverse the first `k` elements and the rest of the array. This approach takes advantage of the fact that reversing an array is an in-place operation.

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
        // calculate the effective number of steps to rotate
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
- The rotation can be performed in-place by reversing the array.
- The number of steps to rotate can be reduced by taking the modulus of `k` with the length of the array.
- The reverse approach can be used to avoid using extra space.