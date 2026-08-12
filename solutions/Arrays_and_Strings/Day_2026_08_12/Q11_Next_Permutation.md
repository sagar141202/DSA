# Next Permutation

## Problem Statement
Given a collection of distinct integers, return all possible permutations of the collection in lexicographic order, and implement the next permutation function which rearranges numbers in the array to get the next permutation in lexicographic order. If such arrangement is not possible, it must rearrange it as the lowest possible order (i.e., sorted in ascending order). The replacement must be in-place. For example, given the array [1,2,3], the next permutation would be [1,3,2]. If the array is [3,2,1], the next permutation would be [1,2,3] as it is the lowest possible order.

## Approach
The algorithm involves finding the first decreasing element from the right, then finding its replacement from the right side, and finally reversing the elements to the right of the replacement. This approach ensures the next permutation is generated in lexicographic order. The process is repeated until no more permutations are possible.

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
        // find the replacement from the right side
        while (j > i && nums[j] <= nums[i]) {
            j--;
        }
        // swap the decreasing element with its replacement
        swap(nums[i], nums[j]);
    }
    // reverse the elements to the right of the replacement
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
Input: [1,2,3]
Output: [1,3,2]
Input: [3,2,1]
Output: [1,2,3]
```

## Key Takeaways
- To generate the next permutation, find the first decreasing element from the right.
- Swap this element with the smallest element greater than it from the right side.
- Reverse the elements to the right of the swapped element to get the next permutation.