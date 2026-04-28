# Next Permutation

## Problem Statement
Given an array of integers, find the next lexicographically greater permutation of the array. If no such permutation exists, then the array is rearranged to the lexicographically smallest permutation. For example, if the input array is [1, 2, 3], the next permutation would be [1, 3, 2]. If the input array is [3, 2, 1], the next permutation would be [1, 2, 3]. The array contains distinct integers from 1 to n, where n is the length of the array.

## Approach
The algorithm works by finding the first decreasing element from the right, then finding the smallest element greater than it on the right side, and swapping them. Finally, it reverses the elements on the right side of the decreasing element to get the next permutation.

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
        // find the smallest element greater than nums[i] on the right side
        while (nums[j] <= nums[i]) {
            j--;
        }
        // swap nums[i] and nums[j]
        swap(nums[i], nums[j]);
    }
    // reverse the elements on the right side of i
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
- The algorithm has a time complexity of O(n) because it only needs to traverse the array once to find the decreasing element and the smallest greater element.
- The algorithm has a space complexity of O(1) because it only uses a constant amount of space to store the indices and temporary swaps.
- The next permutation of an array can be found by swapping the first decreasing element with the smallest greater element on the right side, and then reversing the elements on the right side.