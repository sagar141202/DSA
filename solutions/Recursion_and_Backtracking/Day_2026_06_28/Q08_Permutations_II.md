# Permutations II

## Problem Statement
Given a collection of numbers that might contain duplicates, return all possible unique permutations. The input is a list of integers, and the output should be a list of lists, where each sublist is a unique permutation of the input list. For example, given the input [1, 1, 2], the output should be [[1, 1, 2], [1, 2, 1], [2, 1, 1]]. The length of the input list will not exceed 10, and the elements in the list will be in the range [1, 10^5].

## Approach
The problem can be solved using recursion and backtracking. The idea is to generate all permutations of the input list and then remove duplicates. We can use a sorting step to ensure that duplicate permutations are adjacent to each other, making them easier to remove.

## Complexity
- Time: O(N! / (K1! * K2! * ... * Km!)) where N is the length of the input list and K1, K2, ..., Km are the frequencies of each number in the list
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
        if (i != start && nums[i] == nums[start]) continue;
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
Input: [1, 1, 2]
Output: [[1, 1, 2], [1, 2, 1], [2, 1, 1]]
Input: [2, 2, 1, 1]
Output: [[1, 1, 2, 2], [1, 2, 1, 2], [1, 2, 2, 1], [2, 1, 1, 2], [2, 1, 2, 1], [2, 2, 1, 1]]
```

## Key Takeaways
- Use recursion and backtracking to generate all permutations of the input list
- Remove duplicates by sorting the input list and skipping duplicate elements during the backtracking process
- The time complexity depends on the number of unique permutations, which can be calculated using the formula N! / (K1! * K2! * ... * Km!) where N is the length of the input list and K1, K2, ..., Km are the frequencies of each number in the list