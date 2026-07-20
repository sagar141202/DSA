# Rotate Array

## Problem Statement
Given an array of integers `nums` and an integer `k`, rotate the array to the right by `k` steps. The rotation should be performed in-place, meaning that the original array should be modified. For example, if `nums = [1, 2, 3, 4, 5, 6, 7]` and `k = 3`, the rotated array should be `[5, 6, 7, 1, 2, 3, 4]`. The length of the array is denoted by `n`, where `1 <= n <= 10^5`, and `0 <= k <= 10^5`.

## Approach
The algorithm involves using a temporary array to store the rotated elements, or alternatively, using a three-step reverse approach to achieve the rotation in-place. The key idea is to reverse the entire array, then reverse the first `k` elements, and finally reverse the remaining elements.

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
        
        // Reverse the remaining elements
        reverse(nums.begin() + k, nums.end());
    }
};

int main() {
    Solution solution;
    vector<int> nums = {1, 2, 3, 4, 5, 6, 7};
    int k = 3;
    solution.rotate(nums, k);
    
    // Print the rotated array
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
- The rotation can be achieved by reversing the array three times.
- The actual number of steps to rotate is `k % n`, where `n` is the length of the array.
- The in-place approach has a space complexity of O(1), making it more efficient than the temporary array approach for large inputs.