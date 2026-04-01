# Next Permutation

## Problem Statement
Given a collection of distinct numbers, return all possible permutations of the collection in ascending order, and for a given permutation, find the next permutation in lexicographically sorted order. If the given permutation is the last permutation in lexicographically sorted order, return the first permutation. For example, given the array [1,2,3], the next permutation of [1,2,3] is [1,3,2]. The next permutation of [3,2,1] is [1,2,3]. The array is modified in-place.

## Approach
The algorithm works by finding the largest index k such that nums[k] < nums[k + 1]. If no such index exists, the permutation is the last permutation. Then, we find the largest index l > k such that nums[k] < nums[l] and swap nums[k] and nums[l]. Finally, we reverse the sub-array nums[k + 1:] to get the next permutation.

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
        // find the largest index k such that nums[k] < nums[k + 1]
        while (i >= 0 && nums[i + 1] <= nums[i]) {
            i--;
        }
        
        if (i >= 0) {
            int j = nums.size() - 1;
            // find the largest index l > k such that nums[k] < nums[l]
            while (nums[j] <= nums[i]) {
                j--;
            }
            // swap nums[k] and nums[l]
            swap(nums[i], nums[j]);
        }
        
        // reverse the sub-array nums[k + 1:]
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
Input: [1,2,3]
Output: [1,3,2]
Input: [3,2,1]
Output: [1,2,3]
```

## Key Takeaways
- The algorithm modifies the input array in-place to generate the next permutation.
- If the input array is the last permutation in lexicographically sorted order, the algorithm returns the first permutation.
- The time complexity of the algorithm is O(n), where n is the number of elements in the input array.