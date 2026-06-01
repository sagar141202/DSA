# Permutations II

## Problem Statement
Given a collection of numbers that might contain duplicates, return all unique permutations. The input collection is given as an array of integers, and the output should be a list of lists, where each sublist is a unique permutation of the input array. For example, given the input [1, 1, 2], the output should be [[1, 1, 2], [1, 2, 1], [2, 1, 1]]. The input array can contain any number of integers, and the integers can be any value.

## Approach
The approach to solve this problem is to use recursion and backtracking to generate all permutations of the input array, while keeping track of the elements that have already been used in the current permutation. We will also use a set to keep track of the permutations we have already found to avoid duplicates.

## Complexity
- Time: O(N! / (K1! * K2! * ... * Km!)) where N is the length of the input array, and K1, K2, ..., Km are the frequencies of each distinct element in the array.
- Space: O(N) for the recursion stack.

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
- To avoid duplicates in the permutations, we need to sort the input array first and then skip the duplicate elements in the backtracking process.
- We use a boolean array `used` to keep track of the elements that have already been used in the current permutation.
- The time complexity is O(N! / (K1! * K2! * ... * Km!)) because we divide the total number of permutations by the factorials of the frequencies of each distinct element.