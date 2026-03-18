# Permutations II

## Problem Statement
Given a collection of numbers that might contain duplicates, return all possible unique permutations. The input array is [1, 1, 2], and the desired output is [[1,1,2], [1,2,1], [2,1,1]]. The numbers in the input array may have duplicates, but the output permutations must be unique.

## Approach
The approach to solve this problem is to use recursion and backtracking. We will sort the array first and then use a helper function to generate all permutations. To avoid duplicates, we will skip the current iteration if the current element is the same as the previous one.

## Complexity
- Time: O(N * N!)
- Space: O(N)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

void backtrack(vector<int>& nums, vector<bool>& visited, vector<int>& path, vector<vector<int>>& result) {
    if (path.size() == nums.size()) {
        result.push_back(path);
        return;
    }
    for (int i = 0; i < nums.size(); i++) {
        // Skip the current iteration if the current element is the same as the previous one and the previous one has not been visited
        if (visited[i] || (i > 0 && nums[i] == nums[i-1] && !visited[i-1])) {
            continue;
        }
        visited[i] = true;
        path.push_back(nums[i]);
        backtrack(nums, visited, path, result);
        path.pop_back();
        visited[i] = false;
    }
}

vector<vector<int>> permuteUnique(vector<int>& nums) {
    vector<vector<int>> result;
    vector<bool> visited(nums.size(), false);
    vector<int> path;
    sort(nums.begin(), nums.end());
    backtrack(nums, visited, path, result);
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
```

## Key Takeaways
- Use recursion and backtracking to generate all permutations of the input array.
- Sort the array first to handle duplicates.
- Use a visited array to keep track of the elements that have been visited.