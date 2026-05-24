# Rotate Array

## Problem Statement
Given an array of integers `nums` and an integer `k`, rotate the array to the right by `k` steps. The array can be rotated in-place, and `k` can be larger than the length of the array. For example, if `nums = [1, 2, 3, 4, 5, 6, 7]` and `k = 3`, the rotated array will be `[5, 6, 7, 1, 2, 3, 4]`. The length of the array is between 0 and 10^5, and `k` is between 0 and 10^5.

## Approach
The approach is to use a temporary array to store the rotated elements, then copy them back to the original array. We can also use a more efficient approach by using three reversals: reverse the entire array, reverse the first `k` elements, and reverse the rest of the array.

## Complexity
- Time: O(n)
- Space: O(1) for the in-place approach, O(n) for the temporary array approach

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        // Calculate the actual number of steps to rotate
        k = k % nums.size();
        
        // Reverse the entire array
        reverse(nums.begin(), nums.end());
        
        // Reverse the first k elements
        reverse(nums.begin(), nums.begin() + k);
        
        // Reverse the rest of the array
        reverse(nums.begin() + k, nums.end());
    }
};

// Example usage:
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
- The `k % nums.size()` calculation ensures that the rotation is performed within the bounds of the array.
- The three-reversal approach is more efficient than the temporary array approach for large arrays.
- The `reverse` function from the C++ Standard Template Library (STL) is used to reverse the array and its subarrays.