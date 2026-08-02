# Permutations II

## Problem Statement
Given a collection of numbers that might contain duplicates, return all possible unique permutations. The input collection is given as an array of integers, and the output should be a list of lists, where each sublist is a unique permutation of the input array. For example, given the input [1, 1, 2], the output should be [[1, 1, 2], [1, 2, 1], [2, 1, 1]]. The length of the input array will be between 1 and 9, and each integer in the array will be between 1 and 9.

## Approach
The approach to solve this problem is to use recursion and backtracking. We will generate all permutations of the input array and skip duplicates by sorting the array and only exploring branches where the current element is different from the previous one. This ensures that we do not generate duplicate permutations.

## Complexity
- Time: O(N! / (k1! * k2! * ... * kn!)) where N is the length of the input array and k1, k2, ..., kn are the frequencies of each distinct element in the array
- Space: O(N) for the recursion stack

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

void backtrack(vector<int>& nums, int start, vector<vector<int>>& result) {
    if (start == nums.size()) {
        result.push_back(nums);
    } else {
        for (int i = start; i < nums.size(); i++) {
            if (i > start && nums[i] == nums[start]) continue;
            swap(nums[start], nums[i]);
            backtrack(nums, start + 1, result);
            swap(nums[start], nums[i]);
        }
    }
}

vector<vector<int>> permuteUnique(vector<int>& nums) {
    vector<vector<int>> result;
    sort(nums.begin(), nums.end());
    backtrack(nums, 0, result);
    return result;
}
```

## Test Cases
```
Input: [1, 1, 2]
Output: [[1, 1, 2], [1, 2, 1], [2, 1, 1]]
Input: [2, 2, 1, 1]
Output: [[1, 1, 2, 2], [1, 2, 1, 2], [1, 2, 2, 1], [2, 1, 1, 2], [2, 1, 2, 1], [2, 2, 1, 1]]
```

## Key Takeaways
- Use recursion and backtracking to generate all permutations of the input array.
- Skip duplicates by sorting the array and only exploring branches where the current element is different from the previous one.
- The time complexity is reduced by avoiding duplicate permutations, resulting in a more efficient solution.