# Next Permutation

## Problem Statement
Given an array of integers, find the next lexicographically larger permutation. If no such permutation exists, return the first permutation in lexicographical order. The array should be modified in-place. For example, given the array [1, 2, 3], the next permutation is [1, 3, 2]. If the array is [3, 2, 1], the next permutation is [1, 2, 3] since it is the first permutation in lexicographical order.

## Approach
The algorithm involves finding the first decreasing element from the right, swapping it with the smallest larger element to its right, and reversing the elements to the right of the swapped element. This approach ensures that we generate the next lexicographically larger permutation.

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
    if (i >= 0) {
        int j = nums.size() - 1;
        // Find the smallest larger element to the right of i
        while (nums[j] <= nums[i]) {
            j--;
        }
        // Swap the elements at i and j
        swap(nums[i], nums[j]);
    }
    // Reverse the elements to the right of i
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
- The next permutation of an array can be found by swapping the first decreasing element from the right with the smallest larger element to its right.
- Reversing the elements to the right of the swapped element ensures that we generate the next lexicographically larger permutation.
- If no such permutation exists, the algorithm returns the first permutation in lexicographical order by reversing the entire array.