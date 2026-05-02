# Next Permutation

## Problem Statement
Given an array of integers, find the next lexicographically larger permutation. If no such permutation exists, rearrange the elements to obtain the first permutation (i.e., in ascending order). The array consists of distinct integers from 1 to n, where n is the length of the array. For example, if the input array is [1, 2, 3], the next permutation is [1, 3, 2]. If the input array is [3, 2, 1], the next permutation is [1, 2, 3].

## Approach
The algorithm involves finding the first decreasing element from the right, then finding the smallest element greater than it and swapping them. Finally, reverse the elements to the right of the swapped element. This approach ensures the next permutation is lexicographically larger.

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
        // find the smallest element greater than nums[i]
        while (nums[j] <= nums[i]) {
            j--;
        }
        // swap nums[i] and nums[j]
        swap(nums[i], nums[j]);
    }
    // reverse the elements to the right of the swapped element
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
- The next permutation of an array is obtained by finding the first decreasing element from the right and swapping it with the smallest element greater than it.
- If no such permutation exists, the array is rearranged to obtain the first permutation (i.e., in ascending order).
- The algorithm has a time complexity of O(n) and a space complexity of O(1), where n is the length of the array.