# Next Permutation

## Problem Statement
The next permutation problem is a classic problem in computer science where we are given an array of integers and we need to find the next lexicographically larger permutation of the array. If no such permutation exists, we need to return the first permutation, which is the array in ascending order. The array contains distinct integers from 1 to n, where n is the size of the array. For example, given the array [1, 2, 3], the next permutation is [1, 3, 2]. If the input array is [3, 2, 1], the next permutation is [1, 2, 3] because [3, 2, 1] is the last permutation.

## Approach
The algorithm used to solve this problem is to find the first decreasing element from the right, then find the smallest element greater than it from the right, and swap them. After that, we reverse the elements to the right of the first decreasing element to get the smallest possible permutation.

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
    // reverse the elements to the right of the first decreasing element
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
- We need to find the first decreasing element from the right to determine the next permutation.
- We should find the smallest element greater than the first decreasing element from the right to swap with it.
- Reversing the elements to the right of the first decreasing element gives us the smallest possible permutation.