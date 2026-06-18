# Next Permutation

## Problem Statement
Generate the next permutation of a given array of integers in lexicographic order. If the given array is the last permutation, return the first permutation. The array contains distinct integers from 1 to n, where n is the length of the array. For example, given the array [1, 2, 3], the next permutation is [1, 3, 2]. If the array is [3, 2, 1], the next permutation is [1, 2, 3].

## Approach
The algorithm works by finding the first decreasing element from the right, then swapping it with the smallest element greater than it on its right. Finally, it reverses the elements to the right of the swapped element to get the next permutation.

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
    // If the array is the last permutation, reverse it
    if (i >= 0) {
        int j = nums.size() - 1;
        // Find the smallest element greater than nums[i] on its right
        while (nums[j] <= nums[i]) {
            j--;
        }
        // Swap nums[i] and nums[j]
        swap(nums[i], nums[j]);
    }
    // Reverse the elements to the right of the swapped element
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
- The algorithm has a time complexity of O(n) because it only needs to iterate through the array once to find the first decreasing element and the smallest element greater than it.
- The algorithm has a space complexity of O(1) because it only uses a constant amount of space to store the indices and the swapped elements.
- The algorithm works by finding the first decreasing element from the right and swapping it with the smallest element greater than it on its right, then reversing the elements to the right of the swapped element.