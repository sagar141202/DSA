# Rotate Array

## Problem Statement
Given an array of integers `nums` and an integer `k`, rotate the array to the right by `k` steps. The rotation should be performed in-place, meaning that the original array should be modified. The array can contain duplicate elements and the length of the array is represented by `n`. The value of `k` can be greater than `n`, in which case the effective number of rotations is `k % n`. For example, if `nums = [1, 2, 3, 4, 5, 6, 7]` and `k = 3`, the rotated array should be `[5, 6, 7, 1, 2, 3, 4]`.

## Approach
The algorithm uses a three-step reversal approach to rotate the array in-place. First, reverse the entire array, then reverse the first `k % n` elements, and finally reverse the rest of the array. This approach ensures that the array is rotated to the right by `k` steps.

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
        // Calculate the effective number of rotations
        k = k % nums.size();
        
        // Reverse the entire array
        reverse(nums.begin(), nums.end());
        
        // Reverse the first k elements
        reverse(nums.begin(), nums.begin() + k);
        
        // Reverse the rest of the array
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
Input: nums = [1, 2, 3, 4, 5, 6, 7], k = 10
Output: [5, 6, 7, 1, 2, 3, 4]
```

## Key Takeaways
- The three-step reversal approach allows for efficient in-place rotation of the array.
- The effective number of rotations is `k % n`, where `n` is the length of the array.
- The algorithm has a time complexity of O(n) and a space complexity of O(1), making it suitable for large arrays.