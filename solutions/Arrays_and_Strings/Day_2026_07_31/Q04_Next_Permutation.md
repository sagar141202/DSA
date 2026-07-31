# Next Permutation

## Problem Statement
Given an array of integers, find the next lexicographically greater permutation of the array. If no greater permutation exists, the array should be rearranged to its lexicographically smallest permutation. For example, given the array [1, 2, 3], the next permutation is [1, 3, 2]. If the input array is [3, 2, 1], the next permutation is [1, 2, 3]. The array can contain duplicate elements and the length of the array is in the range [1, 100].

## Approach
The approach is to find the first decreasing element from the right, then find the smallest element greater than it from the right, and swap them. Finally, reverse the elements to the right of the decreasing element. This process generates the next lexicographically greater permutation.

## Complexity
- Time: O(n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

void nextPermutation(vector<int>& nums) {
    int i = nums.size() - 2;
    // find the first decreasing element from the right
    while (i >= 0 && nums[i] >= nums[i + 1]) {
        i--;
    }
    if (i >= 0) {
        int j = nums.size() - 1;
        // find the smallest element greater than nums[i] from the right
        while (nums[j] <= nums[i]) {
            j--;
        }
        // swap nums[i] and nums[j]
        swap(nums[i], nums[j]);
    }
    // reverse the elements to the right of the decreasing element
    int left = i + 1;
    int right = nums.size() - 1;
    while (left < right) {
        swap(nums[left], nums[right]);
        left++;
        right--;
    }
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
- The key to solving this problem is to find the first decreasing element from the right and then find the smallest element greater than it from the right.
- The use of two pointers, one from the left and one from the right, can simplify the process of reversing the elements.
- The time complexity of this solution is O(n), where n is the length of the input array, because we potentially iterate over the entire array.