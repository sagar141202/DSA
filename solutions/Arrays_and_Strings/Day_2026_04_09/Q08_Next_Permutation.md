# Next Permutation

## Problem Statement
Given an array of integers, find the next lexicographically larger permutation. If no such permutation exists, rearrange the elements to form the smallest possible permutation. For example, given the array [1, 2, 3], the next permutation is [1, 3, 2]. If the input array is [3, 2, 1], the next permutation is [1, 2, 3] since it is the smallest possible permutation. The array is 1-indexed and contains distinct integers from 1 to n, where n is the size of the array.

## Approach
The algorithm involves finding the first decreasing element from the right, swapping it with the smallest element greater than it, and then reversing the elements to the right of the swapped element. This approach ensures that the resulting permutation is the next lexicographically larger permutation.

## Complexity
- Time: O(n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

void nextPermutation(vector<int>& nums) {
    // find the first decreasing element from the right
    int i = nums.size() - 2;
    while (i >= 0 && nums[i] >= nums[i + 1]) {
        i--;
    }
    
    // if no decreasing element is found, the array is the last permutation
    if (i >= 0) {
        // find the smallest element greater than nums[i] from the right
        int j = nums.size() - 1;
        while (nums[j] <= nums[i]) {
            j--;
        }
        // swap nums[i] and nums[j]
        swap(nums[i], nums[j]);
    }
    // reverse the elements to the right of the swapped element
    int left = i + 1;
    int right = nums.size() - 1;
    while (left < right) {
        swap(nums[left], nums[right]);
        left++;
        right--;
    }
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
- The next lexicographically larger permutation can be found by swapping the first decreasing element from the right with the smallest element greater than it.
- If no decreasing element is found, the array is the last permutation, and the smallest possible permutation is returned by reversing the array.
- The time complexity is O(n) because in the worst case, we need to traverse the entire array to find the decreasing element and the smallest element greater than it.