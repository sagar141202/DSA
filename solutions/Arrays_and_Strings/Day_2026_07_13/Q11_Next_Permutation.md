# Next Permutation

## Problem Statement
Given an array of integers, find the next lexicographically greater permutation. If no such permutation exists, return the first permutation in lexicographical order. The array consists of distinct integers from 1 to n, where n is the length of the array. For example, given the array [1, 2, 3], the next permutation is [1, 3, 2]. If the array is [3, 2, 1], the next permutation is [1, 2, 3].

## Approach
The algorithm involves finding the first decreasing element from the right, swapping it with the smallest greater element, and then reversing the elements to the right of the swap. This approach ensures that the next permutation is found efficiently.

## Complexity
- Time: O(n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

void nextPermutation(vector<int>& nums) {
    int i = nums.size() - 2;
    // Find the first decreasing element from the right
    while (i >= 0 && nums[i] >= nums[i + 1]) {
        i--;
    }
    // If no decreasing element is found, the array is the last permutation
    if (i >= 0) {
        int j = nums.size() - 1;
        // Find the smallest greater element to the right of the decreasing element
        while (nums[j] <= nums[i]) {
            j--;
        }
        // Swap the decreasing element with the smallest greater element
        swap(nums[i], nums[j]);
    }
    // Reverse the elements to the right of the swap
    int left = i + 1;
    int right = nums.size() - 1;
    while (left < right) {
        swap(nums[left], nums[right]);
        left++;
        right--;
    }
}

// Example usage:
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
- The next permutation of an array can be found by swapping the first decreasing element from the right with the smallest greater element to its right.
- If no decreasing element is found, the array is the last permutation, and the first permutation is returned.
- The algorithm has a time complexity of O(n) and a space complexity of O(1), making it efficient for large inputs.