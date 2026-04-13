# Permutations II

## Problem Statement
Given a collection of numbers that might contain duplicates, return all possible unique permutations. The input is a list of integers, and the output should be a list of lists, where each sublist is a unique permutation of the input list. For example, given the input [1,1,2], the output should be [[1,1,2],[1,2,1],[2,1,1]].

## Approach
The solution uses backtracking to generate all permutations of the input list. It sorts the input list to handle duplicates and skips the same element to avoid duplicate permutations. The algorithm recursively generates all permutations by swapping each element with the remaining elements.

## Complexity
- Time: O(N! / (k1! * k2! * ... * kn!)) where N is the length of the input list and k1, k2, ..., kn are the frequencies of each distinct element
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
    unordered_set<int> used;
    for (int i = start; i < nums.size(); i++) {
        if (used.find(nums[i]) != used.end()) continue;
        used.insert(nums[i]);
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
    for (auto& perm : result) {
        for (auto& num : perm) {
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
Output: [[1,1,2],[1,2,1],[2,1,1]]
```

## Key Takeaways
- Use backtracking to generate all permutations of the input list
- Sort the input list to handle duplicates and skip the same element to avoid duplicate permutations
- Use an unordered set to keep track of used elements in the current permutation to avoid duplicates