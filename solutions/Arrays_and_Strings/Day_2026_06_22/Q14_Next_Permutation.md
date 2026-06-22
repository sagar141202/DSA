# Next Permutation

## Problem Statement
Given a collection of distinct integers, return all possible permutations of the collection in lexicographic order, and find the next permutation in the sorted order. If the given permutation is the last permutation, return the first permutation. The input array will contain distinct integers in the range [0, n-1] where n is the length of the array. For example, if the input is [1, 2, 3], the next permutation would be [1, 3, 2]. If the input is [3, 2, 1], the next permutation would be [1, 2, 3].

## Approach
The algorithm involves finding the first decreasing element from the right, then finding the smallest element greater than it and swapping them, and finally reversing the elements to the right of the decreased element. This approach ensures the next permutation is found in lexicographic order.

## Complexity
- Time: O(n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        // Find the first decreasing element from the right
        int i = nums.size() - 2;
        while (i >= 0 && nums[i] >= nums[i + 1]) {
            i--;
        }
        
        // If the entire array is in descending order, reverse it
        if (i >= 0) {
            int j = nums.size() - 1;
            while (nums[j] <= nums[i]) {
                j--;
            }
            swap(nums[i], nums[j]);
        }
        
        // Reverse the elements to the right of the decreased element
        int left = i + 1, right = nums.size() - 1;
        while (left < right) {
            swap(nums[left], nums[right]);
            left++;
            right--;
        }
    }
};
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
- The next permutation of an array can be found by swapping the first decreasing element from the right with the smallest element greater than it.
- If the entire array is in descending order, the next permutation is the first permutation, which can be obtained by reversing the array.
- The time complexity of the solution is O(n) where n is the length of the array, as each element is visited at most twice.