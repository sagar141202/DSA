# Rotate Array

## Problem Statement
Given an array of integers `nums` and an integer `k`, rotate the array to the right by `k` steps. The length of the array is denoted by `n`. If `k` is greater than `n`, the effective number of steps is `k % n`. For example, if `nums = [1, 2, 3, 4, 5, 6, 7]` and `k = 3`, the output should be `[5, 6, 7, 1, 2, 3, 4]`. The function should modify the input array in-place.

## Approach
We can solve this problem by using a temporary array to store the rotated elements, or by using a three-step reverse approach to achieve in-place rotation. The three-step approach involves reversing the entire array, then reversing the first `k` elements, and finally reversing the remaining elements.

## Complexity
- Time: O(n)
- Space: O(1) for the in-place approach, O(n) for the temporary array approach

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

void rotate(vector<int>& nums, int k) {
    // Calculate the effective number of steps
    k = k % nums.size();
    
    // Reverse the entire array
    reverse(nums.begin(), nums.end());
    
    // Reverse the first k elements
    reverse(nums.begin(), nums.begin() + k);
    
    // Reverse the remaining elements
    reverse(nums.begin() + k, nums.end());
}

// Example usage
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
- The three-step reverse approach allows for in-place rotation with a time complexity of O(n) and a space complexity of O(1).
- The temporary array approach has a time complexity of O(n) but a space complexity of O(n).
- The effective number of steps is `k % n`, where `n` is the length of the array.