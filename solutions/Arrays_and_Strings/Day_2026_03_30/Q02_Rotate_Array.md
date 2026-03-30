# Rotate Array

## Problem Statement
Given an array of integers `nums` and an integer `k`, rotate the array to the right by `k` steps. The length of the array is `n`. For example, if `nums = [1, 2, 3, 4, 5, 6, 7]` and `k = 3`, the rotated array would be `[5, 6, 7, 1, 2, 3, 4]`. The constraint is that `1 <= n <= 10^5` and `0 <= k <= 10^5`.

## Approach
We can solve this problem by using the reverse algorithm to reverse the entire array, then reverse the first `k` elements, and finally reverse the rest of the array. This approach ensures that the array is rotated to the right by `k` steps. We can also use the modulo operator to handle cases where `k` is greater than `n`.

## Complexity
- Time: O(n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

void rotate(vector<int>& nums, int k) {
    k = k % nums.size(); // handle cases where k is greater than n
    reverse(nums.begin(), nums.end()); // reverse the entire array
    reverse(nums.begin(), nums.begin() + k); // reverse the first k elements
    reverse(nums.begin() + k, nums.end()); // reverse the rest of the array
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
```

## Key Takeaways
- Use the reverse algorithm to rotate the array.
- Use the modulo operator to handle cases where `k` is greater than `n`.
- This solution has a time complexity of O(n) and a space complexity of O(1).