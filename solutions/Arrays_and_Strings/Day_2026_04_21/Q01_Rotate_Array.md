# Rotate Array

## Problem Statement
Given an array of integers `nums` and an integer `k`, rotate the array to the right by `k` steps. The rotation should be performed in-place, meaning that the original array should be modified. For example, if `nums = [1, 2, 3, 4, 5, 6, 7]` and `k = 3`, the rotated array should be `[5, 6, 7, 1, 2, 3, 4]`. If `k` is greater than the length of the array, the rotation should be performed by `k % n` steps, where `n` is the length of the array.

## Approach
The algorithm uses a temporary array to store the rotated elements, and then copies them back to the original array. This approach ensures that the rotation is performed correctly and efficiently. The key insight is to use the modulo operator to handle cases where `k` is greater than the length of the array. The rotation is performed in three steps: reverse the entire array, reverse the first `k` elements, and reverse the rest of the array.

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
```

## Key Takeaways
- The rotation can be performed in-place using a temporary array or by reversing the array three times.
- The modulo operator is used to handle cases where `k` is greater than the length of the array.
- The time complexity of the solution is O(n), where n is the length of the array.