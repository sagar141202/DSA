# Permutations II

## Problem Statement
Given a collection of numbers that might contain duplicates, return all unique permutations. For example, given the input [1, 1, 2], the output should be [[1, 1, 2], [1, 2, 1], [2, 1, 1]]. The input will contain only numbers, and the length of the input will not exceed 10. The numbers in the input can be negative, zero, or positive.

## Approach
We can use a backtracking approach to generate all permutations of the input array. To handle duplicates, we will sort the array first and skip the current iteration if the current element is the same as the previous one. This ensures that we only consider each unique permutation once.

## Complexity
- Time: O(N! / (k1! * k2! * ... * kn!)) where N is the length of the input array and k1, k2, ..., kn are the frequencies of each distinct element
- Space: O(N) for the recursion stack

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

void backtrack(vector<int>& nums, vector<bool>& used, vector<int>& path, vector<vector<int>>& result) {
    if (path.size() == nums.size()) {
        result.push_back(path);
        return;
    }
    for (int i = 0; i < nums.size(); i++) {
        if (used[i] || (i > 0 && nums[i] == nums[i - 1] && !used[i - 1])) {
            continue;
        }
        used[i] = true;
        path.push_back(nums[i]);
        backtrack(nums, used, path, result);
        path.pop_back();
        used[i] = false;
    }
}

vector<vector<int>> permuteUnique(vector<int>& nums) {
    vector<vector<int>> result;
    vector<bool> used(nums.size(), false);
    vector<int> path;
    sort(nums.begin(), nums.end());
    backtrack(nums, used, path, result);
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
Input: [1, 1, 2]
Output: 
1 1 2 
1 2 1 
2 1 1 
```

## Key Takeaways
- Use backtracking to generate all permutations of the input array
- Sort the array first and skip the current iteration if the current element is the same as the previous one to handle duplicates
- Use a recursion stack to store the current permutation being generated