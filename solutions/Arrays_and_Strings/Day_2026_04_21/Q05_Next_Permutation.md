# Next Permutation

## Problem Statement
Given an array of integers, find the next lexicographically larger permutation. If there is no such permutation, rearrange the elements to form the smallest possible permutation. For example, given the array `[1, 2, 3]`, the next permutation is `[1, 3, 2]`. If the given array is the last permutation (e.g., `[3, 2, 1]`), the function should return the first permutation, which is `[1, 2, 3]`. The array consists of distinct integers from 1 to n, where n is the length of the array.

## Approach
The algorithm finds the largest index k such that the current element is less than the next one. Then, it finds the largest index l > k such that the current element at index k is less than the element at index l. The elements at indices k and l are swapped, and the sub-array from index k + 1 to the end is reversed.

## Complexity
- Time: O(n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

void nextPermutation(vector<int>& nums) {
    int n = nums.size();
    int i = n - 2;
    // find the largest index k such that nums[k] < nums[k + 1]
    while (i >= 0 && nums[i] >= nums[i + 1]) {
        i--;
    }
    if (i >= 0) {
        int j = n - 1;
        // find the largest index l > k such that nums[k] < nums[l]
        while (j > i && nums[j] <= nums[i]) {
            j--;
        }
        // swap nums[i] and nums[j]
        swap(nums[i], nums[j]);
    }
    // reverse the sub-array from index i + 1 to the end
    reverse(nums.begin() + i + 1, nums.end());
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
- The next permutation of an array can be found by swapping the first decreasing element with the smallest larger element to its right.
- If no such pair exists, the array is the last permutation, and the function should return the first permutation.
- The sub-array from the index after the swapped pair to the end should be reversed to get the smallest possible permutation.