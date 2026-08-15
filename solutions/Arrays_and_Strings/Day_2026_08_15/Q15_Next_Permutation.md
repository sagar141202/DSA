# Next Permutation

## Problem Statement
Given a collection of distinct numbers, find all permutations of the given numbers. However, this problem focuses on finding the next permutation in lexicographical order. If the current permutation is the last permutation in lexicographical order, the function should return the first permutation. For example, given the array [1, 2, 3], the next permutation of [1, 2, 3] is [1, 3, 2]. The next permutation of [3, 2, 1] is [1, 2, 3]. The function should use only constant extra space.

## Approach
The algorithm involves finding the first decreasing element from the right, then finding its successor and swapping them. After that, we reverse the elements to the right of the decreased element to get the next permutation. The intuition is to find the smallest possible change that can be made to the current permutation to get the next permutation.

## Complexity
- Time: O(n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        int i = nums.size() - 2;
        // find the first decreasing element from the right
        while (i >= 0 && nums[i] >= nums[i + 1]) {
            i--;
        }
        // if we found a decreasing element, find its successor and swap them
        if (i >= 0) {
            int j = nums.size() - 1;
            while (nums[j] <= nums[i]) {
                j--;
            }
            swap(nums[i], nums[j]);
        }
        // reverse the elements to the right of the decreased element
        int left = i + 1, right = nums.size() - 1;
        while (left < right) {
            swap(nums[left], nums[right]);
            left++;
            right--;
        }
    }
};
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
- We need to find the first decreasing element from the right to determine the next permutation.
- The next permutation is obtained by swapping the decreased element with its successor and then reversing the elements to the right of the decreased element.
- The function should use only constant extra space.