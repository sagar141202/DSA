# Next Permutation

## Problem Statement
The next permutation problem is a classic problem in computer science, where you are given an array of integers representing a permutation of numbers from 1 to n. The task is to find the next lexicographically larger permutation. If no such permutation exists, the function should return the first permutation (i.e., the permutation in ascending order). The array can contain duplicates. For example, given the array [1, 2, 3], the next permutation is [1, 3, 2]. Given the array [3, 2, 1], the next permutation is [1, 2, 3].

## Approach
The algorithm works by finding the first decreasing element from the right and swapping it with the smallest element to its right that is greater than it. Then, it reverses the elements to the right of the decreased element. This approach ensures that we find the next lexicographically larger permutation.

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
        // find the smallest element to the right that is greater than nums[i]
        while (j > i && nums[j] <= nums[i]) {
            j--;
        }
        // swap nums[i] and nums[j]
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
- The next permutation of a given array can be found by finding the first decreasing element from the right and swapping it with the smallest element to its right that is greater than it.
- After swapping, we need to reverse the elements to the right of the decreased element to ensure that we find the next lexicographically larger permutation.
- The time complexity of this solution is O(n) because in the worst case, we need to traverse the entire array.