# Permutations II

## Problem Statement
Given a collection of numbers that might contain duplicates, return all possible unique permutations. The input will be a list of integers, and the output should be a list of lists, where each sublist is a unique permutation of the input list. For example, given the input [1,1,2], the output should be [[1,1,2], [1,2,1], [2,1,1]]. The input list will contain at most 20 elements, and all elements will be between 1 and 100.

## Approach
The approach to solve this problem involves using recursion and backtracking to generate all permutations of the input list, while skipping duplicates to ensure uniqueness. We will sort the input list first, and then use a recursive function to generate all permutations.

## Complexity
- Time: O(N! / (k1! * k2! * ... * kn!)) where N is the total number of elements and k1, k2, ..., kn are the frequencies of each distinct element
- Space: O(N) for the recursion stack

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

void backtrack(vector<int>& nums, int start, vector<vector<int>>& result) {
    if (start == nums.size()) {
        result.push_back(nums);
        return;
    }
    for (int i = start; i < nums.size(); i++) {
        // skip duplicates
        if (i > start && nums[i] == nums[start]) continue;
        swap(nums[start], nums[i]);
        backtrack(nums, start + 1, result);
        swap(nums[start], nums[i]);
    }
}

vector<vector<int>> permuteUnique(vector<int>& nums) {
    vector<vector<int>> result;
    sort(nums.begin(), nums.end());
    backtrack(nums, 0, result);
    return result;
}

int main() {
    vector<int> nums = {1, 1, 2};
    vector<vector<int>> result = permuteUnique(nums);
    for (auto& vec : result) {
        for (auto& num : vec) {
            cout << num << " ";
        }
        cout << endl;
    }
    return 0;
}
```

## Test Cases
```
Input: [1,1,2]
Output: [[1,1,2], [1,2,1], [2,1,1]]
Input: [2,2,1,1]
Output: [[1,1,2,2], [1,2,1,2], [1,2,2,1], [2,1,1,2], [2,1,2,1], [2,2,1,1]]
```

## Key Takeaways
- Sort the input list to group duplicate elements together
- Use recursion and backtracking to generate all permutations
- Skip duplicates by checking if the current element is the same as the previous one and if the current index is greater than the start index.