# Permutations II

## Problem Statement
Given a collection of numbers that might contain duplicates, return all possible unique permutations. The input is a list of integers, and the output should be a list of lists, where each sublist is a unique permutation of the input list. For example, given the input [1, 1, 2], the output should be [[1, 1, 2], [1, 2, 1], [2, 1, 1]]. The length of the input list is at most 10, and the elements are in the range [1, 1000].

## Approach
To solve this problem, we can use a backtracking approach with recursion. We will generate all permutations of the input list and then remove duplicates. The key idea is to use a set to keep track of the permutations we have seen so far and avoid generating duplicate permutations.

## Complexity
- Time: O(N! / (k1! * k2! * ... * km!)) where N is the length of the input list and k1, k2, ..., km are the frequencies of each number in the list
- Space: O(N! / (k1! * k2! * ... * km!)) for storing the permutations

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

void backtrack(vector<int>& nums, vector<bool>& visited, vector<int>& current, vector<vector<int>>& result) {
    if (current.size() == nums.size()) {
        result.push_back(current);
        return;
    }
    for (int i = 0; i < nums.size(); i++) {
        if (visited[i] || (i > 0 && nums[i] == nums[i - 1] && !visited[i - 1])) {
            continue;
        }
        visited[i] = true;
        current.push_back(nums[i]);
        backtrack(nums, visited, current, result);
        current.pop_back();
        visited[i] = false;
    }
}

vector<vector<int>> permuteUnique(vector<int>& nums) {
    sort(nums.begin(), nums.end());
    vector<vector<int>> result;
    vector<bool> visited(nums.size(), false);
    vector<int> current;
    backtrack(nums, visited, current, result);
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
Output: [[1, 1, 2], [1, 2, 1], [2, 1, 1]]
Input: [2, 2, 1, 1]
Output: [[1, 1, 2, 2], [1, 2, 1, 2], [1, 2, 2, 1], [2, 1, 1, 2], [2, 1, 2, 1], [2, 2, 1, 1]]
```

## Key Takeaways
- The problem can be solved using a backtracking approach with recursion.
- To avoid generating duplicate permutations, we need to skip the same numbers in the same position.
- The time complexity is O(N! / (k1! * k2! * ... * km!)) where N is the length of the input list and k1, k2, ..., km are the frequencies of each number in the list.