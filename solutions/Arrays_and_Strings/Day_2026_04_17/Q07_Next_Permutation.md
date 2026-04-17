# Next Permutation

## Problem Statement
Given a collection of distinct numbers, return all possible permutations of the collection, and find the next permutation in lexicographic order. If the current permutation is the last permutation in lexicographic order, return the first permutation. For example, given the array [1, 2, 3], the next permutation of [1, 2, 3] is [1, 3, 2]. The next permutation of [3, 2, 1] is [1, 2, 3]. The array is modified in-place.

## Approach
The algorithm involves finding the first decreasing element from the right, swapping it with the smallest element greater than it to its right, and reversing the elements to its right. This approach ensures the next permutation is generated in lexicographic order.

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
        // find the smallest element greater than nums[i] to its right
        while (nums[j] <= nums[i]) {
            j--;
        }
        // swap nums[i] and nums[j]
        swap(nums[i], nums[j]);
    }
    // reverse the elements to the right of i
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
```

## Key Takeaways
- The algorithm modifies the input array in-place.
- The time complexity is O(n) due to the potential reversal of the entire array.
- The space complexity is O(1) as only a constant amount of space is used.