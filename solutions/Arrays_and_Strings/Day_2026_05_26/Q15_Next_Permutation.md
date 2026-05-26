# Next Permutation

## Problem Statement
Given a collection of distinct numbers, return all possible permutations of the collection. However, this problem focuses on finding the next permutation in lexicographical order. For example, given the array [1, 2, 3], the next permutation would be [1, 3, 2]. If the array is the last permutation in lexicographical order (e.g., [3, 2, 1]), the function should return the first permutation (i.e., [1, 2, 3]). The input array will contain distinct integers and will not be empty.

## Approach
The algorithm involves finding the first decreasing element from the right, then finding the smallest element greater than it on the right, and swapping these two elements. Finally, reverse the elements to the right of the first decreasing element to get the next permutation.

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
        int i = nums.size() - 2;
        // Find the first decreasing element from the right
        while (i >= 0 && nums[i] >= nums[i + 1]) {
            i--;
        }
        
        // If we found a decreasing element, find the smallest element greater than it on the right
        if (i >= 0) {
            int j = nums.size() - 1;
            while (nums[j] <= nums[i]) {
                j--;
            }
            // Swap the decreasing element with the smallest element greater than it
            swap(nums[i], nums[j]);
        }
        
        // Reverse the elements to the right of the first decreasing element
        int left = i + 1;
        int right = nums.size() - 1;
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
- To find the next permutation, we need to find the first decreasing element from the right and swap it with the smallest element greater than it on the right.
- After swapping, we reverse the elements to the right of the first decreasing element to get the next permutation.
- If the input array is the last permutation in lexicographical order, the function returns the first permutation.