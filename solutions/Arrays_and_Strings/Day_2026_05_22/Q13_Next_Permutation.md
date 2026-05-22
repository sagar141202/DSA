# Next Permutation

## Problem Statement
Given an array of integers, find the next lexicographically larger permutation. If no such permutation exists, return the first permutation in lexicographical order. For example, given the array `[1, 2, 3]`, the next permutation would be `[1, 3, 2]`. If the input array is `[3, 2, 1]`, the output would be `[1, 2, 3]`. The array can contain duplicate elements and the length of the array is between 1 and 100.

## Approach
The approach involves finding the largest index `k` such that `nums[k] < nums[k + 1]`. If no such index exists, the permutation is the last permutation. Then, we find the largest index `l > k` such that `nums[k] < nums[l]` and swap `nums[k]` and `nums[l]`. Finally, we reverse the sub-array `nums[k + 1:]`.

## Complexity
- Time: O(n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

void nextPermutation(vector<int>& nums) {
    int n = nums.size();
    int k = n - 2;
    // find the largest index k such that nums[k] < nums[k + 1]
    while (k >= 0 && nums[k] >= nums[k + 1]) {
        k--;
    }
    if (k >= 0) {
        // find the largest index l > k such that nums[k] < nums[l]
        int l = n - 1;
        while (nums[l] <= nums[k]) {
            l--;
        }
        // swap nums[k] and nums[l]
        swap(nums[k], nums[l]);
    }
    // reverse the sub-array nums[k + 1:]
    reverse(nums.begin() + k + 1, nums.end());
}

int main() {
    vector<int> nums = {1, 2, 3};
    nextPermutation(nums);
    for (int num : nums) {
        cout << num << " ";
    }
    return 0;
}
```

## Test Cases
```
Input: [1, 2, 3]
Output: [1, 3, 2]
Input: [3, 2, 1]
Output: [1, 2, 3]
Input: [1, 1, 5]
Output: [1, 5, 1]
```

## Key Takeaways
- The next permutation of an array can be found by swapping the largest index `k` such that `nums[k] < nums[k + 1]` with the largest index `l > k` such that `nums[k] < nums[l]`.
- If no such index `k` exists, the permutation is the last permutation, and we need to reverse the entire array to get the first permutation.
- The time complexity of this solution is O(n), where n is the length of the input array.