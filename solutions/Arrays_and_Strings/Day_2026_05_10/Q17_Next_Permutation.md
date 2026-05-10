# Next Permutation

## Problem Statement
Given an array of integers, find the next lexicographically larger permutation of the array. If no such permutation exists, arrange the elements in ascending order. The array consists of distinct integers from 1 to n, where n is the length of the array. For example, given the array [1, 2, 3], the next permutation would be [1, 3, 2]. If the input array is the last permutation in lexicographical order (e.g., [3, 2, 1]), the function should return the first permutation in lexicographical order (i.e., [1, 2, 3]).

## Approach
The algorithm involves finding the first decreasing element from the right, then swapping it with the smallest element greater than it on its right side, and finally reversing the elements to the right of the swapped pair. This approach ensures that the resulting permutation is the next lexicographically larger permutation.

## Complexity
- Time: O(n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

void nextPermutation(vector<int>& nums) {
    // Find the first decreasing element from the right
    int i = nums.size() - 2;
    while (i >= 0 && nums[i] >= nums[i + 1]) {
        i--;
    }

    // If the array is the last permutation, reverse it
    if (i < 0) {
        reverse(nums.begin(), nums.end());
        return;
    }

    // Find the smallest element greater than nums[i] on its right side
    int j = nums.size() - 1;
    while (nums[j] <= nums[i]) {
        j--;
    }

    // Swap nums[i] and nums[j]
    swap(nums[i], nums[j]);

    // Reverse the elements to the right of the swapped pair
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
- The algorithm uses a two-pointer approach to find the first decreasing element and the smallest greater element.
- The time complexity is O(n) due to the potential need to scan the entire array.
- The space complexity is O(1) since only a constant amount of space is used to store the indices and temporary swaps.