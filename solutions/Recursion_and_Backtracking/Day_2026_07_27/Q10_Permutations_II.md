# Permutations II

## Problem Statement
Given a collection of numbers that might contain duplicates, return all possible unique permutations. The input is a list of integers, and the output should be a list of lists, where each sublist is a unique permutation of the input list. For example, given the input [1, 1, 2], the output should be [[1, 1, 2], [1, 2, 1], [2, 1, 1]]. The input list is not empty and does not contain more than 20 elements.

## Approach
The problem can be solved using recursion and backtracking. We will generate all permutations of the input list and then remove duplicates. We can use a set to keep track of the permutations we have already seen to avoid duplicates. The recursion will be used to generate all possible permutations, and the backtracking will be used to explore different branches of the recursion tree.

## Complexity
- Time: O(N! / (K1! * K2! * ... * Km!)) where N is the length of the input list and K1, K2, ..., Km are the frequencies of each number in the list
- Space: O(N! / (K1! * K2! * ... * Km!)) for storing the result

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

void backtrack(vector<int>& nums, vector<bool>& used, vector<int>& path, vector<vector<int>>& res) {
    if (path.size() == nums.size()) {
        res.push_back(path);
        return;
    }
    for (int i = 0; i < nums.size(); i++) {
        if (used[i] || (i > 0 && nums[i] == nums[i - 1] && !used[i - 1])) {
            continue;
        }
        used[i] = true;
        path.push_back(nums[i]);
        backtrack(nums, used, path, res);
        path.pop_back();
        used[i] = false;
    }
}

vector<vector<int>> permuteUnique(vector<int>& nums) {
    sort(nums.begin(), nums.end());
    vector<vector<int>> res;
    vector<bool> used(nums.size(), false);
    vector<int> path;
    backtrack(nums, used, path, res);
    return res;
}

int main() {
    vector<int> nums = {1, 1, 2};
    vector<vector<int>> res = permuteUnique(nums);
    for (auto& perm : res) {
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
Input: [1, 1, 2]
Output: 
1 1 2 
1 2 1 
2 1 1 
```

## Key Takeaways
- The recursion and backtracking approach can be used to solve permutation problems with duplicates.
- Using a set to keep track of the permutations we have already seen can help avoid duplicates, but in this case, we use sorting and skipping the same elements to avoid duplicates.
- The time complexity of the solution depends on the number of unique permutations, which can be calculated using the formula N! / (K1! * K2! * ... * Km!).